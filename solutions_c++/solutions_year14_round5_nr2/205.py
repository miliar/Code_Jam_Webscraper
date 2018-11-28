

#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <set>
#include <cstdlib>
#include <hash_map>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <cstdlib>
#include <cassert>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------

#define maxn 1100


int dp[110][210][2][maxn];

void check(int &a, int b) {
	a = max(a, b);
}

int main() {
	freopen("F:/TDDOWNLOAD/B-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/B-large.out", "w", stdout);

	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		int N, P, Q;
		cin>>P>>Q>>N;
		vector<int> H, G;
		rep(i, 0, N) {
			int h, g;
			cin>>h>>g;
			H.push_back(h);
			G.push_back(g);
		}
		H.push_back(0);
		G.push_back(0);

		clr(dp, -1);
		dp[0][H[0]][0][0] = 0;
		rep(i, 0, N) {
			for(int j=H[i];j>0;j--) rep(b, 0, 2) rep(k, 0, maxn) if(dp[i][j][b][k] >= 0) {
				//printf("dp[%d][%d][%d][%d] = %d\n", i, j, b, k, dp[i][j][b][k]);
				if(j==H[i]) {
					for(int sk=1;sk<=k;sk++) {
						int h = max(0, H[i] - sk * P);
						check(dp[i][h][b][k-sk], dp[i][j][b][k] + (h==0?G[i]:0));
						if(h <= 0) break;
					}
				}
				if(b==1) {
					check(dp[i][max(0, j-Q)][!b][k], dp[i][j][b][k]);
				} else {
					//ignore
					check(dp[i][j][!b][k+1], dp[i][j][b][k]);
					//get
					int h = max(0, j-P);
					check(dp[i][h][!b][k], dp[i][j][b][k] + (h==0?G[i]:0));
				}
			}
			rep(b, 0, 2) rep(k, 0, maxn) if(dp[i][0][b][k] >= 0) {
				check(dp[i+1][H[i+1]][b][k], dp[i][0][b][k]);
			}
		}
		int ans = 0;
		rep(j, 0, 210) rep(b, 0, 2) rep(k, 0, maxn) check(ans, dp[N][j][b][k]);
		//cout<<ma<<endl;
		printf("Case #%d: %d\n", te, ans);
	}
}








