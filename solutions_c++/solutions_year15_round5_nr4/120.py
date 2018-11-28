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

int P;
int S[10010], C[10010];

void sol()
{
	map< LL, LL > Set;
	map< LL, LL > Subset;
	vector< LL > ans;

	FOR(a,1,P) Set[S[a]] = C[a];
	Subset[0] = 1;
	Set[0]--;
	if (Set[0]==0) Set.erase( 0 );

	while (SZ(Set))
	{
		pair< LL, LL > pp = *Set.begin();
		LL elem = pp.first;
		ans.push_back( elem );
		map< LL, LL > Subset2;

		for ( map< LL, LL >::iterator it = Subset.begin(); it != Subset.end(); it++ )
		{
			Set[it->first + elem] -= it->second;
			if (Set[it->first + elem] == 0) Set.erase(it->first + elem);
			Subset2[it->first] += it->second;
			Subset2[it->first+elem] += it->second;
		}

		Subset = Subset2;
	}

	sort( ans.begin(), ans.end() );

	FA(a,ans) cout << " " << ans[a];
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
		cin >> P;
		FOR(a,1,P) cin >> S[a];
		FOR(a,1,P) cin >> C[a];

		cout << "Case #" << z << ":";
		sol();
		cout << "\n";
	}

	return 0;
}
