#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;

int T,N,K;
double probs[200],p2[16];
double dp[17][17];
int main() {
	cin >> T;
	cout << fixed << setprecision(15);
	for (int cas=1;cas<=T;cas++) {
		cin >> N >> K;
		for (int c=0;c<N;c++) cin >> probs[c];
		double mp=0;
		for (int mask=0;mask<(1<<N);mask++) if (__builtin_popcount(mask)==K) {
			for (int c=0,off=0;c<N;c++) if ((1<<c)&mask)
				p2[off++]=probs[c];
			fill(dp[0],dp[17],0);
			dp[0][0]=1;
			for (int i=0;i<K;i++) for (int j=0;j<N;j++) {
				dp[i+1][j+1]+=p2[i]*dp[i][j];
				dp[i+1][j]+=(1-p2[i])*dp[i][j];
			}
			mp=max(mp,dp[K][K/2]);
		}

		printf("Case #%d: ",cas);
		cout << mp << endl;
	}
}
