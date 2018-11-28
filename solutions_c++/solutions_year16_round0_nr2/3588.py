#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define vi vector<ll>
#define vvi vector<vi>
#define pb push_back
#define forn(i,n) for( i = 0; i < n; i++ )
#define s(n) scanf("%lld",&n);

int main()
{
	ll i, ii, t, n, ans;
	s(t);
	string str;
	for( ii = 1 ; ii <= t; ii++ )
	{
		ans = 0;
		cin >> str;
        n = str.length();
		for( i = 1; i < n ; i++ ){
			if( str[i] == '-' && str[i-1] == '+' ) ans += 2;
		}
		if( str[0] == '-') ans++;
		printf("Case #%lld: %lld\n", ii, ans);
	}
    return 0;
}