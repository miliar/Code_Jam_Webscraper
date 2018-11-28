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

int n;
char T[30][30];
int px[30], py[30];
int p[10];
bool F[30];

bool dfs( int i )
{
	if (i==n) return true;
	bool flag = false;
	FOR(a,0,n-1) if (T[p[i]][a]=='1' && !F[a])
	{
		flag = true;
		F[a] = true;
		if (!dfs(i+1)) return false;
		F[a] = false;
	}
	if (!flag) return false;
	return true;
}

bool check()
{
	FOR(a,0,n-1) p[a] = a;
	do
	{
		CLR(F);
		if (!dfs(0)) return false;
	}
	while (next_permutation( p, p+n ));
	return true;
}

int sol()
{
	int i = 0;
	FOR(a,0,n-1) FOR(b,0,n-1) if (T[a][b]=='0')
	{
		px[i] = a;
		py[i] = b;
		i++;
	}

	int ans = o_O;
	FOR(a,0,(1<<i)-1)
	{
		FOR(b,0,i-1) if ((a>>b)&1) T[px[b]][py[b]] = '1';
		if (check())
		{
			int ones = 0;
			FOR(b,0,i-1) if ((a>>b)&1) ones++;
			ans = min( ans, ones );
		}
		FOR(b,0,i-1) if ((a>>b)&1) T[px[b]][py[b]] = '0';
	}

	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	cin >> tt;
	FOR(a,1,tt)
	{
		cerr << a << "\n";
		cout << "Case #" << a << ": ";
		cin >> n;
		FOR(b,0,n-1) RE("%s", &T[b][0]);
		cout << sol();
		cout << "\n";
	}
	return 0;
}
