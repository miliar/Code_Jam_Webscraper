#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
#include <cstdio>
#include <vector>
#include <cctype>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

typedef long double LD;
typedef long long LL;

using namespace std;

#define sz(A) (int)(A).size()
#define mp make_pair
#define pb push_back

const int N = 105;

char a[N][N];

int main() {
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		int r, c;
		cin >> r >> c;
		int res = 0;

		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cin >> a[j][k];
			}
		}

		bool impossible = false;
		for (int j = 0; j < r; j++) {		
			for (int k = 0; k < c; k++) {
				if (a[j][k] != '.') {
					bool ok = false;
					for (int q = 0; q < r; q++) {
						if (q != j && a[q][k] != '.') ok = true;
					}
					for (int q = 0; q < c; q++) {
						if (q != k && a[j][q] != '.') ok = true;
					}
					if (!ok) {
						impossible = true;
					}
				}
			}			
		}

		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				if (a[j][k] == '<') res++;
				if (a[j][k] != '.') break;
			}
			for (int k = c - 1; k >= 0; k--) {
				if (a[j][k] == '>') res++;
				if (a[j][k] != '.') break;
			}
		}
		
		for (int j = 0; j < c; j++) {
			for (int k = 0; k < r; k++) {
				if (a[k][j] == '^') res++;
				if (a[k][j] != '.') break;
			}
			for (int k = r - 1; k >= 0; k--) {
				if (a[k][j] == 'v') res++;
				if (a[k][j] != '.') break;
			}
		}


		if (!impossible)
			printf("Case #%d: %d\n", i + 1, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
	}

	return 0;
}
