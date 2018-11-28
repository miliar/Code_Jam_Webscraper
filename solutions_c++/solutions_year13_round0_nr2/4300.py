#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

typedef double db;

const double eps = 1e-8;
const double PI = acos(-1.0);
const int N = 110;

int a[N][N], r[N], c[N];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int _, cnt = 1;
    scanf("%d", &_);
    while(_--) {
        int n, m;
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) scanf("%d", &a[i][j]);
        }
        memset(r, 0, sizeof(r));
        memset(c, 0, sizeof(c));
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) r[i] = max(r[i], a[i][j]);
        }
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) c[i] = max(c[i], a[j][i]);
        }
        int flag = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if( min(r[i], c[j]) != a[i][j] ) flag = 1;
            }
        }
        printf("Case #%d: ", cnt++);
        if(flag == 0) puts("YES");
        else puts("NO");
    }

    return 0;
}
