#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> vi;
typedef vector<string> vs;
const int INF = 0x7fffffff;

int Solution()
{
	lint n, p;
	cin >> n >> p;
	lint maxx = 1;
	for(int i = 0; i < n; ++i)
		maxx *= (lint)2;
	if(maxx == p)
	{
		lint x = maxx - 1;
		cout << x << ' ' << x;
		return 0;
	}

	lint ser = maxx / 2;
	lint ans1 = 0;
	while(ser < p)
	{
		ans1 = ans1 * 2 + 1;
		ser += (maxx - ser) / 2;
	}

	lint ans2 = 2;
	ser = maxx / 2;
	while(ser > p)
	{
		ans2 *= 2;
		ser /= 2;
	}

	cout << ans1 * 2 << ' ' << maxx - ans2;
	return 0;
}

#define debug 1

int main()
{
#ifdef debug
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int n;
	cin >> n;
	getchar();
	for(int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		Solution();
		printf("\n");
	}
	return 0;
}
