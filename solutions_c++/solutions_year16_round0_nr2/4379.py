#include <bits/stdc++.h>
using namespace std;

FILE *fout = fopen("output.out", "w");

int n, sol;
char a[111];

int areAllHappy() {
	int chk = 1;
	for (int i = 1; i <= n; ++i)
		chk &= a[i] == '+';
	return chk;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int tcn = 1; tcn <= tc; ++tcn) {
		scanf("%s", a + 1);
		n = strlen(a + 1);
		sol = 0;
		while (!areAllHappy()) {
			++sol;
			int s;
			for (s = 1; s <= n && a[s] != '-'; ++s);
			int e;
			for (e = s + 1; e <= n && a[e] == '-'; ++e);
			for (int i = 1; i < e; ++i) a[i] = '+' + '-' - a[i];
		}
		printf("Case #%d: %d\n", tcn, sol);
		fprintf(fout, "Case #%d: %d\n", tcn, sol);
		memset(a, 0, sizeof(a));
	}
	return 0;
}