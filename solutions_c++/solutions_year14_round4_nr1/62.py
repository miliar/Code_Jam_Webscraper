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

int n, X, p[10110], q[10110];

void sol()
{
	int ans = 100500;
	FOR(a,1,n) q[a] = a;

	while(1)
	{
		int tmp = 0, i = 1;
		while (i<=n)
		{
			if (i<n && p[q[i]]+p[q[i+1]]<=X) i+=2;
			else i++;
			tmp++;
		}
		ans = min( ans, tmp );

		if (!next_permutation( q+1, q+n+1 )) break;
	}

	cout << ans;
}

void sol2()
{
	sort( p+1, p+n+1 );

	int ans=0, i=1, j=n;

	while (i<=j)
	{
		if (i==j)
		{
			ans++;
			i++;
			j--;
		}
		else if (p[i]+p[j] <= X)
		{
			ans++;
			i++;
			j--;
		}
		else
		{
			ans++;
			j--;
		}
	}

	cout << ans;
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

		cin >> n >> X;
		FOR(b,1,n) cin >> p[b];

		cout << "Case #" << a << ": ";
		//sol();
		//cout << " ";
		sol2();
		cout << "\n";
	}
	return 0;
}
