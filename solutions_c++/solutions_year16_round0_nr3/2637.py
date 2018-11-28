#include <bits/stdc++.h>
using namespace std;
int a[11][16], r[11];
int T, N, J; 

long long check(long long x) {
	for(long long i = 2; i * i <= x; i++) {
		if(x % i == 0) return i;
	}
	return -1;
}
void solveBig() {
	return;
}
void solveSmall() {
	long long num[11], div[11];
	for(int i = (1 << 15) + 1; (i < (1 << 16)) && (J > 0); i += 2) {
		for(int j = 2; j <= 10; j++) {
			num[j] = 0;
			long long base = 1;
			for(int k = 0; k < 16; k++) {
				if(i >> k & 1) num[j] += base;
				base *= j;
			}
		}
		bool flag = 0;
		for(int j = 2; j <= 10 && flag == 0; j++) {
			div[j] = check(num[j]);
			if(div[j] == -1) flag = 1;
		}
		if(flag == 0) {
			for(int j = 15; j >= 0; j--) printf("%d", i >> j & 1);
			for(int j = 2; j <= 10; j++) printf(" %I64d", div[j]);
			printf("\n");
			J--;
			cerr << J << endl;
		}
	}
}
int main() {

	//freopen("C-small-attempt2.in", "r", stdin);
	//freopen("new.out", "w", stdout);

	scanf("%d%d%d", &T, &N, &J);
	printf("Case #1:\n");
	if(N == 16) {
		solveSmall();
	} else {
		solveBig();
	}
	return 0;
}
