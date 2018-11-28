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

#include <time.h>
#pragma comment(linker, "/STACK:20000000")

#define fr(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define fd(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define mp make_pair
#define pb push_back
#define ll long long

using namespace std;

int ri(){int x;scanf("%d",&x);return x;}
ll rll(){ll x;scanf("%lld",&x);return x;}
	

int mas[15][15];
int x[15][15];
bool ok[15];

void solve()
{
		
	int test = ri();
	fr(testing,1,test)
	{
		int n = ri(), m = ri();
		fr(i,0,n-1)
			fr(j,0,m-1)
				mas[i][j] = ri();
		bool ans = false;
		fr(MASK,0,(1<<n)-1)
		{
			memset(ok,false,sizeof(ok));
			fr(i,0,n-1)
			{
				int value = 2;
				if (MASK&(1<<i))
					value = 1;
				fr(j,0,m-1)
					x[i][j] = value;
			}
			fr(j,0,m-1)
			{
				bool yes = false;
				fr(i,0,n-1)
					if (mas[i][j] == 1 && x[i][j] == 2)
						yes = true;
				if (yes)
					fr(i,0,n-1)
						x[i][j] = 1;
			}
			bool res = true;
			fr(i,0,n-1)
				fr(j,0,m-1)
					if (mas[i][j] != x[i][j])
						res = false;
			if (res)
			{
				ans = true;
				break;
			}
		}
		printf("Case #%d: %s\n",testing,ans ? "YES" : "NO" );
	}

}

int main()
{
	/*#ifndef ONLINE_JUDGE
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/input.txt","rt",stdin);
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif*/

	solve();

	/*#ifndef ONLINE_JUDGE
		printf("\n\ntime-%.3lf",clock()*1e-3);
	#endif*/

	return 0;
}