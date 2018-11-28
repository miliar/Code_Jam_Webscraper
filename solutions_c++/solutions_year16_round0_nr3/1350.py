#include<bits/stdc++.h>

int t, n, j;
bool a[50];

void add(int n) {
	for (int i = n / 2 - 2; i > 0; i--) {
		if (a[i] == false) {
			a[i] = true;
			return;
		}
		a[i] = false;
	}
}

long long convert(bool a[], int n, int k) {
	long long x = 0;
	for (int i = 0; i < n / 2; i++) {
		x *= k;
		x += a[i] ? 1 : 0;
	}
	return x;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int l = 0;
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &n, &j);
		for (int i = 0; i < n; i++) a[i] = false;
		a[0] = a[n / 2 - 1] = true;
		printf("Case #%d:\n", ++l);
		for (int i = 0; i < j; i++) {
			add(n);
			for (int k = 0; k < n / 2; k++) printf("%c", a[k] ? '1' : '0');
			for (int k = 0; k < n / 2; k++) printf("%c", a[k] ? '1' : '0');
			for (int k = 2; k < 11; k++) printf(" %I64d", convert(a, n, k));
			printf("\n");
		}
	}
	scanf("\n");
	return 0;
}
