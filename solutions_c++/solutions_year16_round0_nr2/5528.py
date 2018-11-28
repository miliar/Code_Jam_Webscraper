
#include <bits/stdc++.h>
using namespace std;

typedef long long int i64;
#define REP(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define FOR(i,a,b) for( __typeof(a) i=a; i<=b; i++)
#define RFOR(i,a,b) for( __typeof(a) i=a; i>=b; i--)
#define endl '\n'
const int INF = 2147483647;
const int MAX = 1e5 + 10;
const int MOD = 1000000007;



int main(){

	ios_base::sync_with_stdio(0);
	cin.tie(NULL);

	#ifndef ONLINE_JUDGE
		freopen("B-large.in", "r", stdin);
		freopen("B-larger.out", "w", stdout);
	#endif

	string s = "--+-", final = "++++";

	int t;
	cin >> t;

	FOR(tc,1,t){

		cout << "Case #" << tc << ": ";
		cin >> s;
		int sz = s.size();
		int ans = 0;

		if( sz == 1 )
			cout << ( s[0] == '+' ? 0 : 1 ) << endl;

		else{
			FOR(i,0,sz-2){
				if( s[i] != s[i+1] ){
					ans += 1;
				}
			}
			if( s[sz-1] == '-' )
				ans += 1;
			cout << ans << endl;
		}
	}

	return 0;

}
