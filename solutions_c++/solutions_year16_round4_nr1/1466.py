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

int n, R, P, S;

bool check( string s )
{
	while (SZ(s)>1)
	{
		string s2;
		for (int i=0; i<SZ(s); i+=2)
		{
			if (s[i]==s[i+1]) return false;
			if (s[i]=='R' && s[i+1]=='P') s2.push_back( 'P' );
			if (s[i]=='R' && s[i+1]=='S') s2.push_back( 'R' );
			if (s[i]=='P' && s[i+1]=='S') s2.push_back( 'S' );
			if (s[i]=='P' && s[i+1]=='R') s2.push_back( 'P' );
			if (s[i]=='S' && s[i+1]=='R') s2.push_back( 'R' );
			if (s[i]=='S' && s[i+1]=='P') s2.push_back( 'S' );
		}
		s = s2;
	}
	return true;
}

void sol()
{
	string str;
	FOR(a,1,P) str.push_back( 'P' );
	FOR(a,1,R) str.push_back( 'R' );
	FOR(a,1,S) str.push_back( 'S' );
	do
	{
		if (check( str ))
		{
			cout << str << "\n";
			return;
		}
	}
	while( next_permutation( str.begin(), str.end() ) );
	cout << "IMPOSSIBLE\n";
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	FOR(a,1,T)
	{
		cout << "Case #" << a << ": ";
		cin >> n >> R >> P >> S;
		sol();
	}
	return 0;
}
