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

LL mod = 1000002013;

int n, m;
LL before, after;
map< int, LL > Map;

void sol()
{
	after = 0;
	map< int, LL > M2;
	for (map< int, LL >::iterator it = Map.begin(); it != Map.end(); it++)
		if (it->SE > 0)
			M2[it->FI] += it->SE;
		else
		{
			while (it->SE < 0)
			{
				map< int, LL >::iterator it2 = M2.end();
				it2--;
				int pos = it2->FI;
				LL de = it->FI-pos;
				LL z = -it->SE;
				if (it2->SE < z) z = it2->SE;
				after += (((de*(de+1))/2 % mod) * (z%mod)) % mod;
				after %= mod;
				it->SE += z;
				it2->SE -= z;
				if (it2->SE==0) M2.erase( it2 );
			}
		}

	cout << ((after - before)%mod + mod)%mod ;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	RE("%d", &t);

	FOR(zz,1,t)
	{
		before = 0;
		Map.clear();

		RE("%d%d", &n, &m);
		FOR(a,1,m)
		{
			int x, y, z;
			RE("%d%d%d", &x, &y, &z);
			Map[x]+=z;
			Map[y]-=z;

			LL de = y-x;
			before += (((de*(de+1))/2) % mod * z) % mod;
			before %= mod;
		}

		cout << "Case #" << zz << ": ";
		sol();
		cout << "\n";
	}

	return 0;
}
