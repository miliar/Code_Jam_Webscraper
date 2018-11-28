#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <cmath>
using namespace std;

#define CY 105

int ar[CY][CY];
int N, M;

bool can(int n, int m) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			int sum = 0;
			for (int k = 0; k < n; ++k) {
				if (ar[k][j] > ar[i][j]) {
					sum++;
					break;
				}
			}
			for (int k = 0; k < m; ++k) {
				if (ar[i][k] > ar[i][j]) {
					sum++;
					break;
				}
			}
			if (sum >= 2) return false;
		}
	}
	return true;
}

int main(void) {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("me.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int T = 1; T <= cas; ++T) {
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				scanf("%d", &ar[i][j]);
			}
		}
		printf("Case #%d: ", T);
		if (can(N, M)) puts("YES");
		else puts("NO");
	}
	return 0;
}