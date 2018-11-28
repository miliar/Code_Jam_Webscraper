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

int n;
int dp[1001][1001];

void solve(){
	cin >> n;
	vi v(n);
	rep(i, n) cin >> v[i];
	rep(i, n+1) rep(j, n+1) dp[i][j] = inf;
	dp[0][0] = 0;
	
	rep(i, n){
		int mni = 0;
		rep(j, v.size()) if(v[j] < v[mni]) mni = j;
		/*
		dbg(mni);
		rep(j, v.size()) cerr<<v[j]<<(j==v.size()-1?"\n":" ");
		*/
		rep(j, i + 1){
			dp[j + 1][i - j] = min(dp[j + 1][i - j], dp[j][i - j] + mni); //tol
			dp[j][i - j + 1] = min(dp[j][i - j + 1], dp[j][i - j] + (int)v.size() - 1 - mni); //tor
		}
		v.erase(v.begin() + mni);
	}
	
	int ans = inf;
	rep(i, n + 1) ans = min(ans, dp[i][n - i]);
	cout << ans << endl;
}

int main(){
	int cs; cin >> cs;
	rep(CS, cs){
		cout << "Case #" << CS + 1 << ": ";
		solve();
	}
	return 0;
}