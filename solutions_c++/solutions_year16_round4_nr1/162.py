#include <cstdio>
#include <iostream>
using namespace std;

int t, d[3], n;
int a[40][3];
string R[40], P[40], S[40];
char s[] = "RPS";
string com(string A, string B) {
	return min(A + B, B + A);
}
int main() {
	scanf("%d", &t);
	R[0] = "R";
	P[0] = "P";
	S[0] = "S";
	for (int i = 1; i <= 12; i++) {
		R[i] = com(R[i - 1], S[i - 1]);
		P[i] = com(P[i - 1], R[i - 1]);
		S[i] = com(S[i - 1], P[i - 1]);
	}
	for (int tt = 1; tt <= t; tt++) {
		scanf("%d", &n);
		a[0][0] = 1;
		for (int i = 1; i <= n; i++) {
			a[i][0] = a[i - 1][0] + a[i - 1][1];
			a[i][1] = a[i - 1][1] + a[i - 1][2];
			a[i][2] = a[i - 1][2] + a[i - 1][0];
		}
		scanf("%d%d%d", &d[0], &d[1], &d[2]);
		int flag = true;
		for (int i = 0; i < 3; i++) {
			int same = true;
			for (int j = 0; j < 3; j++) {
				if (d[j] != a[n][(j + 3 - i) % 3]) {
					same = 0;
				}
			}
			if (same) {
				flag = false;
				printf("Case #%d: ", tt);
				if (i == 0) {
					printf("%s\n", R[n].c_str());
				}
				if (i == 1) {
					printf("%s\n", P[n].c_str());
				}
				if (i == 2) {
					printf("%s\n", S[n].c_str());
				}
				break;
			}
		}
		if (flag) {
			printf("Case #%d: IMPOSSIBLE\n", tt);
		}
	}
	return 0;
}