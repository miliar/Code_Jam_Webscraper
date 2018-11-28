#pragma warning(disable:4996)

#include <conio.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

void getFactor(double n, map<double, int> &testmap)
{
	double lim, i;
	lim = sqrt(n);
	for (i = 2; i <= n; i++)
	{
		if (fmod(n, i) == 0)
		{
			testmap[i]++;
			n = n / i;
			i = 1;
		}
	}

}
void printMap(map<double, int> &Q)
{
	map<double, int>::iterator it;
	for (it = Q.begin(); it != Q.end(); it++)
	{
		printf("%.0lf : %d\n ", it->first, it->second);
	}
}
void removeZero(map<double, int> &Q)
{
	auto it = Q.begin();
	for (; it != Q.end();)
	{
		if (it->second == 0)
			it = Q.erase(it);
		else
			++it;
	}
}


int main(int argc, const char *argv[])
{
	int test_case_totalnum, now_case_num = 0;
	FILE *hFile;
	int i;
	unsigned int n, lim;
	int N, num_of_string;

	bool isFeglaWon = false;

	hFile = fopen(argv[1], "r");
	fscanf(hFile, "%d", &test_case_totalnum);

	while (now_case_num++ < test_case_totalnum)
	{
		double p, q;
		map<double, int> P, Q;

		printf("Case #%d: ", now_case_num);

		fscanf(hFile, "%lf/%lf", &p, &q);

		getFactor(p, P);
		getFactor(q, Q);

		map<double, int>::iterator it;
		map<double, int>::iterator it_select;
		for (it = Q.begin(); it != Q.end(); it++)
		{
			if ((it_select = P.find(it->first)) != P.end())
			{
				int diff = min(it_select->second, it->second);
				it->second -= diff;
				it_select->second -= diff;
				for (i = 0; i < diff; i++)
				{
					p /= it->first;
					q /= it->first;
				}
			}
		}
		removeZero(P);
		removeZero(Q);
//		printMap(Q);
		if (Q.begin()->first != 2 || Q.size() > 1)
		{
			printf("impossible\n");
			continue;
		}

		double tmpd = 1;
		double elf = p / q;
		for (i = 0; i <= 40; i++)
		{
			if (elf >= tmpd)
			{
				break;
			}
			tmpd /= 2;
		}
		printf("%d\n", i);




	}

	return 0;
}