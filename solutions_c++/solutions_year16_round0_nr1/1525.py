#include<bits/stdc++.h>

int t, n;

void add(bool u[], int &s, int x) {
	if (x == 0) return;
	if (!u[x%10]) {
		u[x%10] = true;
		s++;
	}
	if (s == 10) return;
	add(u, s, x/10);
}

int solve(int n) {
	int s = 0, i;
	bool u[10];
	for (i = 0; i < 10; i++) u[i] = false;
	for (i = 1; s != 10; i++) add(u, s, n * i);
	return --i * n;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	int i = 0;
	while(t--) {
		i++;
		scanf("%d", &n);
		if (n) printf("Case #%d: %d\n", i, solve(n));
		else printf("Case #%d: INSOMNIA\n", i);
	}
	scanf("\n");
	return 0;
}
