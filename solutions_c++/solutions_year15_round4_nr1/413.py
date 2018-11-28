#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>
using namespace std;

char a[200][200];
int b[200][200];

void solve() {
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%s", a[i]);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            b[i][j] = false;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] != '.') {
                b[i][j] |= 1;
                break;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = m - 1; j >= 0; j--) {
            if (a[i][j] != '.') {
                b[i][j] |= 2;
                break;
            }
        }
    }
    for (int j = 0; j < m; j++) {
        for (int i = 0; i < n; i++) {
            if (a[i][j] != '.') {
                b[i][j] |= 4;
                break;
            }
        }
    }
    for (int j = 0; j < m; j++) {
        for (int i = n - 1; i >= 0; i--) {
            if (a[i][j] != '.') {
                b[i][j] |= 8;
                break;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int c;
            if (a[i][j] == '<')
                c = 1;
            else if (a[i][j] == '>')
                c = 2;
            else if (a[i][j] == '^')
                c = 4;
            else if (a[i][j] == 'v')
                c = 8;
            if (a[i][j] != '.') {
                if (b[i][j] & c) {
                    ans++;
                }
                if (b[i][j] == 15) {
                    ans = 100000000;
                }
            }
        }
    }
    if (ans >= 100000000) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("%d\n", ans);
    }
}

int main() {
    freopen("E:/1.in", "r", stdin);
    freopen("E:/1.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
