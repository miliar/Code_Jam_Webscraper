#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define FORR(i, n) FOR(i, 0, n)
using namespace std;
//TA ERRADO

int matrix[105][105], matrix2[105][105];
bool ok(int n, int m) {
	int maior;
	FORR(i, n) {
		maior = 0;
		FORR(j, m) {
			maior = max(maior, matrix[i][j]);
		}
		FORR(j, m) matrix2[i][j] = maior;
	}

	FORR(i, n) {
		FORR(j, m) {
			if(matrix2[i][j] != matrix[i][j]) {
				FORR(k, n) if(matrix2[k][j] > matrix[i][j]) matrix2[k][j] = matrix[i][j];
			}
		}
	}

	FORR(i, n) {
		FORR(j, m) {
			if(matrix2[i][j] != matrix[i][j]) return false;
		}
	}
	return true;
}

int main() {
	int t, n, m;
	scanf("%d", &t);
	FORR(l, t) {
		scanf("%d %d", &n, &m);
		FORR(i, n) {
			FORR(j, m) {
				scanf("%d", &matrix[i][j]);
			}
		}
		printf("Case #%d: ", l+1);
		if(ok(n, m)) printf("YES\n");
		else printf("NO\n");
	}
}
