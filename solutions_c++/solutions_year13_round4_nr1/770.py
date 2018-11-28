#include <algorithm>
#include <iostream>
#include <fstream>
#include <stddef.h>
#include <stdlib.h>
#include <string>

struct journey
{
	unsigned int start;
	unsigned int end;
	unsigned int passengercount;
	
	unsigned int residualincount;
	unsigned int residualoutcount;
};

struct endpoint
{
	unsigned int location;
	unsigned int passengercount;
	unsigned int residualcount;
};

struct problem
{
	unsigned int stopcount;
	unsigned int journeycount;

	journey journeys [1000];

	unsigned int endidx [1000];
};

unsigned long long dist_cost (const problem &p, unsigned int distance)
{
	return (unsigned long long) p.stopcount * distance - (((unsigned long long) distance - 1) * (unsigned long long) distance) / 2;
}

unsigned int calc_journey_cost (const problem &p, const journey &j)
{
	unsigned long long cost = dist_cost (p, j.end - j.start) % 1000002013;
	cost *= j.passengercount;
	cost %= 1000002013;
	return (unsigned int) cost;
}

unsigned int total_cost (const problem &p)
{
	unsigned int cost = 0;
	for (unsigned int i = 0; i < p.journeycount; i++)
	{
		cost += calc_journey_cost (p, p.journeys [i]);
		cost %= 1000002013;
	}
	return cost;
}

bool journey_comparator (const journey &a, const journey &b)
{
	return a.start < b.start;
}

problem p;

bool endidx_comparator (const unsigned int &a, const unsigned int &b)
{
	return p.journeys [a].end < p.journeys [b].end;
}

int main ()
{
	std::ifstream in ("a.in");
	std::ofstream out ("a.out");

	unsigned int testcount;
	in >> testcount;

	for (unsigned int i = 0; i < testcount; i++)
	{
		std::cout << "Case #" << (i + 1) << ":" << std::endl;

		in >> p.stopcount;
		in >> p.journeycount;

		for (unsigned int j = 0; j < p.journeycount; j++)
		{
			in >> p.journeys [j].start;
			in >> p.journeys [j].end;
			in >> p.journeys [j].passengercount;
			p.journeys [j].residualincount = p.journeys [j].passengercount;
			p.journeys [j].residualoutcount = p.journeys [j].passengercount;

			p.endidx [j] = j;
		}
		
		std::sort (p.journeys, p.journeys + p.journeycount, journey_comparator);
		std::sort (p.endidx, p.endidx + p.journeycount, endidx_comparator);

		int referencecost = total_cost (p);
		int mincost = 0;

		while (true)
		{
			// 1. 
			unsigned int bestlength = 0xFFFFFFFF;
			unsigned int startjourney = 0;
			unsigned int endjourney = 0;

			for (unsigned int startidx = 0; startidx < p.journeycount; startidx++)
			{
				// Find the closest exit station in front or equal to the start station
				unsigned int start = p.journeys [startidx].start;
				unsigned int endidxidxubound = p.journeycount - 1;
				unsigned int endidxidxlbound = 0;

				while (endidxidxubound - endidxidxlbound > 1)
				{
					unsigned int uboundend = p.journeys [p.endidx [endidxidxubound]].end;
					unsigned int lboundend = p.journeys [p.endidx [endidxidxlbound]].end;
					unsigned int mididxidx = (endidxidxubound + endidxidxlbound) / 2;
					unsigned int midend = p.journeys [p.endidx [mididxidx]].end;

					if (midend < start)
					{
						// use 2nd half
						endidxidxlbound = mididxidx;
					}
					else
					{
						endidxidxubound = mididxidx;
					}
				}

				for (unsigned int endidxidx = endidxidxlbound; endidxidx < p.journeycount; endidxidx++)
				{
					unsigned int endidx = p.endidx [endidxidx];
					if (p.journeys [endidx].end < p.journeys [startidx].start) { continue; }
					if (p.journeys [startidx].residualincount == 0) { continue; }
					if (p.journeys [endidx].residualoutcount == 0) { continue; }

					unsigned int start = p.journeys [startidx].start;
					unsigned int end = p.journeys [endidx].end;

					bestlength = end - start;
					startjourney = startidx;
					endjourney = endidx;
					break;
				}
			}

			if (bestlength == 0xFFFFFFFF) { break; } // Done.

			unsigned long long deltacost = dist_cost (p, p.journeys [endjourney].end - p.journeys [startjourney].start) % 1000002013;
			unsigned int passengercount = p.journeys [endjourney].residualoutcount < p.journeys [startjourney].residualincount ? p.journeys [endjourney].residualoutcount : p.journeys [startjourney].residualincount;
			
			p.journeys [startjourney].residualincount -= passengercount;
			p.journeys [endjourney].residualoutcount -= passengercount;

			// std::cout << passengercount << " in at " << p.journeys [startjourney].start << " out at " << p.journeys [endjourney].end << std::endl;

			deltacost *= passengercount;
			deltacost %= 1000002013;

			mincost += (unsigned int) deltacost;
			mincost %= 1000002013;
		}

		int loss = referencecost - mincost;
		while (loss < 0)
		{
			loss += 1000002013;
		}
		loss %= 1000002013;

		out << "Case #" << (i + 1) << ": " << loss;
		out << std::endl;
	}

	return 0;
}

