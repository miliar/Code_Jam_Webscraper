#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
typedef long long i64;
const int N = 40;

int n, m, col;
i64 a[N], b[N], c[N];

inline bool Check() {
	for (int i = 2; i <= 10; ++i)
		b[i] = c[i] = 0;
	for (int i = 1; i <= n; ++i)
		for (int j = 2; j <= 10; ++j) 
			b[j] = b[j] * j + a[i];
	for (int i = 2; i <= 10; ++i) {
		bool ok = 0;
		for (i64 j = 2; j * j <= b[i]; ++j)
			if (b[i] % j == 0) {
				c[i] = j;
				ok = 1;
				break;
			}
		if (!ok) return 0;
	}
	return 1;
}

void Dfs(int x) {
	if (col >= m) return;
	if (x == n) {
		if (Check()) {
			++col;
			for (int i = 1; i <= n; ++i)
				printf("%lld", a[i]);
			for (int i = 2; i <= 10; ++i)
				printf(" %lld", c[i]);
			puts("");
		}
		return;
	}
	a[x] = 1;
	Dfs(x+1);
	a[x] = 0;
	Dfs(x+1);
}

int main() {

	int tcase;
	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; ++i) {
		scanf("%d%d", &n, &m);
		a[1] = a[n] = 1;
		printf("Case #%d:\n", i);
		Dfs(2);
	}

	return 0;
}
