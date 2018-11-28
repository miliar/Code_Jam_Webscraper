#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
#define FOR(i, a, b) for(int i = a; i <= b; i ++) 

int test;
int n, m, k;
char a[1000][1000];

int main() {
	freopen("test.inp", "r", stdin);
	freopen("test.out", "w", stdout);

	cin >> test;
	FOR(t, 1, test) {
		printf("Case #%d:\n", t);
		cin >> m >> n >> k;
		if (k == m*n-1) {
			FOR(i, 1, m) {
				FOR(j, 1, n) {
					if (i == m && j == n) printf("c"); else printf("*");
				}
				printf("\n");
			}
		} else if (k ==0) {
			FOR(i, 1, m) {
				FOR(j, 1, n) {
					if (i == m && j == n) printf("c"); else printf(".");
				}
				printf("\n");
			}
		} else 
		if (m==1 || n==1) {
			if (k>=m*n) {
				printf("Impossible\n");
			} else {
				if (m==1) {
					FOR(i, 1, m) {
						FOR(j, 1, k) printf("*");
						FOR(j, k+1, n-1) printf(".");
						printf("c\n");
					}
				} else {
					FOR(i, 1, n) {
						FOR(j, 1, k) printf("*\n");
						FOR(j, k+1, m-1) printf(".\n");
						printf("c\n");
					}
				}
			}
		} else  if (k >= m * n || (m*n-4 < k && k < m*n-1)) 
			printf("Impossible\n");
		else { 
			FOR(i, 1, m) FOR(j, 1, n) {
				if (k>0 && (i<m-1 || j<n-1)) a[i][j]='*', k--;
				else a[i][j]='.';
			}
			a[m][n] = 'c';

			FOR(i, 1, m) {
				FOR(j, 1, n) printf("%c", a[i][j]);
				printf("\n");
			}
		}
	}
	return 0;
}