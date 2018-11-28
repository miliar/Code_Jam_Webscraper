#include <bits/stdc++.h>

using namespace std;

char s[111][111];
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int n, m;
string dir = "><v^";

bool inside(int x, int y){
    return (0 <= x && x < n && 0 <= y && y < m);
}

void solve(){
    scanf("%d%d", &n, &m);
    for(int i = 0; i < n; ++i) scanf("%s", s[i]);
    //for(int i = 0; i < n; ++i) puts(s[i]);
    int ans = 0;
    for(int i = 0; i < n; ++i)
    for(int j = 0; j < m; ++j){
        if (s[i][j] == '.') continue;
        if (ans == -1) break;
        bool met = false;
        bool rightway = false;
        for(int k = 0; k < 4; ++k){
            int u = i + dx[k];
            int v = j + dy[k];
            bool alive = false;
            while (inside(u, v)){
                if (s[u][v] != '.'){
                    alive = true;
                    break;
                }
                u += dx[k];
                v += dy[k];
            }
            if (alive){
                met = true;
                if (dir[k] == s[i][j]) rightway = true;
            }
        }
        if (met) ans += (1 - rightway);
        else ans = -1;
    }
    if (ans == -1) printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest;
    scanf("%d", &ntest);
    //fprintf(stderr, "%d\n", ntest);
    for(int test = 1; test <= ntest; ++test){
        printf("Case #%d: ", test);
        solve();
    }
    return 0;
}
