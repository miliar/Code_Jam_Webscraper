#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
//#include <multiset>
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

int n, D;
int As, Cs, Rs;
int Am, Cm, Rm;
int M[1000100], S[1000100];
int par[1000100];
int mi[1000100], ma[1000100];
PAR pp[1000100];

void sol()
{
	par[0] = -1;
	FOR(a,1,n-1)
	{
		M[a] = ((LL)M[a-1]*Am + Cm) % Rm;
		par[a] = M[a]%a;
		S[a] = ((LL)S[a-1]*As + Cs) % Rs;
	}

	mi[0] = S[0];
	ma[0] = S[0];
	pp[0] = make_pair( S[0], S[0] );
	FOR(a,1,n-1)
	{
		mi[a] = min( mi[par[a]], S[a] );
		ma[a] = max( ma[par[a]], S[a] );
		pp[a] = make_pair( ma[a], mi[a] );
	}

	//FOR(a,0,n-1) cout << par[a] << " " << S[a] << " " << mi[a] << " " << ma[a] << "\n";

	int ans = 0;
	multiset< PAR > Set;
	int ii = 0;
	sort( pp, pp+n );
	//FOR(a,0,n-1)
	//	if (S[0]-D-1 <= mi[a] && ma[a] <= S[0]-1)
	//		Set.insert( make_pair( mi[a], ma[a] ) );
	FOR(a,S[0]-D,S[0])
	{
		//int tmp = 0;
		//FOR(b,0,n-1) if (a<=mi[b] && ma[b]<=a+D) tmp++;

		while (SZ(Set)>0)
		{
			PAR p = *Set.begin();
			if (p.first < a) Set.erase( p );
			else break;
		}
		while (1)
		{
			if (ii==n || pp[ii].first > a+D) break;
			if (a<=pp[ii].second && pp[ii].first<=a+D) Set.insert( make_pair( pp[ii].second, pp[ii].first ) );
			ii++;
		}
		//ass( tmp == SZ(Set) );
		
		ans = max( ans, SZ(Set) );
	}

	cout << ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin >> t;
	FOR(z,1,t)
	{
		cerr << z << "\n";
		cin >> n >> D;
		cin >> S[0] >> As >> Cs >> Rs;
		cin >> M[0] >> Am >> Cm >> Rm;

		cout << "Case #" << z << ": ";
		sol();
		cout << "\n";
	}

	return 0;
}
