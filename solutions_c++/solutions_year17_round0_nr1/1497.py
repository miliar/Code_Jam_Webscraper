#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define vi vector<ll>
#define vvi vector<vi>
#define pb push_back
#define forn(i,n) for( i = 0; i < n; i++ )
#define s(n) scanf("%lld",&n);
#define MODN 1000000007

int main()
{
	freopen("in1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	ll i, j, ii, t;
	s(t);
	for( ii = 1 ; ii <= t ; ii++ )
	{
		ll n, k;
		string str;
		cin >> str; s(k);
		n = str.length();
		ll ans = 0;
		for( i = 0; i + k - 1 < n; i++ ){
			if( str[i] == '-' ){
				ans++;
				for( j = i; j < i+k; j++ ) str[j] = ( str[j] == '-' ) ? '+' : '-' ;
			}
		}
		for( i = n-1; i >= 0 && str[i] != '-'; i-- );
		if( i == -1 ) cout << "Case #" << ii << ": " << ans << endl;
		else cout << "Case #" << ii << ": " << "IMPOSSIBLE" << endl;
	}
}
