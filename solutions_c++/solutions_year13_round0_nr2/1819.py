#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<cstring>
#include<cmath>
#include<map>
#define _USE_MATH_DEFINES
using namespace std;

int main() {
	int A[100][100];
	int t;
	scanf("%d", &t);
	int n,m;
	for (int i = 0; i < t; i++) {
		bool possible = true;
		scanf("%d %d", &n, &m);
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				scanf("%d", &A[j][k]);
			}
		}
		for (int x = 1; x < 100; x++) {
			for (int j = 0; j < n; j++) {
				bool found = true;
				for (int k = 0; k < m; k++) {
					if (A[j][k] > x) {
						found = false;
						break;
					}
				}
				if (found) {
					for (int k = 0; k < m; k++) {
						A[j][k] = 0;
					}
				}
			}
			for (int k = 0; k < m; k++) {
				bool found = true;
				for (int j = 0; j < n; j++) {
					if (A[j][k] > x) {
						found = false;
						break;
					}
				}
				if (found) {
					for (int j = 0; j < n; j++) {
						A[j][k] = 0;
					}
				}
			}
			bool found = false;
			bool done = true;
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < m; k++) {
					if (A[j][k] == x) {
						found = true;
						break;
					}
					if (A[j][k] != 0) {
						done = false;
					}
				}
				if (found) {
					break;
				}
			}
			if (found) {
				possible = false;
				break;
			}
			if (done) {
				//printf("done : %d\n", x);
				break;
			}
		}
		///////////////////
	/*		for (int j = 0; j < n; j++) {
				for (int k = 0; k < m; k++) {
					printf("%d ", A[j][k]);
				}
				printf("\n");
			}*/

		///////////////////
		if (possible) {
			printf("Case #%d: YES\n", i+1);
		}
		else {
			printf("Case #%d: NO\n", i+1);
		}
	}
	return 0;
}
