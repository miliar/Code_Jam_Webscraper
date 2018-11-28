#include <bits/stdc++.h>

using namespace std;

int does(char x[101]) {
	int ans = 1;
	char curr = x[0];
	for (int i = 0; i < (int) strlen(x); i++) {
		if (x[i] != curr) {
			curr = x[i];
			ans++;
		}
	}
	if (curr == '+') ans--;
	if (ans < 0) ans = 0;
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	char x[101];
	for (int i = 1; i <= t; i++) {
		if (i == 1) gets(x);
		gets(x);
		if (x[0] == '-' && 1 == (int)strlen(x)) {
			printf("Case #%d: %d\n", i, 1);
			continue;
		} else if (x[0] == '+' && 1 == (int)strlen(x)) {
			printf("Case #%d: %d\n", i, 0);
			continue;
		}
		int ans = does(x);
		printf("Case #%d: %d\n", i, ans);
	}
}
