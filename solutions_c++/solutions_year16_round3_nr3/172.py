#include<bits/stdc++.h>

using namespace std;

int AB[10][10], AC[10][10], BC[10][10], ABC[10][10][10], A[1000], B[1000], C[1000];

int main() {
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++) {
		int a, b, c, K, ans = 0;
		scanf("%d %d %d %d", &a, &b, &c, &K);
		
		for (int i = 0; i < c; i++)
			for (int j = 0; j < c; j++) {
				AB[i][j] = AC[i][j] = BC[i][j] = K;
				for (int k = 0; k < c; k++) ABC[i][j][k] = 1;
			}
		
		int i = 0, j = 0, k = 0, f = b, g = c;
		while (i < a) {
			while (AB[i][j] == 0 && f > 0) j = (j + 1) % b, f--, g = c;
			if (f == 0) {
				i++;
				f = b;
				g = c;
				j = (B[ans - 1] + 1) % b;
				k = (C[ans - 1] + 1) % c;
				continue;
			}
			while ((AC[i][k] == 0 || BC[j][k] == 0 || ABC[i][j][k] == 0) && g > 0) k = (k + 1) % c, g--;
			if (g == 0) {
				j = (j + 1) % b;
				f--;
				g = c;
				k = (C[ans - 1] + 1) % c;
				continue;
			}
			if (AB[i][j] > 0 && AC[i][k] > 0 && BC[j][k] > 0 && ABC[i][j][k] > 0) {
				AB[i][j]--;
				AC[i][k]--;
				BC[j][k]--;
				ABC[i][j][k]--;
				
				A[ans] = i;
				B[ans] = j;
				C[ans] = k;
				ans++;
			}
		}
		
		printf("Case #%d: %d\n", T, ans);
		for (int i = 0; i < ans; i++) printf("%d %d %d\n", A[i] + 1, B[i] + 1, C[i] + 1);
	}
	
	return 0;
}
