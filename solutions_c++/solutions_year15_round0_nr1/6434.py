#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define se second
#define fi first

using namespace std;
typedef long long ll;
typedef pair < int, int > pii;
const int MAX=  1e5+5;


int main(){
	
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	int t;
	cin >> t;
	int cur, n , ans, ntc = 1;
	string s;
	while( t-- ){
		cin >> n >> s;
		cur = (s[0]-'0');
		ans = 0;
		for( int i = 1; i <= n ;i++ ){
			if( cur < i && s[i] != '0' ){
				ans += i - cur;
				cur = i;
			}
			cur += s[i]-'0';
		}
		printf("Case #%d: %d\n", ntc, ans );
		ntc ++;
	}
	
	return 0;
}
