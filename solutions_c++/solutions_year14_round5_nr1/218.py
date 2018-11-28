#include<bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<__LINE__<<": "<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
const int inf = (int)1e9;
const double INF = 1e12, EPS = 1e-9;

void solve(){
	int n, p, q, r, s;
	cin >> n >> p >> q >> r >> s;
	vi v;
	ll sum = 0;
	ll L = 0, R = 0;
	ll ans = 3e18;
	
	rep(i, n){
		v.pb(((ll)i * p + q) % r + s);
		sum += v.back();
	}
	
	int j = 0;
	
	rep(i, n + 1){
		while(j < n && (j < i || sum - R > R - L && sum - R > L)) R += v[j++];
		if(j > i){
			R -= v[--j];
			ans = min(ans, max(max(sum - R, R - L), L));
			R += v[j++];
		}
		ans = min(ans, max(max(sum - R, R - L), L));
		L += v[i];
	}
	printf("%.20f\n", 1 - ans * 1.0 / sum);
}

int main(){
	int CS; cin >> CS;
	rep(cs, CS){
		cout << "Case #" << cs + 1 << ": ";
		solve();
	}
	return 0;
}
