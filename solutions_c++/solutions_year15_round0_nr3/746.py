#include <bits/stdc++.h>
using namespace std;

/*
		1	i	j	k

	1	1	i	j	k

	i	i	-1	k	-j

	j	j	-k	-1	i

	k	k	j	-i	-1
*/

int prodMat[][5] = {
	{ 0, 0, 0, 0, 0 },
	{ 0, 1, 2, 3, 4 },
	{ 0, 2,-1, 4,-3 },
	{ 0, 3,-4,-1, 2 },
	{ 0, 4, 3,-2,-1 }
};

typedef long long ll;

int prod ( int a, int b ) {
	int r = prodMat[abs(a)][abs(b)];
	if ( (a>0) != (b>0) ) r = -r;
	return r;
}

int fastPow ( int base, ll expo ) {
	int r = 1;
	while ( expo ) {
		if ( expo&1 ) r = prod ( r, base );
		expo >>= 1;
		base = prod(base,base);
	}
	return r;
}

int toInt[300];

int main ( )
{
	toInt['i'] = 2;
	toInt['j'] = 3;
	toInt['k'] = 4;

	ll rep;
	int ntc, n;
	cin >> ntc;
	for ( int test = 1; test <= ntc; ++test ) {
		cin >> n >> rep;
		string s;
		cin >> s;

		int total = 1;
		for ( int i = 0; i < n; ++i )
			total = prod ( total, toInt[int(s[i])] );
		total = fastPow ( total, rep );

		bool can = false;
		int cur = 1;
		bool foundI = false;
		if ( total != -1 )
			goto printAnswer;

		for ( int count = (int)min ( rep, ll(20) ); count--; ) {
			for ( int i = 0; i < n; ++i ) {
				cur = prod ( cur, toInt[int(s[i])] );
				if ( cur == 2 && !foundI ) foundI = true;
				if ( cur == 4 && foundI ) {
					can = true;
					i = n;
					count = 0;
				}
			}
		}

		printAnswer:
		if ( can ) printf ( "Case #%d: YES\n", test );
		else printf ( "Case #%d: NO\n", test );
	}
	return 0;
}
