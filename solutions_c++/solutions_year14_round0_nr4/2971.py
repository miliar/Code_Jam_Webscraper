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

bool used[1050];

void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		int n = ri();
		vector<double> a,b;
		fr(i,1,n)
		{
			double x;
			cin >> x;
			a.pb(x);
		}
		fr(i,1,n)
		{
			double x;
			cin >> x;
			b.pb(x);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		int win_second = 0;
		int r = n - 1,l = 0;	
		fd(i,n - 1,0)
		{
			if (b[r] > a[i])
				r--;
			else
				l++,win_second++;
		}
		int win_first = 0;
		r = n - 1;
		for(int i = n - 1,l = 0;i >= l;r--)
		{
			if (a[i] + 0.0000001 > b[r])
				win_first++,i--;
			else
				l++;
		}
		printf("Case #%d: %d %d\n",testing,win_first,win_second);
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