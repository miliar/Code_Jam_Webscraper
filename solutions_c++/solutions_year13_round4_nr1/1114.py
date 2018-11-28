// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

struct Passengers
{
	int o, p;
};

struct Event
{
	int s, p, t;
};

bool cmp(const Event &l, const Event &r)
{
	if (l.s != r.s)
		return l.s < r.s;

	return l.t < r.t;
}

long long S(long long n)
{
	return n*(n + 1)/2;
}



int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in("A-small-attempt1.in");
	//std::ifstream in("A.in");

	int T;
	in >> T;

	

	for (int testNumber = 1; testNumber <= T; ++testNumber)
	{
		long long N, M;
		in >> N >> M;

		int w1 = 0, w2 = 0;

		//std::cout << N << " " << M << "\n";

		std::vector<Event> events;
		long long q = 0;
		for (int i = 0; i < M; ++i)
		{
			long long o, e, c;
			in >> o >> e >> c;

			//std::cout << o << " " << e << " " << c << "\n";

			q += (S(N) - S(N - (e - o)))*c;

			Event e1;
			e1.s = o;
			e1.p = c;
			e1.t = 0;
			events.push_back(e1);

			e1.s = e;
			e1.p = c;
			e1.t = 1;
			events.push_back(e1);
		}

		//std::cout << q << "\n";
		std::sort(events.begin(), events.end(), cmp);


		long long r = 0;
		std::vector<Passengers> currP;
		for (int curr = 0; curr < events.size(); ++curr)
		{
			if (0 == events[curr].t)
			{
				Passengers p;
				p.p = events[curr].p;
				p.o = events[curr].s;

				w1 += events[curr].p;

				currP.push_back(p);
			}
			else
			{
				long long n = events[curr].p;
				for (int p = currP.size() - 1; p >= 0 && n > 0; --p)
				{
					if (n >= currP[p].p)
					{
						long long d = (events[curr].s - currP[p].o);

						r += currP[p].p*(S(N) - S(N - d));
						n -=currP[p].p;
						w2 += currP[p].p;
						currP.pop_back();
					}
					else
					{
						long long d = (events[curr].s - currP[p].o);
						r += n*(S(N) - S(N - d));
						w2 += n;
						currP.back().p -= n;
						n = 0;
					}
				}
			}
		}

		//std::cout << w1 << " " << w2 << "\n";



		std::cout << "Case #" << testNumber << ": " << (q - r) % 1000002013 << "\n";

	}

	return 0;
}

