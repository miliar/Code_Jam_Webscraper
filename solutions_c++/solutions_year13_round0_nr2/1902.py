#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("outB.txt", "w", stdout);

    int t, n, m, a[100][100], i, j, x, ans;
    int lin[100], col[100];
    scanf("%d", &t);
    for(x = 1; x <= t; x++) {
        scanf("%d %d", &n, &m);
        for(i = 0; i < n; i++) {
            for(j = 0; j < m; j++) {
                scanf("%d", &a[i][j]);
            }
        }

        for(i = 0; i < n; i++) {
            lin[i] = 0;
            for(j = 0; j < m; j++) {
                if(a[i][j] > lin[i]) lin [i] = a[i][j];
            }
        }

        for(j = 0; j < m; j++) {
            col[j] = 0;
            for(i = 0; i < n; i++) {
                if(a[i][j] > col[j]) col[j] = a[i][j];
            }
        }
        ans = 1;
        for(i = 0; i < n; i++) {
            for(j = 0; j < m; j++) {
                if(a[i][j] != min(lin[i], col[j])) {
                    ans = 0;
                    break;
                }
            }
        }
        printf("Case #%d: %s\n", x, ans? "YES" : "NO");
    }
    return 0;
}
