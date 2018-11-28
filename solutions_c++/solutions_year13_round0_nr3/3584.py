#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>

#include <set>
#include <map>
#include <list>
#include <queue>
#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i,a,b) for (int i = (int)a; i <= (int)b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef unsigned long long ll;

#define pb push_back
#define mp make_pair

int T;
ll A, B;

bool isFair(ll x)
{
	char str[200], rev[200];
	sprintf(str, "%d", x);
	int len = strlen(str);
	strcpy(rev, str);
	strrev(rev);
	return strcmp(str, rev) == 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	REP(tc, T)
	{
		int count = 0;
		ll min = 1, max = 1;
		cin >> A >> B;
		long double sA = sqrt(A);
		if (sA - static_cast<ll>(sA) <= numeric_limits<double>::epsilon())
		{
			min = static_cast<ll>(sA);
		}
		else 
		{
			min = static_cast<ll>(ceil(sA));
		}
		long double sB = sqrt(B);
		if (sB - static_cast<ll>(sB) <= numeric_limits<double>::epsilon())
		{
			max = static_cast<ll>(sB);
		}
		else 
		{
			max = static_cast<ll>(floor(sB));
		}
		for (ll i = min; i <= max; i++)
		{
			if (isFair(i) && isFair(i*i)) count++;
		}
		printf("Case #%d: %d\n", tc+1, count);
	}
}