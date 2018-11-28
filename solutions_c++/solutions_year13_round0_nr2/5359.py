#include <cstdio>

int n, m;
int a[200][200];
int rmax[200], rmin[200], cmax[200], cmin[200];

bool pos() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == rmin[i] && a[i][j] < rmax[i]) {
                if (a[i][j] < cmax[j]) return false;
            }
            if (a[i][j] == cmin[j] && a[i][j] < cmax[j]) {
                if (a[i][j] < rmax[i]) return false;
            }
        }
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%d", &a[i][j]);
            }
        }
        for (int i = 0; i < n; i++) {
            rmax[i] = 1;
            rmin[i] = 100;
        }
        for (int j = 0; j < m; j++) {
            cmax[j] = 1;
            cmin[j] = 100;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a[i][j] > rmax[i]) rmax[i] = a[i][j];
                if (a[i][j] < rmin[i]) rmin[i] = a[i][j];
                if (a[i][j] > cmax[j]) cmax[j] = a[i][j];
                if (a[i][j] < cmin[j]) cmin[j] = a[i][j];
            }
        }
        printf("Case #%d: ", tc);
        if (pos()) printf("YES\n");
        else printf("NO\n");
    }
    
    return 0;
}
