/* by Ashar Fuadi (fushar) */

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>

#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0, _n = (int)n; i < _n; i++)
#define FOR(i,a,b) for (int i = (int)a, _b = (int)b; i <= _b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define pb push_back
#define mp make_pair


vector<ll> ans;
int T;
ll A, B;
char buf[100];

bool pal(ll x)
{
	sprintf(buf, "%lld", x);
	int n = strlen(buf);
	int i = 0, j = n-1;
	while (i < j)
	{
		if (buf[i] != buf[j])
			return false;
		i++, j--;
	}
	return true;
}
int main()
{
	FOR(i, 1, 10000000)
		if (pal(i) && pal(i*i))
			ans.pb(i*i);
			
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%lld%lld", &A, &B);
		printf("Case #%d: %d\n", tc+1, upper_bound(ans.begin(), ans.end(), B) - lower_bound(ans.begin(), ans.end(), A));
	}
}
