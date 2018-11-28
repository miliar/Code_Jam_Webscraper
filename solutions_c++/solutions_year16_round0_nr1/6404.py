#include <bits/stdc++.h>
using namespace std;

bitset<10> mark;
bitset<10> mask(~0);
int n;

bool split(int val) {
	int t;
	while (val) {
		t = val % 10;
		mark[t] = 1;
		val /= 10;
	}
	return mark == mask;
}

void solve(int cas) {
	int t = 0;
	mark = 0;
	printf("Case #%d: ", cas);
	if (n == 0) {
		puts("INSOMNIA"); return;
	}
	while (1) {
		t += n;
		if (split(t)) {
			printf("%d\n", t);
			return;
		}
	}
}

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		scanf("%d", &n); solve(i);
	}
	return 0;
}