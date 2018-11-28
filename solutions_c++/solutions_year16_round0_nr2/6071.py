//AnotherHackyCodeBySmartCoder
//GCJ_B_S.cpp
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minei(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxei(x)  max_element(x.begin(),x.end())-(x).begin()

#define uns(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acusum(x)  accumulate(x.begin(),x.end(),0)
#define acumul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>());
#define bits(x)     __builtin_popcount( x )
#define oo INT_MAX
#define inf 10000000000

const double pi = acos(-1.0);
const double eps = 1e-11;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
void fastIO() {
	std::ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
}
#define MAXN 111
ll dp[2][MAXN];
int main() {
	fastIO();
	freopen("GCJ_B_L_O.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		string s;
		cin >> s;
		for (int j = 0; j < 2; j++)
			for (int i = 0; i < MAXN; i++)
				dp[j][i] = inf;
		int n = sz(s);
		if (s[0] == '-') {
			dp[1][0] = 1;
			dp[0][0] = 0;
		} else {
			dp[0][0] = 1;
			dp[1][0] = 0;
		}

		for (int i = 1; i < n; i++) {
			if (s[i] == '-') {
				dp[0][i] = min(dp[0][i - 1], dp[1][i - 1] + 1);
				dp[1][i] = min(dp[0][i - 1] + 1, dp[1][i - 1] + 2);
			} else {
				dp[0][i] = min(dp[1][i - 1] + 1, dp[0][i - 1] + 2);
				dp[1][i] = min(dp[1][i - 1], dp[0][i - 1] + 1);
			}

		}
		cout << "Case #" << tc << ": " << min(dp[0][n - 1] + 1, dp[1][n - 1])
				<< endl;
	}
	return 0;
}
