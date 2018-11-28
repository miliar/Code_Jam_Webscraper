#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int N = 16;
const int J = 50;

int dig[20];
int dvs[20];
int cnt = 0;

long long get_factor(long long x) {
	for (long long i = 2; i * i <= x; ++i) {
		if (x % i == 0) return i;
	}
	return 0;
}

bool check() {
	for (long long base = 2; base <= 10; ++base) {
		long long t = 0;
		for (int i = 0; i < N; ++i) {
			t = t * base + (long long)dig[i];
		}
		dvs[base] = get_factor(t);
		if (!dvs[base]) return false;
	}
	return true;
}

void output() {
	for (int i = 0; i < N; ++i) {
		printf("%d", dig[i]);
	}
	for (int i = 2; i <= 10; ++i) {
		printf(" %d", dvs[i]);
	}
	puts("");
}

void dfs(int pos, int val) {
	dig[pos] = val;
	if (pos == N - 2) {
		if (check()) {
			output();
			++cnt;
			if (cnt == J) exit(0);
		}
		return;
	}
	dfs(pos + 1, 0);
	dfs(pos + 1, 1);
}

int main() {
	freopen("C1.out", "w", stdout);
	cout << "Case #1:" << endl;
	dig[0] = dig[N - 1] = 1;
	dfs(1, 0);
	dfs(1, 1);
	return 0;
}
