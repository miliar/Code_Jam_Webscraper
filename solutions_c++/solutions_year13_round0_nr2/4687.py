#include <cstdio>

using namespace std;

int n, m;
int mat[101][101];

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%d", &mat[i][j]);
			}
		}
		bool valid = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				bool flag = true;
				for (int k = 0; k < m; k++) {
					if (mat[i][k] > mat[i][j]) {
						flag = false;
						break;
					}
				}
				if (flag) continue;
				flag = true;
				for (int k = 0; k < n; k++) {
					if (mat[k][j] > mat[i][j]) {
						flag = false;
						break;
					}
				}
				if (!flag) {
					valid = false;
					break;
				}
			}
		}
		printf("Case #%d: ", t);
		if (valid) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
}