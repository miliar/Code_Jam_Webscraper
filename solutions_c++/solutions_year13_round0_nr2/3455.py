#include <cstdio>
#include <algorithm>

using namespace std;

struct Pos {
    int r;
    int c;
    int s;
    friend bool operator < (Pos a, Pos b) {
        return a.s < b.s;
    }
};

int T, TT;
int n, m;
int a[100][100];
bool good[100][100];
Pos pos[10000];

int main() {
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        int i, j;
        scanf("%d %d", &n, &m);
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                scanf("%d", &a[i][j]);
                pos[i*m + j].r = i;
                pos[i*m+j].c = j;
                pos[i*m+j].s = a[i][j];
                good[i][j] = 0;
            }
        }
        sort(pos, pos+n*m);
        for (i = 0; i < n*m; i++) {
            if (good[pos[i].r][pos[i].c])
                continue;
            for (j = 0; j < m; j++)
                if (a[pos[i].r][j] > pos[i].s)
                    break;
            if (j == m) {
                for (j = 0; j < m; j++)
                    good[pos[i].r][j] = 1;
                continue;
            }
            for (j = 0; j < n; j++)
                if (a[j][pos[i].c] > pos[i].s)
                    break;
            if (j != n)
                break;
            for (j = 0; j < n; j++)
                good[pos[i].r][pos[i].c] = 1;
        }
        if (i != n*m)
            printf("NO\n");
        else
            printf("YES\n");
                        
    }
    
    
}