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

const int maxn = 5;

int v[maxn][maxn];

vector <int> x;
int n;
bool used[maxn];

bool go(int pos) {
	if (pos == (int)x.size()) {
		return true;
	}

	bool st = false;

	for (int i = 0; i < n; i++) {
		if (v[x[pos]][i] == 1 && !used[i]) {
			st = true;
			used[i] = true;

			if (!go(pos + 1)) {
				return false;
			}

			used[i] = false;
		}
	}

	return st;
}

int get_ans() {
	bool st = false;

	x.clear();
	for (int i = 0; i < n; i++) {
		x.push_back(i);
	}

	while (true) {
		memset(used, 0, sizeof used);
		if (!go(0)) {
			return 1000000;
		}

		if (!next_permutation(x.begin(), x.end())) {
			break;
		}
	}

	return 0;
}

int getr(int x, int y) {
	if (x == n) {
		x = 0;
		y++;
	}

	if (y == n) {
		return get_ans();
	}

	int ans = getr(x + 1, y);
	if (v[x][y] == 0) {
		v[x][y] = 1;
		ans = min(ans, getr(x + 1, y) + 1);
		v[x][y] = 0;
	}

	return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;

	int ts = 0;

	while (t--) {
		ts++;

		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			scanf(" ");
			for (int j = 0; j < n; j++) {
				char c;
				scanf("%c", &c);
				v[i][j] = c - '0';
			}
		}

		printf("Case #%d: ", ts);

		int ans = getr(0, 0);

		cout << ans << endl;
	}

	return 0;
}
