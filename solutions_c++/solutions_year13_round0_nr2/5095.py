#include <cstdio>
#include <algorithm>
using namespace std;

int map[200][200];
int row[200], col[200];
int rowmin[200], colmin[200];

void test() {
    int n,m;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) scanf("%d", &map[i][j]);
    for (int i = 0; i < n; i++) {
        col[i] = map[i][0];
        colmin[i] = map[i][0];
        for (int j = 0; j < m; j++) {
            if (map[i][j] != col[i]) col[i] = -1;
            colmin[i] = min(colmin[i], map[i][j]);
        }
    }
    for (int j = 0; j < m; j++) {
        row[j] = map[0][j];
        rowmin[j] = map[0][j];
        for (int i = 0; i < n; i++) {
            if (map[i][j] != row[j]) row[j] = -1;
            rowmin[j] = min(rowmin[j], map[i][j]);
        }
    }
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
        if (map[i][j] == rowmin[j] || map[i][j] == colmin[i]) {
            if (row[j] < 0 && col[i] < 0) {
//                printf("Proble w %d %d min %d %d", i, j, rowmin[j], colmin[i], row[j], col[j]);
                puts("NO");
                return;
            }
        }
    }
    puts("YES");
}

int main() {
    int t; scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i+1);
        test();
    }
    return 0;
}