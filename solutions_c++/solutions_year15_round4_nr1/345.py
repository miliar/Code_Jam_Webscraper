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
char T[1000][1000];

bool can_get( int x, int y, int dx, int dy )
{
	while(1)
	{
		x += dx;
		y += dy;
		if (x<1 || x>n || y<1 || y>m) return false;
		if (T[x][y]!='.') return true;
	}
	return false;
}

void sol()
{
	int ans = 0;
	FOR(a,1,n) FOR(b,1,m) if (T[a][b]!='.')
	{
		int dx = 0, dy = 0;
		if (T[a][b]=='>') dy=1;
		else if (T[a][b]=='<') dy=-1;
		else if (T[a][b]=='v') dx=1;
		else dx=-1;

		if (!can_get( a, b, dx, dy ))
		{
			if (!can_get( a, b, 1, 0 ) && !can_get( a, b, -1, 0 ) && !can_get( a, b, 0, 1 ) && !can_get( a, b, 0, -1 ))
			{
				cout << "IMPOSSIBLE";
				return;
			}
			ans++;
		}
	}

	cout << ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t=0;
	cin >> t;
	FOR(a,1,t)
	{
		cerr << a << "\n";
		
		RE("%d%d\n", &n, &m);
		FOR(z,1,n) gets( &T[z][1] );

		cout << "Case #" << a << ": ";

		sol();

		cout << "\n";
	}

	cerr << clock() << "\n";
	return 0;
}
