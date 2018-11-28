#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); i++)
#define For(i, a, b) for(int i = (a); i < (b); i++)
#define foreach(it, c) for(__typeof (c).begin() it = (c).begin(); it != (c).end(); ++it)
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define sz(v) (int)(v).size()
#define all(v) (v).begin(), (v).end()
#define sqr(x) ((x) * (x))
#define fill(m, c) memset((m), (c), sizeof (m))
#define DBG(x) cout << #x << " = " << x << endl

template<class T> T abs(T x) { return x > 0 ? x : -x; }

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<int> vi;

const double EPS = 1e-9;
const double PI = acos(-1.0);
const long long INF = 1ll << 60;
const int MOD = 1e9 + 7;

int a, n;
int v[105];
ll dp[105][2000020];

ll go(int i, int x){
	if(i == n) return 0;
	if(x > v[i]) return go(i + 1, min(1000002, x + v[i]));
	if(dp[i][x] != -1) return dp[i][x];
	ll ret = dp[i][x] = 0;
	if(x - 1 + x > x) ret = min(go(i + 1, x), go(i, x + (x - 1))) + 1;
	else ret = go(i + 1, x) + 1;
	return dp[i][x] = ret;
}

int main(){
	clock_t t = clock();
	int tt; cin >> tt;
	for(int t = 1; t <= tt; t++){
		cin >> a >> n;
		rep(i, n) cin >> v[i];
		sort(v, v + n);
		fill(dp, -1);
		cout << "Case #" << t << ": " << go(0, a) << endl;
	}
	cerr << (clock() - t) / (double)CLOCKS_PER_SEC << endl;
	return 0;
}
