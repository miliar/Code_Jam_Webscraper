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
	ll i, ii, t, n;
	s(t);
	string str;
	for( ii = 1 ; ii <= t; ii++ )
	{
		cin >> str;
        n = str.length();
		ll hash[27] = {0};
		for( i = 0; i < n ; i++ ){
			hash[str[i] - 'A']++;
		}
		ll ans[11] = {0};

		if( hash['Z'-'A'] > 0) {
			ll cnt = hash['Z'-'A'];
			hash['Z'-'A'] -= cnt;
			hash['E'-'A'] -= cnt;
			hash['R'-'A'] -= cnt;
			hash['O'-'A'] -= cnt;
			ans[0] += cnt;
		}
		if( hash['W'-'A'] > 0) {
			ll cnt = hash['W'-'A'];
			hash['T'-'A'] -= cnt;
			hash['W'-'A'] -= cnt;
			hash['O'-'A'] -= cnt;
			ans[2] += cnt;
		}
		if( hash['U'-'A'] > 0) {
			ll cnt = hash['U'-'A'];
			hash['F'-'A'] -= cnt;
			hash['O'-'A'] -= cnt;
			hash['U'-'A'] -= cnt;
			hash['R'-'A'] -= cnt;
			ans[4] += cnt;
		}
		if( hash['X'-'A'] > 0) {
			ll cnt = hash['X'-'A'];
			hash['S'-'A'] -= cnt;
			hash['I'-'A'] -= cnt;
			hash['X'-'A'] -= cnt;
			ans[6] += cnt;
		}
		if( hash['G'-'A'] > 0) {
			ll cnt = hash['G'-'A'];
			hash['E'-'A'] -= cnt;
			hash['I'-'A'] -= cnt;
			hash['G'-'A'] -= cnt;
			hash['H'-'A'] -= cnt;
			hash['T'-'A'] -= cnt;
			ans[8] += cnt;
		}
		if( hash['O'-'A'] > 0 ) {
			ll cnt = hash['O'-'A'];
			hash['O'-'A'] -= cnt;
			hash['N'-'A'] -= cnt;
			hash['E'-'A'] -= cnt;
			ans[1] += cnt;
		}
		if( hash['H'-'A'] > 0 ) {
			ll cnt = hash['H'-'A'];
			hash['T'-'A'] -= cnt;
			hash['H'-'A'] -= cnt;
			hash['R'-'A'] -= cnt;
			hash['E'-'A'] -= 2 * cnt;
			ans[3] += cnt;
		}
		if( hash['F'-'A'] > 0 ) {
			ll cnt = hash['F'-'A'];
			hash['F'-'A'] -= cnt;
			hash['I'-'A'] -= cnt;
			hash['V'-'A'] -= cnt;
			hash['E'-'A'] -= cnt;
			ans[5] += cnt;
		}
		if( hash['S'-'A'] > 0) {
			ll cnt = hash['S'-'A'];
			hash['S'-'A'] -= cnt;
			hash['E'-'A'] -= 2 * cnt;
			hash['V'-'A'] -= cnt;
			hash['N'-'A'] -= cnt;
			ans[7] += cnt;
		}
		if( hash['I'-'A'] > 0 ) {
			ll cnt = hash['I'-'A'];
			hash['N'-'A'] -= 2 * cnt;
			hash['I'-'A'] -= cnt;
			hash['E'-'A'] -= cnt;
			ans[9] += cnt;
		}
		printf("Case #%lld: ", ii);
		for( ll i = 0; i < 10; i++ ){
			while( ans[i] > 0 ){
				 cout << i;
				 ans[i]--;
			}
		}
		cout << endl;
	}
    return 0;
}