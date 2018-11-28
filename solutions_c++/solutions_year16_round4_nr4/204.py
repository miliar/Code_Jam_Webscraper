#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define FOR(i, x, y) for(int i = x; i < y; ++ i)
#define pb push_back
#define mk make_pair

const int N = 30;
int n;
bool a[N][N], b[N][N], use[N], arrive[N];
char s[N];
bool flag;

void dfs(int t){
    if (!flag) return;
    if (t == n)
        return;
    FOR(j,0,n) if (!arrive[j]){
        bool haveWork = false;
        arrive[j] = true;
        FOR(i,0,n) if (!use[i] && b[j][i]){
            haveWork = true;
            use[i] = true;
            dfs(t + 1);
            use[i] = false;
        }
        if (!haveWork){
            flag = false;
            return;
        }
        arrive[j] = false;
    }
}

bool check(){
    flag = true;
    FOR(i,0,n)
        arrive[i] = false, use[i] = false;
    dfs(0);
    return flag;
}

void solve() {
    scanf("%d",&n);
    FOR(i,0,n){
        scanf("%s",s);
        FOR(j,0,n)
            a[i][j] = s[j] == '1';
    }
    int m = n*n, ans = n*n;
    FOR(i, 0, 1<<m){
        int cost = 0;
        FOR(j,0,m){
            int x = j / n, y = j % n;
            if (i>>j&1){
                b[x][y] = 1;
                cost += !a[x][y];
            }else{
                b[x][y] = 0;
                if (a[x][y])
                    cost = ans + 1;
            }
        }
        // FOR(i,0,n){
        //     FOR(j,0,n)
        //         printf("%d ",  b[i][j]);
        //     puts("");
        // }
        // printf("%d %d\n", cost, ans);
        // puts("");
        if (cost < ans)
            if (check())
                ans = cost;
    }
    printf("%d\n", ans);
}


int main() {
#ifdef LOCAL
    freopen("in","r",stdin);
#endif
    int T, Case = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++Case);
        solve();
    }
    return 0;
}
