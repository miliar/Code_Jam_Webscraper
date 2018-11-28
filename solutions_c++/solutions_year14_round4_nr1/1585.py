#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 100005;
const double eps = 1e-8;
const int inf = 0x3f3f3f3f;

int n, cap;
int disc[maxn];

int solve() {
	sort(disc, disc + n);
	int i = 0, j = n - 1;
	int cnt = 0;
	while (i <= j) {
		if (i == j) {
			cnt ++;
			break;
		}
		if (disc[j] + disc[i] > cap) {
			j --;
			cnt ++;
		} else {
			j --;
			i ++;
			cnt ++;
		}
	}
	return cnt;
}

int main(int argc, char const *argv[]) {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas;
	scanf ("%d", &cas);
	for (int t = 1; t <= cas; t ++) {
		cin >> n >> cap;
		for (int i = 0; i < n; i ++) {
			cin >> disc[i];
		}
		int ans = solve();
		printf ("Case #%d: %d\n", t, ans);
	}
	return 0;
}