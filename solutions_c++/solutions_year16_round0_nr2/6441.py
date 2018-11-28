#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char s[1010];
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int kase = 1; kase <= t; kase++) {
		scanf("%s", s);

		int len = strlen(s);
		char tmp_c = s[0];
		int ans = 0;

		for (int i= 0; i < len; i++) {
			if (tmp_c != s[i]) {
				ans++;
				tmp_c = s[i];
			}
		}
		if (tmp_c == '-') ans++;

		printf("Case #%d: %d\n", kase, ans);
	}

	return 0;
}
