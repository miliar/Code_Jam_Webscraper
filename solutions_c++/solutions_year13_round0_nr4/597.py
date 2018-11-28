#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000

void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

bool was[1<<20];
int k, n;
map< int, int > Map;
int need_to_open[30];
VI inside[30];
int order[30], sz=0;

bool sol( int mask=0 )
{
	if (sz==n) return true;

	was[mask] = true;

	FOR(a,0,n-1) if (!((mask>>a)&1))
		if (!was[ mask | (1<<a) ])
			if (Map[need_to_open[a]] > 0)
			{
				Map[need_to_open[a]]--;
				FA(b,inside[a]) Map[inside[a][b]]++;
				order[sz++] = a+1;

				if (sol( mask | (1<<a) )) return true;

				sz--;
				FA(b,inside[a]) Map[inside[a][b]]--;
				Map[need_to_open[a]]++;
			}

	return false;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T, cur_t=0;
	RE("%d", &T);
	FOR(z,1,T)
	{
		cur_t++;
		RE("%d%d", &k, &n);
		Map.clear();
		CLR(was);
		sz=0;
		FOR(a,1,k)
		{
			int x;
			RE("%d", &x);
			Map[x]++;
		}
		FOR(a,0,n-1)
		{
			int x, y;
			RE("%d%d", &x, &y);
			need_to_open[a] = x;
			inside[a].clear();
			FOR(b,1,y)
			{
				int z;
				RE("%d", &z);
				inside[a].push_back(z);
			}
		}

		cout << "Case #" << cur_t << ":";
		if (sol())
		{
			for (int a=0; a<sz; a++)
				cout << " " << order[a];
		}
		else cout << " IMPOSSIBLE";

		cout << "\n";
	}

	return 0;
}
