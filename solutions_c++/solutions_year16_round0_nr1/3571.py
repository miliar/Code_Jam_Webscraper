#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>
#include <memory.h>

#include <time.h>
#pragma comment(linker, "/STACK:100000000")
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(x) (int)(x).size()
#define ll long long
#define fr(i,a,b) for(int i = (a);i <= (b);i++)
#define fd(i,a,b) for(int i = (a);i >= (b);i--)

int ri(){int x;scanf("%d",&x);return x;}

int getMask(ll n)
{
	int mask = 0;
	if (n == 0)
		return 1;
	while(n)
	{
		mask |= (1 << (n % 10));
		n /= 10;
	}
	return mask;
}

void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		ll n = ri();
		int mask = 0;
		int endMask = (1 << 10) - 1;
		ll res = n;
		for(int iter = 0;iter <= 10000 && mask != endMask;iter++)
		{
			res = (ll)(iter + 1) * n;
			mask |= getMask(res);
		}
		if (mask != endMask)
		{
			printf("Case #%d: INSOMNIA\n",testing);
			continue;
		}
		printf("Case #%d: %lld\n",testing, res);
	}
}

int main()
{
    #ifndef ONLINE_JUDGE
			freopen("C:/Users/WhiteDevil/Desktop/input.txt","rt",stdin);
			freopen("C:/Users/WhiteDevil/Desktop/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif
	
	solve();

    return 0;
}