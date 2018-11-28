#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

const int maxSize = (1 << 21) + 5;

vector < int > freePos;
double ans[maxSize];
double p[maxSize];
char s[25];
int n;
int sMask, fullMask;

void moveMask (int curMask)
{
	for (int i = 0; i < n; i++)
	{
		if (curMask & (1 << i) )
			continue;

		int newMask = (curMask | (1 << i) );
		int curCost = n + 1;
		int cnt = 0;
		double sum = 0;

		for (int j = i; ; )
		{
			if ( (!(curMask & (1 << j) ) ) && j != i)
				break;

			curCost--;
			sum += curCost / (n * 1.);
			cnt++;

			j--;
			if (j == -1)
				j = n - 1;

			if (j == i)
				break;
		}

		double curAns = ans[curMask] * (cnt / (n * 1.) ) + sum * p[curMask];

		ans[newMask] += curAns;
		p[newMask] += p[curMask] * (cnt / (n * 1.) );
	}
}

void getPos (int ind, int remPos, int curMask)
{
	if (ind == freePos.size())
	{
		moveMask(curMask);

		return ;
	}

	if (freePos.size() - ind > remPos)
		getPos(ind + 1, remPos, curMask);

	if (remPos != 0)
	{
		curMask ^= (1 << freePos[ind] );
		getPos(ind + 1, remPos - 1, curMask);
		curMask ^= (1 << freePos[ind] );
	}
}

void solve ()
{
	freePos.clear();
	for (int i = 0; i < n; i++)
	{
		if (s[i] == '.')
			freePos.push_back(i);
	}

	sMask = 0; fullMask = 0;
	for (int i = 0; i < n; i++)
	{
		if (s[i] == 'X')
			sMask |= (1 << i);

		fullMask |= (1 << i);
	}

	for (int i = 0; i <= fullMask; i++)
	{
		ans[i] = 0;
		p[i] = 0;
	}

	ans[sMask] = 0;
	p[sMask] = 1;

	for (int i = 0; i < freePos.size(); i++)
	{
		getPos(0, i, sMask);
	}

	printf("%.12lf", ans[fullMask] );
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test, t;

	scanf("%d\n", &test);
	for (t = 0; t < test; t++)
	{
		if (t)
			printf("\n");

		printf("Case #%d: ", t + 1);

		// input

		gets(s);
		n = strlen(s);

		// #input

		solve();
	}

	return 0;
}