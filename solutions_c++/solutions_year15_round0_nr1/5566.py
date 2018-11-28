#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>


//#include <unordered_map>

using namespace std;

char s[1000001];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++) {
		int n;
		scanf("%d %s", &n, &s);
		int lvl = 0, ans = 0, d = 5, r = 3;
		for (int i = 0; i <= n; i++) {
			if (i > lvl)
				ans += i - lvl;
			if (i > lvl)
				lvl = i;
			lvl += s[i] - '0';
			r += 2;
			d -= 2;
		}
		printf("Case #%d: %d\n", i, ans + d - r + 4*n + 2);
	}

	return 0;
}