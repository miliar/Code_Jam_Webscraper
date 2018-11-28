#include <bits/stdc++.h>
using namespace std;

FILE *fout = fopen("output.out", "w");

int f(int n, int i, vector<int> &d) {
	int bn = n;
	n = n * i;
	while (n) {
		d[n % 10] = 1;
		n /= 10;
	}
	n = bn;
	int chk = 1;
	for (int i = 0; i < 10; ++i)
		chk &= d[i];
	if (chk) return n * i;
	return f(n, i + 1, d);
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int tcn = 1; tcn <= tc; ++tcn) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", tcn);
		fprintf(fout, "Case #%d: ", tcn);
		if (n == 0) {
			printf("INSOMNIA");
			fprintf(fout, "INSOMNIA");
		} else {
			vector<int> digit(10, 0);
			int res = f(n, 1, digit);
			printf("%d", res);
			fprintf(fout, "%d", res);
		}
		puts("");
		fprintf(fout, "\n");
	}
	return 0;
}