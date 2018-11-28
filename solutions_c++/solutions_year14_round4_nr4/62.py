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

int m, n;
string S[10];

void sol()
{
	int ans = 0, cnt = 0;

	FOR(a,0,(1<<(2*m))-1)
	{
		bool flag = true;
		FOR(b,0,m-1) if (((a>>(2*b))&3)>=n) flag = false;

		int cc[5];
		CLR(cc);
		FOR(b,0,m-1) cc[(a>>(2*b))&3]++;
		FOR(b,0,n-1) if (cc[b]==0) flag = false;

		if (flag)
		{
			int tmp = 0;
			FOR(b,0,n-1)
			{
				vector< string > vec;
				FOR(c,0,m-1)
					if ( ((a>>(2*c))&3)==b )
						vec.push_back( S[c+1] );
				sort( vec.begin(), vec.end() );

				tmp++;
				FA(c,vec)
				{
					tmp += SZ(vec[c]);
					if (c)
						FA(d,vec[c])
							if (SZ(vec[c-1])==d-1 || vec[c-1][d]!=vec[c][d])
							{
								tmp -= d;
								break;
							}
				}
			}
			
			if (tmp > ans)
			{
				ans = tmp;
				cnt = 1;
			}
			else if (tmp == ans)
				cnt++;
		}
	}

	cout << ans << " " << cnt;
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

		cin >> m >> n;
		FOR(b,1,m) cin >> S[b];

		cout << "Case #" << a << ": ";
		sol();
		//cout << " ";
		//sol2();
		cout << "\n";
	}
	return 0;
}
