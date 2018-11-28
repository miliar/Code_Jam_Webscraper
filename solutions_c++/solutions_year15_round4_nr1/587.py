#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define FORE(it,c) for(__typeof(c.begin())it=c.begin();it!=c.end();it++)
typedef pair<int,int> pii;

const int maxN = 111;

int m, n;
char a[maxN][maxN];
int mx[maxN], nx[maxN], my[maxN], ny[maxN];

void solve(){
    scanf("%d%d", &m, &n);
    memset(mx, 0x8F, sizeof mx);
    //printf("mx = %d\n", mx[0]);
    memset(my, 0x8F, sizeof my);
    memset(nx, 0x2F, sizeof nx);
    memset(ny, 0x2F, sizeof ny);
    for (int i = 1; i <= m; i++){
        scanf("%s", a[i] + 1);
        for (int j = 1; j <= n; j++){
            if (a[i][j] != '.'){
                mx[i] = max(mx[i], j);
                nx[i] = min(nx[i], j);
                my[j] = max(my[j], i);
                ny[j] = min(ny[j], i);
            }
        }
    }
    int res = 0;
    for (int i = 1; i <= m; i++)
    for (int j = 1; j <= n; j++) if (a[i][j] != '.'){
        //printf("%d, %d, %d, %d\n", mx[i], nx[i], my[j], ny[j]);
        if (mx[i] == nx[i] && my[j] == ny[j]){
            printf("IMPOSSIBLE\n"); return;
        }
        if (a[i][j] == '^')
            res += (ny[j] == i);
        else if (a[i][j] == 'v')
            res += (my[j] == i);
        else if (a[i][j] == '<')
            res += (nx[i] == j);
        else if (a[i][j] == '>')
            res += (mx[i] == j);
    }
    printf("%d\n", res);
}

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t; scanf("%d", &t);
    for (int test = 1; test <= t; test++){
        printf("Case #%d: ", test);
        solve();
    }
    return 0;
}
