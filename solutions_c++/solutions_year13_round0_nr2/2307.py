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

int n, m;
int p[110][110];
bool hor[110], ver[110];

bool sol()
{
	while(1)
	{
		bool has_one = false;
		int global_min = o_O;
		FOR(a,1,n) FOR(b,1,m) if (!hor[a] && !ver[b])
		{
			has_one = true;
			global_min = min(global_min, p[a][b]);
		}
		if (!has_one) return true;

		int min_h=o_O, ind_h=-1;
		FOR(a,1,n) if (!hor[a])
		{
			set< int > Set;
			FOR(b,1,m) if (!ver[b]) Set.insert( p[a][b] );
			if (SZ(Set)==1)
				if (*Set.begin() < min_h)
				{
					min_h = *Set.begin();
					ind_h = a;
				}
		}

		int min_v=o_O, ind_v=-1;
		FOR(b,1,m) if (!ver[b])
		{
			set< int > Set;
			FOR(a,1,n) if (!hor[a]) Set.insert( p[a][b] );
			if (SZ(Set)==1)
				if (*Set.begin() < min_v)
				{
					min_v = *Set.begin();
					ind_v = b;
				}
		}

		//if (ind_v==-1 && ind_h==-1) return false;

		if (min_h == global_min) hor[ind_h] = true;
		else if (min_v == global_min) ver[ind_v] = true;
		else return false;
	}
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
		
		CLR(hor);
		CLR(ver);

		cin >> n >> m;
		FOR(a,1,n) FOR(b,1,m) cin >> p[a][b];

		cout << "Case #" << cur_t << ": ";
		if (sol()) cout << "YES";
		else cout << "NO";
		cout << "\n";
	}

	return 0;
}
