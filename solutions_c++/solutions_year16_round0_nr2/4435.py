#include <bits/stdc++.h>

using namespace std;

int t;

void solve(char *s) {
	int n = strlen(s);
	int w = 0;
	bool state = 0;
	for (int i = n-1; i >= 0; i--) {
		bool cur = (s[i] == '+') ^ state;
		if (!cur) {
			state = !state;
			w++;
		}
	}
	printf("%d\n", w);
}

int main() {
	scanf("%d", &t);
	char s[200];
	for (int i = 1; i <= t; i++) {
		scanf("%s", s);
		printf("Case #%d: ", i);
		solve(s);
	}
	return 0;
}