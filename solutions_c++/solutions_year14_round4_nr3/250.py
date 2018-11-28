#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

bool used[2005];
int A[2005], B[2005], answer[2005];

int FindMin(int l, int r, int desired) {
	int mn = 1 << 30, pos = -1;
	for (int i = r - 1; i >= l; --i) {
		if (!used[i] && mn > A[i] && (desired == -1 || B[i] == desired)) {
			mn = A[i];
			pos = i;
		}
	}
	return pos;
}

void Solve() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> A[i];
	}
	for (int i = 0; i < n; ++i) {
		cin >> B[i];
	}
	memset(used, 0, sizeof used);
	int pos = 0;
	for (int i = n - 1; i > -1; --i) {
		if (A[i] == 1) {
			pos = i;
			break;
		}
	}
	answer[pos] = 1;
	used[pos] = true;
	for (int i = 1; i < n; ++i) {
		int rp = FindMin(pos + 1, n, B[pos] - 1), lp = FindMin(0, pos, B[pos]);
		if (lp == -1) {
			answer[rp] = i + 1;
			pos = rp;
		} else if (rp == -1) {
			answer[lp] = i + 1;
			pos = lp;
		} else {
/*			if (B[lp] + 1 == B[rp]) {
				answer[lp] = i + 1;
				pos = lp;
			} else {
				answer[rp] = i + 1;
				pos = rp;
			}      1*/
		}
		used[pos] = true;
	}
	for (int i = 0; i < n; ++i) {
		cout << answer[i] << " ";
	}
	cout << endl;
}


int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d:\n", I + 1);
		Solve();
	}
	return 0;
}