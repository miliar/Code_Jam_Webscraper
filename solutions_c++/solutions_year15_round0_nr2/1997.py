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
#pragma comment(linker, "/STACK:20000000")

#define fr(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define fd(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define mp make_pair
#define pb push_back
#define ll long long

using namespace std;

int ri(){int x;scanf("%d",&x);return x;}
ll rll(){ll x;scanf("%lld",&x);return x;}



void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		int n = ri();
		int res = 1050;
		vector<int> mas;
		for(int i = 0;i < n;i++	)
			mas.pb(ri());
		sort(mas.begin(),mas.end());
		vector<int> temp;
		int res2 = 1050;
		for(int d = 1;d <= mas.back();d++)
		{
			//temp = mas;
			int cnt = 0;
		/*	while(temp.back() > d)
			{
				int x = temp.back();
				temp.pop_back();
				temp.pb(d);
				temp.pb(x - d);
				sort(temp.begin(),temp.end());
				cnt++;
			}
			cnt += temp.back();
			res = min(res,cnt);*/
			cnt = 0;
			for(int j = 0;j < mas.size();j++)
				cnt += (mas[j] + d - 1) / d - 1; 
			cnt += d;
			res2 = min(res2,cnt);
		}
		//if (res != res2)
		//	cout << "EO" << endl;
		printf("Case #%d: %d\n",testing,res2);
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