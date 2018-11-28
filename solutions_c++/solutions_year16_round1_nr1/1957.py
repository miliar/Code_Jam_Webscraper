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
	string str, ans;
	for( ii = 1 ; ii <= t; ii++ )
	{
		cin >> str;
        n = str.length();
		ans = str[0];
		for( i = 1; i < n ; i++ ){
			if( ans[0] <= str[i] ) ans = str[i] + ans;
			else ans = ans + str[i];
			//cout << ans << " ";
		}
		printf("Case #%lld: ", ii); cout << ans << endl;
	}
    return 0;
}