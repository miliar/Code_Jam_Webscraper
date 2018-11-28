#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
using namespace std;

void solve(int test) {
	int n;
	cin >> n;
	if (n == 0) {
		printf("Case #%d: INSOMNIA\n", test);
		return;
	}
	bool visited[10];
	int cnt = 0;
	memset(visited, 0, sizeof(visited));
	int t;
	for (t = n; ; t += n) {
		int c = t;
		while (c != 0) {
			if (!visited[c % 10]) {
				visited[c % 10] = true;
				++cnt;
			}
			c /= 10;
		}
		if (cnt == 10) break;
	}
	printf("Case #%d: %d\n", test, t);
}

int main() {
//	freopen("test.in", "r", stdin);
//	freopen("test.our", "w", stdout);
	int testNumber;
	cin >> testNumber;
	for (int test = 1; test <= testNumber; ++test) {
		solve(test);
	}
}