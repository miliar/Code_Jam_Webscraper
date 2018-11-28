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

string Q[1<<11];
map< string, int > dist;

void sol( string s )
{
	dist.clear();

	int z = 1;
	Q[0] = s;
	dist[s] = 0;

	FOR(a,0,z-1)
	{
		string ii = Q[a];
		FA(b,ii)
		{
			string jj = ii;
			reverse( jj.begin(), jj.begin()+b+1 );
			FOR(c,0,b) jj[c] = (jj[c]=='-' ? '+' : '-');
			if (dist.find( jj ) == dist.end())
			{
				dist[ jj ] = dist[ ii ]+1;
				Q[z++] = jj;
			}
		}
	}

	cout << dist[ string( SZ(s), '+' ) ];
}

void sol2( string s )
{
	string end = string( SZ(s), '+' );
	int ans = 0;
	while ( s != end )
	{
		int i;
		if (s[0]=='+')
		{
			FA(a,s) if (s[a+1]=='-') { i = a; break; }	
		}
		else
		{
			RFA(a,s) if (s[a]=='-') { i = a; break; }
		}
		reverse( s.begin(), s.begin()+i+1 );
		FOR(c,0,i) s[c] = (s[c]=='-' ? '+' : '-');
		ans ++;
	}

	cout << ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	FOR(z,1,T)
	{
		string s;
		cin >> s;
		cout << "Case #" << z << ": ";
		//sol( s );
		//cout << " ";
		sol2( s );
		cout << "\n";
	}

	return 0;
}
