#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define vi vector<ll>
#define vvi vector<vi>
#define pb push_back
#define forn(i,n) for( i = 0; i < n; i++ )
#define s(n) scanf("%lld",&n);
vi ans(1000005,0);
void mark( ll n, vi &hash){
    ll r, n1 = n;
	while(n1 != 0){
		r = n1 % 10;
		hash[r]++;
		n1 /= 10;
	}
}

ll go(ll n){
	ll i, j, r, flag = 0;
	vi hash(11,0);
	if( n == 0 ) return 0;
	for( i = 1; i < 1000005; i++ ){
		mark( i*n, hash );
		flag = 0;
		for( j = 0; j < 10; j++ ){
			if( hash[j] > 0 ) flag++;
			else break;
		}
		if( flag == 10 ) return i*n;
	}
	return 0;
}
int main()
{
	ll i, ii, t, n;
	s(t);
	for( i = 0; i < 1000005; i++ ){
        ans[i] = go(i);
    }
	for( ii = 1 ; ii <= t; ii++ )
	{
		s(n);
        if( ans[n] == 0 ) printf("Case #%lld: INSOMNIA\n",ii);
        else printf("Case #%lld: %lld\n", ii, ans[n]);
	}
    return 0;
}