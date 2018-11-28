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
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
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


#define maxn 2100000
int dp[2][maxn];

void check(int &a, int b) {
	a = min(a, b);
}

int main() {
	freopen("F:/TDDOWNLOAD/A-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/A-large.out", "w", stdout);

	int Te; cin>>Te;
	for(int te=1;te<=Te;te++) {
		
		int A, N;
		cin>>A>>N;
		vector<int> v;
		rep(i, 0, N) {
			int x; cin>>x;
			v.push_back(x);
		}
		sort(all(v));
		bool now = false;
		clr(dp[now], 0x3f);
		dp[now][A] = 0;
		int MM = max(A, v[sz(v)-1]) + 10;
		rep(i, 0, sz(v)) {
			rep(j, 0, MM) dp[!now][j] = 1000000;
			rep(j, 0, MM) {
				if(j > v[i]) check(dp[!now][min(MM-1, j+v[i])], dp[now][j]);
				check(dp[!now][j], dp[now][j]+1);//delete
				check(dp[now][min(MM-1, j+j-1)], dp[now][j]+1); // add
			}
			now = !now;
		}
		int ans = 1000000;
		rep(j, 0, MM) check(ans, dp[now][j]);
		printf("Case #%d: ", te);
		printf("%d\n", ans);
	}
}