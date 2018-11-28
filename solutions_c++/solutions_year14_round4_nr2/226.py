#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int TAM = 1010;

int a[TAM], invA[TAM], n;
int pos[TAM];
int dp[TAM][TAM];

int go ( int i, int j )
{
	int& r = dp[i][j];
	if ( r != -1 ) return r;
	const int val = i + (n-(j+1));
	const int left = n - val;
	if ( i > j ) return r = 0;
	return ( r = min ( pos[val]+go(i+1,j), (left-pos[val]-1)+go(i,j-1) ) );
}


int main ( )
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int nTests;
	cin >> nTests;

	for ( int curT = 1; curT <= nTests; ++curT )
	{
		cin >> n;
		for ( int i = 0; i < n; ++i )
			cin >> a[i];

		vector<int> auxA ( a, a+n );
		sort ( auxA.begin(), auxA.end() );
		auxA.resize ( unique(auxA.begin(),auxA.end()) - auxA.begin() );

		for ( int i = 0; i < n; ++i ) {
			a[i] = lower_bound ( auxA.begin(), auxA.end(), a[i] ) - auxA.begin();
			invA[a[i]] = i;
		}

		for ( int i = 0; i < n; ++i ) {
			pos[a[i]] = 0;
			for ( int j = 0; j < i; ++j )
				if ( a[j] > a[i] )
					pos[a[i]]++;
		}

		memset ( dp, -1, sizeof ( dp ) );
		cout << "Case #" << curT << ": " << go(0,n-1) << '\n';
	}

	return 0;
}
