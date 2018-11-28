#include <cmath>
#include <ctime>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <queue>

using namespace std;

const int MAX = 100;

int polje[MAX][MAX], red[MAX], stupac[MAX];

int main() {
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++) {
        int n, m;
        scanf ("%d %d", &n, &m);
        for (int i = 0; i < MAX; i++) {
            red[i] = stupac[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf ("%d", &polje[i][j]);
                red[i] = max (red[i], polje[i][j]);
                stupac[j] = max (stupac[j], polje[i][j]);
            }
        }
        int pattern = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!(polje[i][j] == red[i] || polje[i][j] == stupac[j])) {
                    pattern = 0;
                }
            }
        }
        printf ("Case #%d: ", t);
        if (pattern) {
            printf ("YES\n");
        } else {
            printf ("NO\n");
        }
	}
	return 0;
}
