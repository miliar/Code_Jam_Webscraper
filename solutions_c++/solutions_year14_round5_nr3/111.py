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

int n, k;
char cmd[20];
int num[20];

bool dp[16][1<<16];

void sol()
{
	FOR(a,1,n) num[a]+=100;

	int k = 1;

	FOR(a,1,n) if (num[a]>100)
	{
		int tmp = num[a];
		FOR(b,1,n) if (num[b]==tmp) num[b] = k;
		k++;
	}

	FOR(a,1,n) if (num[a]==100)
	{
		num[a] = 0;
		k++;
	}

	CLR(dp);
	FOR(a,0,(1<<k)-1) dp[0][a] = true;

	FOR(a,1,n) FOR(b,0,(1<<k)-1) if (dp[a-1][b])
		if (num[a]>0)
		{
			if (cmd[a]=='E')
			{
				if (((b>>num[a])&1)==0)
					dp[a][b^(1<<num[a])] = true;
			}
			else if (cmd[a]=='L')
			{
				if (((b>>num[a])&1)==1)
					dp[a][b^(1<<num[a])] = true;
			}
		}
		else
		{
			if (cmd[a]=='E')
			{
				FOR(c,0,k-1)
					if (((b>>c)&1)==0)
						dp[a][b^(1<<c)] = true;
			}
			else
			{
				FOR(c,0,k-1)
					if (((b>>c)&1)==1)
						dp[a][b^(1<<c)] = true;
			}
		}

	int ans = o_O;
	FOR(a,0,(1<<k)-1) if (dp[n][a])
	{
		int tmp = 0;
		FOR(b,0,k-1) tmp += ((a>>b)&1);
		ans = min( ans, tmp );
	}

	if (ans==o_O) cout << "CRIME TIME";
	else cout << ans;
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

		cin >> n;

		char str[5];

		FOR(b,1,n)
		{
			RE("%s%d", str, &num[b]);
			cmd[b] = str[0];
		}

		cout << "Case #" << a << ": ";
		sol();
		//cout << " ";
		//sol2();
		cout << "\n";
	}
	return 0;
}
