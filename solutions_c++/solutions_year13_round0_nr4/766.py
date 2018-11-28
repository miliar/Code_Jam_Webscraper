#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int k, n, x, i, j, c[205], p[25][45], t[25], ans[25], v[2000000], found;

void dfs(int k, int x){
    if (v[x]) return;
    v[x] = 1;
    if (k > n){
        found = 1;
        return;
    }
    for (int i = 1; i <= n; i++)
    if (c[t[i]]){
        c[t[i]]--;
        int tmp = t[i];
        t[i] = 0;
        for (int j = 1; j <= p[i][0]; j++) c[p[i][j]]++;
        ans[k] = i;
        dfs(k + 1, x + (1 << (i - 1)));
        if (found) return;
        for (int j = 1; j <= p[i][0]; j++) c[p[i][j]]--;
        t[i] = tmp;
        c[t[i]]++;
    }
}
int main(){
    int cas, CAS;
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d", &CAS);
    for (cas = 1; cas <= CAS; cas++){
        scanf("%d%d", &k, &n);
        memset(c, 0, sizeof(c));
        for (i = 1; i <= k; i++){
            scanf("%d", &x);
            c[x]++;
        }
        for (i = 1; i <= n; i++){
            scanf("%d%d", &t[i], &p[i][0]);
            for (j = 1; j <= p[i][0]; j++) scanf("%d", &p[i][j]);
        }
        found = 0;
        memset(v, 0, sizeof(v));
        dfs(1, 0);
        if (!found) printf("Case #%d: IMPOSSIBLE\n", cas); else{
            printf("Case #%d: ", cas);
            for (i = 1; i < n; i++) printf("%d ", ans[i]); printf("%d\n", ans[i]);
        }
    }
}
