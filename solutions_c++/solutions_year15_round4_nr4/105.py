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
map< vector< VI >, int > dp[10];
vector< VI > vec[10];

bool check( VI A, VI B, VI C )
{
	ass( SZ(A) == SZ(B) );
	ass( SZ(B) == SZ(C) );

	FA(a,B)
	{
		int cnt = 0;
		if (A[a]==B[a]) cnt++;
		if (C[a]==B[a]) cnt++;
		if (B[(a+1)%SZ(B)]==B[a]) cnt++;
		if (B[(a-1+SZ(B))%SZ(B)]==B[a]) cnt++;
		if (cnt != B[a]) return false;
	}

	return true;
}

bool minimal( vector< VI > vec )
{
	vector< VI > ans = vec, tmp = vec;
	FOR(a,0,m)
	{
		FA(b,tmp)
		{
			int tt = tmp[b][0];
			FA(c,tmp[b]) if (c>0) tmp[b][c-1] = tmp[b][c];
			tmp[b][SZ(tmp[b])-1] = tt;
		}
		if (tmp < ans) ans = tmp;
	}

	return vec==ans;
}

void init()
{
	vec[0].push_back( VI() );
	FOR(a,0,5) FA(b,vec[a])
	{
		VI tmp = vec[a][b];
		FOR(c,1,3)
		{
			tmp.push_back( c );
			vec[a+1].push_back( tmp );
			tmp.pop_back();
		}
	}
}

void sol()
{
	FOR(a,0,9) dp[a].clear();
	FA(a,vec[m])
	{
		vector< VI > vv;
		vv.push_back( VI(m,0) );
		vv.push_back( VI(vec[m][a]) );
		dp[0][ vv ] = 1;
	}

	int ans = 0;
	FOR(a,0,n-1)
		for (map< vector< VI >, int >::iterator it = dp[a].begin(); it != dp[a].end(); it++)
			if (minimal( it->first ))
			{
				VI p1 = it->first[SZ(it->first)-2];
				VI p2 = it->first[SZ(it->first)-1];
				if (a==n-1)
				{
					if (check(p1, p2, VI(m,0)))
					{
						ans += dp[a][it->first];
						if (ans >= o_O+7) ans -= o_O+7;
					}
				}
				else
				{
					FA(b,vec[m])
						if (check(p1, p2, vec[m][b]))
						{
							vector< VI > pp = it->first;
							pp.push_back( vec[m][b] );
							dp[a+1][pp] += dp[a][it->first];
							if (dp[a+1][pp]>=o_O+7) dp[a+1][pp]-=o_O+7;
						}
				}
			}
	
	cout << ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	init();

	int t=0;
	cin >> t;
	FOR(a,1,t)
	{
		cerr << a << "\n";

		cin >> n >> m;

		cout << "Case #" << a << ": ";

		sol();

		cout << "\n";
	}

	cerr << clock() << "\n";
	return 0;
}
