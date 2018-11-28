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

int n, p, q;
int H[110], G[110];
//int ans = 0;

map< int, int > Map;

int dfs()
{
	//FOR(a,1,deep) cout << "  ";
	//FOR(a,1,n) cout << H[a] << " ";
	//cout << g << "\n";

	int tmp = 0;
	FOR(a,1,n) tmp = tmp*211 + max(H[a],0);
	if (Map.find(tmp) != Map.end())
		return Map[tmp];

	int re = 0;
	int g = 0;

	FOR(a,1,n) if (H[a]>0)
	{
		H[a]-=p;
		if (H[a]<1) g += G[a];
		re = max( re, g );
		//ans = max( ans, g );

		FOR(b,1,n) if (H[b]>0)
		{
			H[b]-=q;

			re = max( re, dfs() + g );

			H[b]+=q;
			break;
		}

		if (H[a]<1) g -= G[a];
		H[a]+=p;
	}

	FOR(b,1,n) if (H[b]>0)
	{
		H[b]-=q;

		re = max( re, dfs() + g );

		H[b]+=q;
		break;
	}

	Map[tmp] = re;
	return re;
}

void sol()
{
	Map.clear();

	cout << dfs();
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin >> t;

	FOR(a,1,t)
	{
		cerr << a << "\n";

		cin >> p >> q >> n;

		FOR(b,1,n) cin >> H[b] >> G[b];

		cout << "Case #" << a << ": ";
		sol();
		//cout << " ";
		//sol2();
		cout << "\n";
	}
	return 0;
}
