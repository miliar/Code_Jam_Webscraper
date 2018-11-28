#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

int main(void) {
    freopen("B-large.in", "r", stdin);
    freopen("dataout.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        int lawn[111][111], ans = 1;
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%d", &lawn[i][j]);
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int mark = 0;
                for (int k = 0; k < n; k++) {
                    if (lawn[k][j] > lawn[i][j]) {
                        mark++;
                        break;
                    }
                }
                for (int k = 0; k < m; k++) {
                    if (lawn[i][k] > lawn[i][j]) {
                        mark++;
                        break;
                    }
                }
                if (mark == 2) {
                    ans = 0;
                    break;
                }
            }
            if (!ans) {
                break;
            }
        }
        printf("Case #%d: %s\n", cases, (ans) ? "YES" : "NO");
    }
    return 0;
}
