#include <iostream> 
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <functional>
#include <cstring>
#include <algorithm>
#include <map>
#include <cmath>
#include <ctime>
#include <unordered_map>

using namespace std;

int a[4][4];
int b[4][4];

int check(int i, int j, int n) {
	for (int k = 0; k < n; ++k) {
		if (b[i][k] != b[j][k]) return 0;
	}
	return 1;
}

int solve() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			char c;
			cin >> c;
			a[i][j] = c - '0';
		}

	int ans = n*n;
	for (int i = 0; i < (1 << n*n); ++i) {
		int cnt = 0;
		for (int j = 0; j < n*n; ++j) {
			if (i >> j & 1) {
				cnt += !a[j / n][j%n];
				b[j / n][j%n] = 1;
			}
			else {
				if (a[j / n][j%n]) cnt = n*n;
				b[j / n][j%n] = 0;
			}
		}

		int ok = 1;
		for (int i = 0; i < n; ++i) {
			int x = 0, y = 0;
			for (int j = 0; j < n; ++j) {
				if (b[j][i] && !y) {
					for (int k = 0; k < n; ++k) {
						if (b[j][i] && b[k][i]) ok &= check(j, k, n);
					}
					for (int k = 0; k < n; ++k) {
						y += b[j][k];
					}
				}
				x += b[j][i];
			}
			ok &= x > 0;
			ok &= x == y;
		}
		if (ok) ans = min(ans, cnt);
	}
	return ans;
}


int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);

	cout.setf(ios::fixed);
	cout.precision(9);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		cout << solve() << endl;
	}

}