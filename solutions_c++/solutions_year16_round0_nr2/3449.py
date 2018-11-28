#define _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <sstream>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <ctime>
#include <set>
#include <map>

#define ll long long
#define ld long double
#define mp make_pair
#define TASKNAME "monument"


const int inf = 2 * 1e9;
const int mod = 1e9 + 7;
const ll infll = (ll)1e18;
const ld eps = 1e-9;

const int dx[] = { 1, 0, -1, 0 };
const int dy[] = { 0, -1, 0, 1 };

using namespace std;

void solve() {
	string s;
	cin >> s;
	int n = s.size();
	int ans = 0;
	for (int i = n - 1; i >= 0; i--) {
		int t = s[i] == '-' ? 0 : 1;
		t += ans;
		t %= 2;
		if (t == 0)
			ans++;
	}
	cout << ans;
}

int main() {
#ifdef __DEBUG__
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	clock_t start = clock();
#else
	//assert(freopen(TASKNAME".in", "r", stdin));
	//assert(freopen(TASKNAME".out", "w", stdout));
#endif
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cerr << "Test #" << t + 1 << " in progress\n";
		cout << "Case #" << t + 1 << ": ";
		solve();
		cout << endl;
		cerr << "Test #" << t + 1 << " done\n";
}

#ifdef __DEBUG__
	fprintf(stderr, "\nTime: %Lf\n", ((clock() - start) / (ld)CLOCKS_PER_SEC));
#endif
	return 0;
}