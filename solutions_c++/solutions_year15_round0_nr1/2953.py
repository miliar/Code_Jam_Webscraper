#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <fstream>
#include <cassert>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <numeric>
#include <ctime>
#include <cstdlib>
#include <sstream>

using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define pii pair<int, int>
#define pll pair<long long, long long>
#define y1 stupid_y1
#define ll long long
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x)*(x))
#define sz(a) (int)a.size()
#define file "a"

const int inf = (int)1e9;
const double eps = 1e-9;
const double pi = acos(-1.0);


void solve(){
	int n;
	string s;
	cin >>n;
	cin >>s;

	int total = 0;
	int ans = 0;
	for (int i=0;i<s.length();i++){
		int t = s[i] - '0';
		int add = max(i-total, 0);
		ans += add;
		total += add;
		total += t;
	}
	printf("%d\n", ans);
}

int main () {
	#ifdef LOCAL
	freopen(file".in", "r", stdin);
	freopen(file".out", "w", stdout);
	#endif

	int tests;
	cin >>tests;

	for (int i=0;i<tests;i++){
		printf("Case #%d: ", i + 1);
		solve();
	}

	#ifdef LOCAL
	cerr << (double)clock() * 1.0 / CLOCKS_PER_SEC << endl;
	#endif

	return 0;
}

