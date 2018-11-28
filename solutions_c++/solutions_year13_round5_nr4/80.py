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


double dp[1<<20];

int main() {
 	freopen("F:/TDDOWNLOAD/D-small-attempt0.in", "r", stdin);
 	freopen("F:/TDDOWNLOAD/D-small-attempt0.out", "w", stdout);

	int T;
	cin>>T;
	rep(te, 1, T+1) {
		string s;
		cin>>s;
		int n = sz(s);

		rep(i, 0, (1<<n)) dp[i] = 0;
		int t = 0;
		rep(i, 0, sz(s)) if(s[i] == 'X') t|=(1<<i);
		dp[t] = 0;

		for(int i=(1<<n)-2;i>=0;i--) {
			double tmp = 0.0;
			rep(j, 0, n) {
				int delay = 0;
				while(i&(1<<((j+delay)%n))) delay++;
				int ni = i|(1<<((j+delay)%n));
				tmp += (n-delay + dp[ni]) / (double)n;
			}
			dp[i] = tmp;
		}


		printf("Case #%d:", te);
		printf(" %.10lf\n", dp[t]);
	}
}

