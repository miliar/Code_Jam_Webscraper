#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
struct abc{
    char s[110];
    bool operator < (const abc &a) const{
        return strcmp(s, a.s) < 0;
    }
}c[1010];
int b[1010][1010];
int ans, tot, n, m;
int last[4];
void dfs(int x, int cur){
    if (x == n){
        for (int i = 0; i < m; i++) if (last[i] == 0) return;
        if (cur > ans){ ans = cur; tot = 0; }
        if (cur == ans) tot++;
        return;
    }
    int t;
    for (int i = 0; i < m; i++){
        t = last[i];
        last[i] = x;
        dfs(x + 1, cur + b[t][x]);
        last[i] = t;
    }
}
int main(){
    int T, ri = 1, i, j, k;
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++) scanf("%s", c[i].s);
        c[n].s[0] = 0;
        n++;
        sort(c, c + n);
        for (i = 0; i < n; i++){
            for (j = i + 1; j < n; j++){
                for (k = 0; c[i].s[k] && c[i].s[k] == c[j].s[k]; k++);
                b[i][j] = strlen(c[j].s) - k;
            }
        }
        ans = 0;
        memset(last, 0, sizeof(last));
        dfs(1, 0);
        printf("Case #%d: %d %d\n", ri++, ans + m, tot);
    }
    return 0;
}
