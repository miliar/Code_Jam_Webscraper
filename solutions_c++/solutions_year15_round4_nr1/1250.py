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

int dx[] = {0,1,0,-1,0};
int dy[] = {1,0,-1,0,0};
string buf = ">v<^.";

void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		int n = ri(),m = ri();
		vector<string> mas(n + 1);
		fr(i,1,n)
			cin >> mas[i];
		int res = 0;
		fr(i,1,n)
		{
			for(int j = 0;j < m;j++)
			{
				int ind = 0;
				char c = mas[i][j];
				for(int k = 0;k < 5;k++)
					if (buf[k] == c)
						ind = k;
				if (ind == 4)
					continue;
				vector<bool> dir(4,false);
				for(int t = 0;t < 4;t++)
				{
					int x = dx[t] + i;
					int y = dy[t] + j;
					for(;x >= 1 && x <= n && y >= 0 && y < m;)
					{
						if (mas[x][y] != '.')
						{
							dir[t] = true;
							break;
						}
						x += dx[t];
						y += dy[t];
					}
				}
				if (dir[ind])
					continue;
				mas[i][j] = '.';
				res++;
				for(int t = 0;t < 4;t++)
					if (dir[t])
					{
						mas[i][j] = buf[t];
						break;
					}
				if (mas[i][j] == '.')
				{
					res = -1;
					goto mark;
				}
			}
		}
		mark:
		printf("Case #%d: ",testing);
		if (res == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
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