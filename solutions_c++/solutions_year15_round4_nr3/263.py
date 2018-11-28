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
string sent[30];
vector< int > words[30];

bool engF[50000], freF[50000];

int str_to_LL( string str )
{
	int re = 0;
	FA(a,str) re = re*30 + str[a]-'a'+1;
	return re;
}

vector< int > parse( string str )
{
	vector< int > re;
	string tmp;
	FA(a,str)
		if (str[a]==' ')
		{
			if (tmp!="") re.push_back( str_to_LL( tmp ) );
			tmp = "";
		}
		else tmp.push_back( str[a] );
	if (tmp!="") re.push_back( str_to_LL( tmp ) );

	return re;
}

void sol()
{
	int mx = 0;
	FOR(a,1,n)
	{
		words[a] = parse( sent[a] );
		FA(b,words[a]) mx = max( mx, words[a][b] );
	}

	if (mx < 50000)
	{
		int ans = o_O;
		CLR( engF );
		CLR( freF );
		FA(c,words[1]) engF[ words[1][c] ] = true;
		FA(c,words[2]) freF[ words[2][c] ] = true;
		int C0 = 0;
		FOR(a,0,mx) if (engF[a] && freF[a]) C0++;
		FOR(a,0,(1<<(n-2))-1)
		{
			set< int > eng2, fre2;
			FOR(b,3,n)
				if (((a>>(b-3))&1)==0)
				{
					FA(c,words[b])
						//if (eng.find(words[b][c]) == eng.end())
							eng2.insert( words[b][c] );
				}
				else
				{
					FA(c,words[b])
						//if (fre.find(words[b][c]) == fre.end())
							fre2.insert( words[b][c] );
				}
			int tmp = C0;
			for (set< int >::iterator it = eng2.begin(); it != eng2.end(); it++)
				if (!engF[ *it ] && freF[ *it ])
				{
					tmp++;
					if (tmp > ans) break;
				}
			if (tmp > ans) continue;
			for (set< int >::iterator it = fre2.begin(); it != fre2.end(); it++)
				if (!freF[ *it ] && engF[ *it ])
				{
					tmp++;
					if (tmp > ans) break;
				}
			if (tmp > ans) continue;
			for (set< int >::iterator it = eng2.begin(); it != eng2.end(); it++)
				if (!engF[ *it ] && !freF[ *it ])
					if (fre2.find( *it ) != fre2.end())
					{
						tmp++;
						if (tmp > ans) break;
					}
			ans = min( ans, tmp );
		}

		cout << ans;
		return;
	}

	int ans = o_O;
	set< int > eng, fre;
	FA(c,words[1]) eng.insert( words[1][c] );
	FA(c,words[2]) fre.insert( words[2][c] );
	int C0 = 0;
	for (set< int >::iterator it = eng.begin(); it != eng.end(); it++)
		if (fre.find( *it ) != fre.end())
			C0++;
	FOR(a,0,(1<<(n-2))-1)
	{
		set< int > eng2, fre2;
		FOR(b,3,n)
			if (((a>>(b-3))&1)==0)
			{
				FA(c,words[b])
					//if (eng.find(words[b][c]) == eng.end())
						eng2.insert( words[b][c] );
			}
			else
			{
				FA(c,words[b])
					//if (fre.find(words[b][c]) == fre.end())
						fre2.insert( words[b][c] );
			}
		int tmp = C0;
		for (set< int >::iterator it = eng2.begin(); it != eng2.end(); it++)
			if (eng.find( *it ) == eng.end() && fre.find( *it ) != fre.end())
			{
				tmp++;
				if (tmp > ans) break;
			}
		if (tmp > ans) continue;
		for (set< int >::iterator it = fre2.begin(); it != fre2.end(); it++)
			if (fre.find( *it ) == fre.end() && eng.find( *it ) != eng.end())
			{
				tmp++;
				if (tmp > ans) break;
			}
		if (tmp > ans) continue;
		for (set< int >::iterator it = eng2.begin(); it != eng2.end(); it++)
			if (eng.find( *it ) == eng.end() && fre.find( *it ) == fre.end())
				if (fre2.find( *it ) != fre2.end())
				{
					tmp++;
					if (tmp > ans) break;
				}
		ans = min( ans, tmp );
	}

	cout << ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t=0;
	cin >> t;
	FOR(a,1,t)
	{
		cerr << a << "\n";
		
		cin >> n;
		FOR(b,0,n) getline( cin, sent[b] );

		cout << "Case #" << a << ": ";

		sol();

		cout << "\n";
	}

	cerr << clock() << "\n";
	return 0;
}
