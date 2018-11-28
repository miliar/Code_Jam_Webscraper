
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <functional>
#include <cctype>
#include <climits>
#include <string>
#include <utility>
using namespace std;

void prn(int testcase, int answer) {
	cout << "Case #" << testcase << ": ";
	cout << answer;
	cout << "\n";
}

const int maxn = (int)1e6;
int answer[maxn + 1];
int rev[maxn + 1];

int revf(int n) {
	int ret = 0;
	while (n) {
		ret = ret * 10 + n % 10;
		n /= 10;
	}
	return ret;
}

void offer(int pos, int val) {
	if (answer[pos] == 0) {
		answer[pos] = val;
	} else {
		answer[pos] = min(answer[pos], val);
	}
}

void init() {
	for (int i = 1; i < maxn; ++i) {
		rev[i] = revf(i);
	}
	for (int i = 1; i <= maxn; ++i) answer[i] = 0;
	answer[1] = 1;
	for (int i = 1; i < maxn; ++i) {
		offer(i + 1, answer[i] + 1);
		if(i < rev[i] && rev[i] <= maxn) offer(rev[i], answer[i] + 1);
	}
}

void solve() {
	init();
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t) {
		int n;
		cin >> n;
		prn(t, answer[n]);
	}

}

int main () {
//#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//#endif

	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	solve();

	return 0;
}