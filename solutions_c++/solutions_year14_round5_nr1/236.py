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

LL n, p, q, r, s;
LL A[1000100];
LL S[1000100];

void sol()
{
	FOR(a,1,n) S[a] = S[a-1]+A[a];

	double ans = 0.;

	FOR(a,1,n) FOR(b,a,n)
	{
		LL s1 = S[a-1];
		LL s2 = S[b]-S[a-1];
		LL s3 = S[n]-S[b];

		LL ss = s1;
		if (ss < s2) ss = s2;
		if (ss < s3) ss = s3;

		ans = max( ans, (double)(S[n]-ss)/S[n] );
	}

	WR("%.10lf", ans);
}

void sol2()
{
	FOR(a,1,n) S[a] = S[a-1]+A[a];

	double ans = 0.;

	int ii=1, jj=n;
	FOR(a,1,n) if (S[a]*3>=S[n]) { ii = a; break; }
	FOR(a,1,n) if (S[a]*3>=S[n]*2) { jj = a; break; }

	FOR(i,ii-1000,ii+1000) FOR(j,jj-1000,jj+1000)
		if (1<=i && i<=n && 1<=j && j<=n)
		{
			LL s1 = S[i-1];
			LL s2 = S[j]-S[i-1];
			LL s3 = S[n]-S[j];

			LL ss = s1;
			if (ss < s2) ss = s2;
			if (ss < s3) ss = s3;

			ans = max( ans, (double)(S[n]-ss)/S[n] );
		}

	WR("%.10lf", ans);
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

		cin >> n >> p >> q >> r >> s;

		FOR(b,1,n) A[b] = (p*(b-1) + q) % r + s;

		cout << "Case #" << a << ": ";
		//sol();
		//cout << " ";
		sol2();
		cout << "\n";
	}
	return 0;
}
