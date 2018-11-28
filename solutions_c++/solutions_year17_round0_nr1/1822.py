#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = (a); i < int(b); ++i)
#define rrep(i,b,a) for(int i = (b); i --> int(a);)
#define trav(i,v) for(auto&i:v)
#define all(c) (c).begin(), (c).end()
#define sz(c) int((c).size())
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	rep(t,1,T+1) {
		cout << "Case #" << t << ": ";
		string s;
		int k,ans = 0;
		cin >> s >> k;
		rep(i,0,sz(s)-k+1) if(s[i] == '-') {
			rep(j,i,i+k) s[j] ^= 6;
			++ans;
		}
		trav(i,s) if(i == '-') ans = -1;
		if(ans == -1) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
}