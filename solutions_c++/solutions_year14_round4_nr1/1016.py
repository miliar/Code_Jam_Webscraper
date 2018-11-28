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


void Solve()
{
	int i, j, k, n, m, l;

	in_int2(n, m);
	multiset<int> a;
	for (i = 0; i < n; i++)
	{
		in_int1(k);
		a.insert(k);
	}

	int total = 0;
	multiset<int>::iterator it;
	while (a.size())
	{
		total++;
		int u = *a.rbegin();
		it = a.find(u);
		a.erase(it);
		if (!a.size()) break;
		if (*a.begin() > m - u) continue;
		if (*a.rbegin() < m - u)
		{
			a.erase(a.find(*a.rbegin()));
			continue;
		}
		it = a.lower_bound(m - u);
		if (it != a.end())
		{
			if (*it > m - u) it--;
			a.erase(it);
		}
	}

	printf(" %d", total);
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