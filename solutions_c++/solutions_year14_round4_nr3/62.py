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

int W, H, n;
int M[1010][1010];
int X0[1010], Y0[1010], X1[1010], Y1[1010];
int D[1010];
bool F[1010];

void sol()
{
	M[0][n+1] = M[n+1][0] = W;
	FOR(a,1,n)
	{
		M[0][a] = M[a][0] = X0[a];
		M[a][n+1] = M[n+1][a] = W-X1[a]-1;
		FOR(b,1,n)
		{
			int tmp = 0;
			if (X1[a] < X0[b]) tmp = max( tmp, X0[b]-X1[a]-1 );
			if (X1[b] < X0[a]) tmp = max( tmp, X0[a]-X1[b]-1 );
			if (Y1[a] < Y0[b]) tmp = max( tmp, Y0[b]-Y1[a]-1 );
			if (Y1[b] < Y0[a]) tmp = max( tmp, Y0[a]-Y1[b]-1 );
			M[a][b] = M[b][a] = tmp;
		}
	}

	/*FOR(a,0,n+1)
	{
		FOR(b,0,n+1) cout << M[a][b] << " ";
		cout << "\n";
	}*/

	FOR(a,0,n+1) D[a] = o_O;
	D[0] = 0;

	CLR(F);

	// dijkstra!
	while(1)
	{
		int i=-1;
		FOR(a,0,n+1) if (!F[a]) if (i==-1 || D[a] < D[i]) i = a;
		if (i==-1) break;

		F[i] = true;
		FOR(a,0,n+1) if (!F[a]) D[a] = min( D[a], D[i] + M[i][a] );
	}

	cout << D[n+1];
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

		cin >> W >> H >> n;
		FOR(b,1,n) cin >> X0[b] >> Y0[b] >> X1[b] >> Y1[b];

		cout << "Case #" << a << ": ";
		sol();
		//cout << " ";
		//sol2();
		cout << "\n";
	}
	return 0;
}
