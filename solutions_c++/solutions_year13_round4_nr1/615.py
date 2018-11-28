#include <map>
#include <cmath>
#include <queue>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
const long long MOD = 1000002013;
bool v[10005];
long long n, m, cnt;
struct Pnode{
    long long x, y, c;
} p[10005], ed[10005], st[10005];

long long f(long long x){
    if (!x) return 0;
    return ((2 * (long long)n + 1 - x) * x / (long long)2) % MOD;
}

int cmp(Pnode a, Pnode b){return a.x < b.x;}
void dfs(int x){
    v[x] = 1;
    st[++cnt].x = p[x].x; st[cnt].y = p[x].c;
    ed[cnt].x = p[x].y; ed[cnt].y = p[x].c;
    for (int y = 1; y <= m; y++)
    if (!v[y] && !(p[x].x > p[y].y || p[x].y < p[y].x)) dfs(y);
}
int main(){
    int CAS, cas, i, op, j, k;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &CAS);
    for (cas = 1; cas <= CAS; cas++){
        scanf("%lld%lld", &n, &m);
        long long ans = 0;
        for (i = 1; i <= m; i++){
            scanf("%lld%lld%lld", &p[i].x, &p[i].y, &p[i].c);
            ans += f(p[i].y - p[i].x) * p[i].c;
        }
        memset(v, 0, sizeof(v));
        for (i = 1; i <= m; i++)
        if (!v[i]){
            cnt = 0;
            dfs(i);
            sort(st + 1, st + cnt + 1, cmp);
            sort(ed + 1, ed + cnt + 1, cmp);
            op = cnt;
            for (j = cnt; j >= 1; j--){
                while (op > 1 && ed[op - 1].x >= st[j].x) op--;
                int k = op;
                while (st[j].y){
                    long long t = min(st[j].y, ed[k].y);
                    ans -= f(ed[k].x - st[j].x) * t;
                    ed[k++].y -= t; st[j].y -= t;
                }
            }
        }
        printf("Case #%d: %lld\n", cas, ans);
    }
}
