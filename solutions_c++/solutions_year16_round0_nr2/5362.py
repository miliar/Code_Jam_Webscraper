
/*
    Created By : stormshadow
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long int i64;
#define pii pair<int,int>
#define vi vector<int>
#define pb(x) push_back(x)
#define mp make_pair
#define ff first
#define ss second
#define endl '\n'
#define clr(x,_) memset(x,_,sizeof(x))
#define REP(i,n) for(int i=0; i<n ; i++)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define RFOR(i,a,b) for(int i=a; i>=b; i--)
#define INF 2147483647
#define MAX 100010
#define MOD 1000000007


int main () {

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
