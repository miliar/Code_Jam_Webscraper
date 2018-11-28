#include<bits/stdc++.h>

int t;
char s[200];
bool a[200];

bool solved(int n) {
	for (int i = 0; i < n; i++) if(a[i] == false) return false;
	return true;
}

void reverse(int x, int y) {
	for (int i = x, j = y; i < j; i++, j--) {
		bool tmp = a[i];
		a[i] = a[j];
		a[j] = tmp;
	}
}

void flip(int x, int y) {
	for (int i = x; i < y; i++) a[i] = !a[i];
}

int lastFalse(int n) {
	for (int i = n - 1; i >= 0; i--) if(!a[i]) return i;
}

int firstTrue(int n) {
	for (int i = 0; i < n; i++) if(a[i]) return i;
	return n;
}

int solve(int n) {
	for (int i = 0; ; i++) {
//		for (int j = 0; j < n; j++) printf("%c%s", a[j] ? '+' : '-', j == n - 1 ? "\n" : "");
		if (solved(n)) return i;
		if (a[0] == true) reverse(0, lastFalse(n));
		else flip(0, firstTrue(n));
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	int i = 0;
	while(t--) {
		i++;
		scanf("%s", s);
		for (int j = 0; s[j]; j++) {
			if(s[j] == '+') a[j] = true;
			else a[j] = false;
		}
		printf("Case #%d: %d\n", i, solve(strlen(s)));
	}
	scanf("\n");
	return 0;
}
