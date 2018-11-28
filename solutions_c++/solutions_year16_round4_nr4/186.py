#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;
int b[30][30];

int check(int n) {
	for (int i = 0; i < n; ++i) {
		int fl2 = 1;
		for (int j = 0; j < (1 << n); ++j) {
			int fl = 0;
			for (int k = 0; k < n; ++k)
				if (!b[i][k] && ((j >> k) & 1)) {
					fl = 1;
					break;
				}
			if (fl)
				continue;
			int cnt = 0;
			for (int k = 0; k < n; ++k) {
				if (k == i)
					continue;
				int fl3 = 0;
				for (int k1 = 0; k1 < n; ++k1)
					if ((j >> k1) & 1)
						if (b[k][k1])
							fl3 = 1;
				cnt += fl3;
			}
			if (cnt < (int)__builtin_popcount(j)) {
				fl2 = 0;
				break;
			}
		}
		if (fl2)
			return 0;
	}
	return 1;
}

int n;
int a[30][30];


int solve() {
	cin >> n;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			char c;
			cin >> c;
			a[i][j] = c - '0';
		}
	}
	int ans = 10000;
	for (int k = 0; k < (1 << (n * n)); ++k) {
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				b[i][j] = a[i][j] | ((k >> (i * n + j)) & 1);
			}
		}
		if (check(n)) {
			ans = min(ans, __builtin_popcount(k));
		}
	}
	return ans;
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 0; i < tt; ++i) {
		cout << "Case #" << i + 1 << ": " << solve() << "\n";
	}
	return 0;
}


