#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <algorithm>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
using namespace std;

void InitFiles() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

long long a[1000 * 1000];

void Solve() {
	long long curW, n;
	cin >> curW >> n;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	sort(a, a + n);

	long long ans = n;
	long long curOp = 0;
	for (int i = 0; i < n; ++i) {
		ans = min(ans, curOp + n - i);
		if (curW > a[i]) {
			curW += a[i];
		} else {
			if (curW == 1) {
				curOp += 1;
				continue;
			}
			while (curW <= a[i]) {
				curW += curW - 1;
				++curOp;
			}
			curW += a[i];
		}
	}
	ans = min(ans, curOp);
	cout << ans << endl;
}

int main() {
	InitFiles();
	int t;
	char buf[100];
	gets(buf);
	t = atoi(buf);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}