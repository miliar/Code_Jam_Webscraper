#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <numeric>
#include <memory.h>
#define mp make_pair
#define pii pair <int, int>
#define ll long long
#define ui unsigned int
#define ld double
#define pll pair <ll, ll> 
 
using namespace std;

vector <char> ans;
vector <char> res;

bool go(int n, int a, int b, int c) {
	if (n == 0) {
		if (a != 0) {
			ans.push_back('S');
		} else if (b != 0) {
			ans.push_back('P');
		} else {
			ans.push_back('R');
		}
		return true;
	}

	int x = a + b - c;

	if (x < 0) {
		return false;
	}

	if (x % 2 != 0) {
		return false;
	}

	x /= 2;

	if (x > a || x > b) {
		return false;
	}

	if (!go(n - 1, x, b - x, a - x)) {
		return false;
	}

	res.clear();

	for (int i = 0; i < (int)ans.size(); i++) {
		if (ans[i] == 'S') {
			res.push_back('P');
			res.push_back('S');
		} else if (ans[i] == 'P') {
			res.push_back('P');
			res.push_back('R');
		} else {
			res.push_back('R');
			res.push_back('S');
		}
	}

	ans = res;

	return true;
}

void sortt(int l, int r) {
	if (l == r) {
		return;
	}

	int m = (l + r) >> 1;

	sortt(l, m);
	sortt(m + 1, r);

	bool st = false;

	for (int i = l; i <= m; i++) {
		int p = i - l + m + 1;

		if (ans[i] > ans[p]) {
			st = true;
			break;
		}

		if (ans[i] < ans[p]) {
			break;
		}
	}

	if (st) {
		for (int i = l; i <= m; i++) {
			int p = i - l + m + 1;

			swap(ans[i], ans[p]);
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;

	int ts = 0;

	while (t--) {
		ans.clear();
		ts++;

		int n, a, b, c;

		cin >> n >> a >> b >> c;

		swap(a, c);

		printf("Case #%d: ", ts);

		if (!go(n, a, b, c)) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			sortt(0, (1 << n) - 1);
			for (int i = 0; i < (int)ans.size(); i++) {
				printf("%c", ans[i]);
			}
			cout << endl;
		}
	}

	return 0;
}
