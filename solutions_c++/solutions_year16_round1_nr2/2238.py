#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int T, t, i, j, k, n;
vector< vector<int> > a;
bool wasr[50], wasc[50];
int p[50][50];
int cnt[50][50];
bool done;

void go(int k) {
    int i, j, q;
    if (k == 2 * n - 1) {
        done = true;
        return;
    }
    if (!wasr[0]) {
        wasr[0] = true;
        for (i = 0; i < n; i++) { p[0][i] = a[k][i]; cnt[0][i] = 1; }
        go(k+1);
        return;
    }
    for (i = 0; i < n; i++) {
        if (wasr[i]) continue;
        for (j = 0; j < n; j++) {
            if (p[i][j] != 0 && p[i][j] != a[k][j]) break;
            if (p[i-1][j] >= a[k][j]) break;
        }
        if (j < n) continue;
        for (q = 0; q < i; q++) if (p[q][0] >= a[k][0]) break;
        if (q < i) break;

        for (j = 0; j < n; j++) {
            p[i][j] = a[k][j];
            cnt[i][j]++;
        }
        wasr[i] = true;
        go(k+1);
        if (!done) {
            wasr[i] = false;
            for (j = 0; j < n; j++) {
                cnt[i][j]--;
                if (cnt[i][j] == 0) p[i][j] = 0;
            }
        }
        break;
    }
    if (done) return;
    for (i = 0; i < n; i++) {
        if (wasc[i]) continue;
        if (p[0][i] == a[k][0]) {
            for (j = 0; j < n; j++) {
                if (p[j][i] != 0 && p[j][i] != a[k][j]) break;
                if (i > 0 && p[j][i-1] >= a[k][j]) break;
            }
            if (j < n) break;
            for (j = 0; j < n; j++) {
                p[j][i] = a[k][j];
                cnt[j][i]++;
            }
            wasc[i] = true;
            go(k+1);
            if (!done) {
                wasc[i] = false;
                for (j = 0; j < n; j++) {
                    cnt[j][i]--;
                    if (cnt[j][i] == 0) p[j][i] = 0;
                }
            }
            break;
        }
    }

}

int main() {
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        printf("Case #%d:", t);
        scanf("%d", &n);
        a.clear();
        for (i = 0; i < 2 * n - 1; i++) {
            vector<int> v;
            for (j = 0; j < n; j++) { scanf("%d", &k); v.push_back(k); }
            a.push_back(v);
        }
        sort(a.begin(), a.end());
        for (i = 0; i < n; i++) {
            wasr[i] = wasc[i] = false;
            for(j = 0; j < n; j++) cnt[i][j] = p[i][j] = 0;
        }
        done = false;
        go(0);
        /*
        printf("%d\n", n);
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                printf("%d ", p[i][j]);
            }
            printf("\n");
        }
        // */
        for (i = 0; i < n; i++) {
            if (!wasr[i]) for (j = 0; j < n; j++) printf(" %d", p[i][j]);
            if (!wasc[i]) for (j = 0; j < n; j++) printf(" %d", p[j][i]);
        }
        printf("\n");
    }
    return 0;
}
