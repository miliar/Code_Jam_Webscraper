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

int a[10][10],b[10][10];
char mark[20];

void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		int r1 = ri();
		const int n = 4;
		memset(mark,0,sizeof(mark));
		fr(i,1,n)
			fr(j,1,n)
			{
				a[i][j] = ri();
				if (i == r1)
					mark[a[i][j]] |= 1;
			}
		int r2 = ri();
		fr(i,1,n)
			fr(j,1,n)
			{	
				b[i][j] = ri();
				if (i == r2)
					mark[b[i][j]] |= 2;
			}
		bool cheat = true;
		int bad = 0;
		int res = 0;
		fr(i,1,16)
			if (mark[i] == 3)
			{
				cheat = false;
				bad++;
				res = i;
			}
		if (bad > 1)
			printf("Case #%d: Bad magician!\n",testing);
		else
		if (bad == 0)
			printf("Case #%d: Volunteer cheated!\n",testing);
		else
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