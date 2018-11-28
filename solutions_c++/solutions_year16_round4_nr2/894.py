#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int MAXN = 210;
int n, m;
double p[MAXN];
double f[MAXN][MAXN];
double now[MAXN];
double ans;

void init()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) scanf("%lf", &p[i]);
}

void update()
{
    memset(f, 0, sizeof(f));
    f[0][0] = 1;
    for (int i = 0; i < m; ++i){
        for (int j = 0; j <= i; ++j){
            f[i + 1][j + 1] += f[i][j] * now[i]; 
            f[i + 1][j]     += f[i][j] * (1 - now[i]);
        }
    }
    ans = max(ans, f[m][m / 2]);
    return;
}

void dfs(int i, int d)
{
    if (d == m) { update(); return; }
    if (n - i + d < m) return;
    for (int j = i; j < n; ++j) {
        now[d] = p[j];
        dfs(j + 1, d + 1);
    }
}

int main()
{
    int dat;
    scanf("%d", &dat);
    for (int cas = 1; cas <= dat; ++cas) {
        init();
        ans = 0;
        dfs(0, 0);
        printf("Case #%d: %.20f\n", cas, ans);
    }
}
