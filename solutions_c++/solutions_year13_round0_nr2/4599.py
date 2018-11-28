#include <cstdio>
#include <iostream>

using namespace std;

const int MAXN = 200;

int a[MAXN][MAXN];
int b[MAXN][MAXN];

int main() {
  int T; scanf("%d\n", &T);
  for (int tt = 1; tt <= T; ++tt) {
  	int n, m;
  	cin >> n >> m;
  	for (int i = 0; i < n; ++i) {
  		for (int j = 0; j < m; ++j) {
  			cin >> a[i][j];
  			b[i][j] = 200;
  		}
  	}

  	for (int i = 0; i < n; ++i) {
  		int c = a[i][0];
  		for (int j = 1; j < m; ++j) {
  			if (a[i][j] > c) c = a[i][j];
  		}
  		for (int j = 0; j < m; ++j) {
  			if (b[i][j] > c) b[i][j] = c;
  		}
  	}
  	for (int i = 0; i < m; ++i) {
  		int c = a[0][i];
  		for (int j = 1; j < n; ++j) {
  			if (a[j][i] > c) c = a[j][i];
  		}
  		for (int j = 0; j < n; ++j) {
  			if (b[j][i] > c) b[j][i] = c;
  		}
  	}
  	bool f = true;
  	for (int i = 0; i < n; ++i) {
  		for (int j = 0; j < m; ++j) {
  			if (b[i][j] != a[i][j]) {
  				f = false;
  				break;
  			}
  		}
  	}
    printf("Case #%d: ", tt);
    if (f) printf("YES");
    else printf("NO");
    putchar('\n');
  }
  return 0;
}

