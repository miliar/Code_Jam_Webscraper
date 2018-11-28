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

int n, p;
bool inside[1050], outside[1050];

void sol()
{
	CLR(inside);
	CLR(outside);

	FOR(a,0,(1<<n)-1)
	{
		//cout << a << ": ";
		int ones=0;
		FOR(b,0,n-1) if ((a>>b)&1) ones++;
		int m1 = (1<<ones)-1;
		int m2 = (1<<(n-ones))-1;
		FOR(b,0,(1<<n)-1) if ( m1 <= b && m2 <= (1<<n)-b-1 )
		{
			if (a<p) inside[b] = true;
			else outside[b] = true;
			//cout << b << " ";
		}
		//cout << "\n";
	}

	int ans1=-1, ans2=-1;
	DFOR(a,(1<<n)-1,0) if (inside[a] && !outside[a]) { ans1 = a; break; }
	DFOR(a,(1<<n)-1,0) if (inside[a]) { ans2 = a; break; }

	cout << ans1 << " " << ans2;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	//n=4;
	//sol();

	//return 0;

	int t;
	RE("%d", &t);

	FOR(zz,1,t)
	{
		cin >> n >> p;

		cout << "Case #" << zz << ": ";
		sol();
		cout << "\n";
	}

	return 0;
}
