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



void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		int n = ri();
		vector<int> mas;
		fr(i,1,n)
			mas.pb(ri());
		vector<int> temp;
		temp = mas;
		sort(temp.begin(),temp.end());
		int mx = temp[n - 1];
		int res = 2e9;
		do
		{
			bool check = true;
			int m = 0;
			fr(i,0,n - 1)
				if (temp[i] == mx)
				{
					m = i;
					break;
				}
			fr(i,1,m)
				if (temp[i] < temp[i - 1])
					check = false;
			fr(i,m,n - 2)
				if (temp[i] < temp[i + 1])
					check = false;
			if (check)
			{
				int step = 0;
				vector<int> a = mas;
				fr(i,0,n - 1)
				{
					if (a[i] != temp[i])
					{
						int pos;
						fr(j,0,a.size() - 1)
							if (a[j] == temp[i])
								pos = j;
						for(;pos > i;pos--)
							step++,swap(a[pos],a[pos - 1]);
					}
				}
				res = min(res,step);
			}
		}while(next_permutation(temp.begin(),temp.end()));
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