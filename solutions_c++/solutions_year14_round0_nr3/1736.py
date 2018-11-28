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

int M, R, C;
int ans[10][10];
bool F[10][10];
int cc;

void dfs( int x, int y )
{
	cc++;
	F[x][y] = true;

	bool flag = false;
	FOR(a,x-1,x+1) FOR(b,y-1,y+1) if (a||b)
		if (ans[a][b]>0)
			flag = true;
	if (!flag)
		FOR(a,x-1,x+1) FOR(b,y-1,y+1) if (a||b)
			if (ans[a][b]>=0 && !F[a][b])
				dfs(a,b);
}

void stupid()
{
	FOR(a,0,(1<<(R*C))-1)
	{
		int cnt = 0;
		FOR(b,0,R*C-1) if ((a>>b)&1) cnt++;
		if (cnt==M)
		{
			int z = a;
			FOR(b,0,R+1) FOR(c,0,C+1)
				if (b==0 || b==R+1 || c==0 || c==C+1)
					ans[b][c] = -1;
				else { ans[b][c] = z&1; z>>=1; }
			FOR(b,1,R) FOR(c,1,C) if (ans[b][c]==0)
			{
				cc = 0;
				CLR(F);
				dfs(b,c);
				if (cc==R*C-M)
				{
					FOR(d,1,R)
					{
						FOR(e,1,C)
							if (d==b && e==c) cout << "c";
							else cout << (ans[d][e]>0 ? "*" : ".");
						cout << "\n";
					}
					return;
				}
			}
		}
	}

	cout << "Impossible\n";
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
		cin >> R >> C >> M;
		cout << "Case #" << a << ":\n";
		stupid();
		//cout << "\n";
	}
	return 0;
}
