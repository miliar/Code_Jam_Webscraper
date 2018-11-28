#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define in_str(b) scanf("%s",(b))
#define in_int1(a) scanf("%d",&(a))
#define in_int2(a,b) scanf("%d%d",&(a),&(b))
#define in_int3(a,b,c) scanf("%d%d%d",&(a),&(b),&(c))
#define in_int4(a,b,c,d) scanf("%d%d%d%d",&(a),&(b),&(c),&(d))
#define mp(a,b) make_pair(a,b)

/*
pair<int, int>	mas[1010];
int dp[1010][1010];
int n, pos;

int doit(int f, int len)
{
	if (len == n) return 0;
	int& res = dp[f][len];
	if (res == -1)
	{
		res = 1e9;
		int i = n - len - 1;
		if (i < pos)
		{

		}
	}

	return res;
}
*/

int mas[1010];

void Solve()
{
	int i, j, k, m, n, l;

	in_int1(n);
	map<int, int> pos;
	for (i = 0; i < n; i++)
	{
		int a;
		in_int1(a);
		pos[a] = i;
		mas[i] = a;
	}

	int best = 0;
	map<int, int>::iterator it = pos.begin();
	int left = 0;
	int right = n - 1;
	for (i = 0; i < n - 1; i++, it++)
	{
		if (it->second - left < right - it->second)
		{
			for (j = it->second - 1; j >= left; j--)
			{
				pos[mas[j]]++;
				mas[j + 1] = mas[j];
				best++;
			}
			mas[j + 1] = it->first;
			left++;
		}
		else
		{
			for (j = it->second + 1; j <= right; j++)
			{
				pos[mas[j]]--;
				mas[j - 1] = mas[j];
				best++;
			}
			mas[j - 1] = it->first;
			right--;
		}
	}

	printf(" %d", best);
}

int main(int argc, char**argv)
{
	if (argc > 1) freopen(argv[1], "rt", stdin);
	else freopen("input.txt", "rt", stdin);

	freopen("output.txt", "wt", stdout);
	int test;

	in_int1(test);
	for (int step = 1; step <= test; step++)
	{
		printf("Case #%d:", step);
		Solve();
		printf("\n");
	}
	return 0;
}