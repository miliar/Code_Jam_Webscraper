#include <bits/stdc++.h>
using namespace std;

const int N=1e2+10;
char s[N][N];
int r, c, vis[N][N], cc, cycle;
int dx[]={1, 0, 0, -1};
int dy[]={0, 1, -1, 0};

int solve(int u, int v) {
    if(s[u][v]=='^') return 3;
    if(s[u][v]=='>') return 1;
    if(s[u][v]=='v') return 0;
    return 2;
}

void conv(int k, int u, int v) {
    if(!k) s[u][v]='v';
    if(k==1) s[u][v]='>';
    if(k==2) s[u][v]='<';
    if(k==3) s[u][v]='^';
}

int in(int u, int v) { return u>=0 && u<r && v>=0 && v<c; }

void dfs(int u, int v) {
    cc++;
    vis[u][v]=1;
    int d=solve(u, v), i, j;
    for(i=u+dx[d], j=v+dy[d]; in(i, j) && s[i][j]=='.'; i+=dx[d], j+=dy[d]);
    if(!in(i, j)) return;
    if(!vis[i][j]) dfs(i, j);
    else cycle=1;
}

int main() {
    int t, T=1;
    scanf("%d", &t);
    while(t--) {
        int ok=1, ans=0;
        scanf("%d %d", &r, &c);
        memset(vis, 0, sizeof(vis));
        for(int i=0; i<r; i++) scanf("%s", s[i]);
        for(int i=0; i<r; i++) for(int j=0; j<c; j++) if(!vis[i][j] && s[i][j]!='.') {
            cc=cycle=0;
            dfs(i, j);
            if(cycle) continue;
            if(cc>1) ans++;
            else {
                int cnt=0;
                for(int k=0; k<4; k++) {
                    int ai, aj;
                    for(ai=i+dx[k], aj=j+dy[k]; in(ai, aj) && s[ai][aj]=='.'; ai+=dx[k], aj+=dy[k]);
                    if(!in(ai, aj)) cnt++;
                    else {
                        ans++;
                        conv(k, i, j);
                        break;
                    }
                }
                if(cnt==4) ok=0;
            }
        }
        printf("Case #%d: ", T++);
        if(!ok) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
