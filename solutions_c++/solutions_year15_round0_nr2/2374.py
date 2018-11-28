
#include <cstring>
#include <cassert>
#include <cstdio>
#include <vector>
#include <set>
#include <iostream>

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))

struct PancakePile
{
	PancakePile(int n) : numOfPancakes(n),divisor(1),maxPileNum(n) {}
	int numOfPancakes;
	int divisor;
	int maxPileNum;
};

struct classcomp {
  bool operator() (const PancakePile& lhs, const PancakePile& rhs) const
  {return lhs.maxPileNum>rhs.maxPileNum;}
};
#if 0
int getTimeExtremeSlow(const std::vector<int> &plates)
{
	if (plates.empty())
	{
		return 0;
	}

	int sum = 0;
	for (unsigned int i = 0; i < plates.size(); ++i)
	{
		sum += plates[i];
	}

	if (!sum)
	{
		return 0;
	}

	// no special
	std::vector<int> noSpecial;
	for (unsigned int i = 0; i < plates.size(); ++i)
	{
		if (plates[i] > 1)
		{
			noSpecial.push_back(plates[i]-1);
		}
	}
	int min = getTimeExtremeSlow(noSpecial) +1;

	for (unsigned int i = 0; i < plates.size(); ++i)
	{
		std::vector<int> special(plates);

		if (plates[i] > 1)
		{
			int toRemove = plates[i]/2;
			special[i] -= toRemove;
			special.push_back(toRemove);

			int specialsum = 0;
			for (unsigned int i = 0; i < plates.size(); ++i)
			{
				specialsum += plates[i];
			}

			assert(sum ==specialsum);

			int m = getTimeExtremeSlow(special)+1;

			if (m < min)
			{
				min = m;
			}
		}
	}
	return min;
}


int getTimeExtremeSlow()
{
	std::vector<int> plates;
	int diners;
	std::cin >> diners;
	for (int i = 0; i < diners; ++i)
	{
		int p;
		std::cin >> p;
		plates.push_back(p);

	}

//	printf ("num of plates = %lu  plates are: ", plates.size());

	for (std::vector<int>::iterator it = plates.begin(); it != plates.end(); ++it)
	{
//		printf ("%d ", *it);
	}
//	printf ("\n");
	int min = getTimeExtremeSlow(plates);
//	printf ("min = %d\n", min);

	return min;
}

int getTimeSlow()
{
	std::multiset<int,classcomp> plates;
	int diners;
	std::cin >> diners;
	int sum = 0;
	for (int i = 0; i < diners; ++i)
	{
		int p;
		std::cin >> p;
		plates.insert(p);
		sum += p;
	}

	printf ("Sum = %d, plates =", sum);

	for (std::set<int,classcomp>::iterator it = plates.begin(); it != plates.end(); ++it)
	{
		printf ("%d ", *it);
	}
	printf ("\n");

	int min = *plates.begin();

	int divisions = 0;

	while (*plates.begin() > 1)
	{
		int p = *plates.begin();
		plates.erase(plates.begin());
		plates.insert(p/2);
		plates.insert(p-p/2);
		divisions +=1;

		if (divisions + *plates.begin() < min)
		{
			min = divisions + *plates.begin();
		}

		printf ("divisions = %d, plates =", divisions);

		for (std::set<int,classcomp>::iterator it = plates.begin(); it != plates.end(); ++it)
		{
			printf ("%d ", *it);
		}
		printf ("min = %d\n", min);

	}
	return min;
}
#endif

int getTimeSlowCorrect()
{
	std::multiset<PancakePile,classcomp> plates;
	int diners;
	std::cin >> diners;
	int sum = 0;
	for (int i = 0; i < diners; ++i)
	{
		int p;
		std::cin >> p;
		plates.insert(PancakePile(p));
		sum += p;
	}
/*
	printf ("Sum = %d, plates =", sum);

	for (std::set<PancakePile,classcomp>::iterator it = plates.begin(); it != plates.end(); ++it)
	{
		printf ("%d", it->numOfPancakes);
		if (it->divisor >1)
		{
			printf ("/%d(%d) ", it->divisor, it->maxPileNum);
		} else {
			printf (" ");
		}
	}
	printf (", min = %d\n", plates.begin()->numOfPancakes);
*/
	int min = plates.begin()->numOfPancakes;

	int divisions = 0;

	while (true)
	{
		PancakePile b = *plates.begin();
		if (b.divisor > b.maxPileNum)
		{
			break;
		}

		plates.erase(plates.begin());

		divisions += 1;
		b.divisor += 1;
		b.maxPileNum = (b.numOfPancakes+b.divisor-1)/b.divisor;   // ceiling

		plates.insert(b);

		if (divisions + plates.begin()->maxPileNum < min)
		{
			min = divisions + plates.begin()->maxPileNum;
		}
/*
		printf ("divisions = %d, plates =", divisions);
		for (std::set<PancakePile,classcomp>::iterator it = plates.begin(); it != plates.end(); ++it)
		{
			printf ("%d", it->numOfPancakes);
			if (it->divisor >1)
			{
				printf ("/%d(%d) ", it->divisor, it->maxPileNum);
			} else {
				printf (" ");
			}
		}
		printf ("min = %d\n", min);
//*/
	}
	return min;
}
#if 0
const int maxPancakeNum = 1023;
int diners [maxPancakeNum+1]; // there are diners[i] plates that have i pancakes

int getTimeQuick()
{
	memset (diners, 0, sizeof(int)*(maxPancakeNum+1));
	int d;
	std::cin >> d;
	int max = 0;
	for (int i = 0; i < d; ++i)
	{
		int p;
		std::cin >> p;
		++diners[p];
		if (p > max)
		{
			max = p;
		}
	}

	int divisions = 0;
	int min = max;

	//printf ("initially min is %d, and did %d divisions.\n", min, divisions);

	for (int i = max; i > 1; --i)
	{
		if (diners[i] > 0)
		{
			if (i+divisions < min)
			{
				min = i+divisions;
			}

			int n1 = i/2;
			int n2 = i-n1;
			//printf ("we have %d plates with %d pancakes. With %d divisions inc %d and %d\n", diners[i], i, diners[i], n1, n2);
			diners[n1] += diners[i];
			diners[n2] += diners[i];
			divisions += diners[i];
			diners[i] = 0;
		} else {
			//printf ("we have %d plates with %d pancakes. nothing to do.\n", diners[i], i);
		}
		//printf ("@i=%d the new minimum is %d (div = %d)\n",i ,min, divisions);
	}
	return min;
}
#endif

void infinite_house_of_pancakes ()
{
	int tcNum;
	std::cin >> tcNum;

	// printf ("Num of TCs = %d\n", tcNum);

	for (int tc = 0; tc < tcNum; ++tc)
	{
		// int min = getTimeQuick();
		// int min = getTimeSlow();
		// int min = getTimeExtremeSlow();
		int min = getTimeSlowCorrect();

		printf ("Case #%d: %d\n", tc+1, min);
	}
}
