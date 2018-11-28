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

bool used[10500];

void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		int n = ri(),x = ri();
		vector<int> mas;
		fr(i,1,n)
			mas.pb(ri());
		sort(mas.begin(),mas.end());
		memset(used,0,sizeof(used));
		int res = 0;
		fd(i,n - 1,0)
		{
			if (used[i])
				continue;
			used[i] = true;
			fd(j,i - 1,0)
				if (!used[j] && mas[i] + mas[j] <= x)
				{
					used[j] = true;
					break;
				}
			res++;
		}
		printf("Case #%d: %d\n",testing,res);
	}

}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/input.txt","rt",stdin);
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif

	solve();

	#ifndef ONLINE_JUDGE
		printf("\n\ntime-%.3lf",clock()*1e-3);
	#endif

	return 0;
}