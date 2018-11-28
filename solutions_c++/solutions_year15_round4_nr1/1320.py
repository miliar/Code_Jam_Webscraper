#include<bits/stdc++.h>
using namespace std;

#define LET(x, a)  __typeof(a) x(a)
#define TR(v, it) for(LET(it, v.begin()); it != v.end(); it++)
#define si(x) scanf("%d",&x)
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define INF 1000000000
#define MOD 1000000007
#define SET(x,y) memset(x,y,sizeof(x));
#define LL long long int
#define ULL unsigned LL
#define PII pair<int, int>

int main() {
    int t, n, m;
    int cs = 1;
    cin >> t;
    while (t--) {
        cin >> n >> m;
        string a[200];
        int row[200], col[200];
        memset(row, 0, sizeof(row));
        memset(col, 0, sizeof(col));
        int i, j, k;
        for (i = 0; i < n; i++) { 
            cin >> a[i];
            for (j = 0; j < m; j++) {
                if (a[i][j] != '.')
                    row[i] ++, col[j] ++;
            }
        }
        int ans = 0;
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                int dx = 0, dy = 0;
                if (a[i][j] == '.')
                    continue;
                else if (a[i][j] == '^')
                    dx = -1;
                else if (a[i][j] == '>')
                    dy = 1;
                else if (a[i][j] == '<')
                    dy = -1;
                else
                    dx = 1;
                if (row[i] == 1 && col[j] == 1) {
                    ans = -INF;
                }
                int cx = i + dx, cy = j + dy;
                while (cx >= 0 && cx < n && cy >= 0 && cy < m) {
                    if (a[cx][cy] != '.')
                        break;
                    cx += dx;
                    cy += dy;
                }
                if (!(cx >= 0 && cx < n && cy >= 0 && cy < m))
                    ans++;
            }
        }
        printf("Case #%d: ", cs++);
        if (ans >= 0) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}

