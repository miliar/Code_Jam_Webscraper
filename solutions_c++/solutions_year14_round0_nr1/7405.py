#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int n, T;
	scanf("%d", &T);
	int a[4], b[4], c[4];
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d", &n);
		for (int i = 1; i <= 4; ++i) {
			for (int j = 0; j < 4; ++j) scanf("%d", a+j);
			if (i == n) memcpy(b, a, sizeof(b));
		}
		scanf("%d", &n);
		for (int i = 1; i <= 4; ++i) {
			for (int j = 0; j < 4; ++j) scanf("%d", a+j);
			if (i == n) memcpy(c, a, sizeof(b));
		}
		int cnt = 0, ans;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) if (b[i] == c[j]) ++cnt, ans = b[i];
		printf("Case #%d: ", tt);
		if (cnt == 1)
			printf("%d\n", ans);
		else if (cnt > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
}