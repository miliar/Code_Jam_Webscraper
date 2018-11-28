#include <bits/stdc++.h>

using namespace std;

typedef pair<int ,int> ii;

int T, C=1;

int n, m;
int visited[128][128], TT;
vector<ii> adj[128][128];
int v[128];
ii pos[128];
int rot[128][128];
char M[128][128];


bool alcanca(int x1, int y1, int x2, int y2) {
    if (x1 == x2 and y1 == y2)
        return true;
    visited[x1][y1] = TT;
    for (int i=0;i<(int)adj[x1][y1].size();i++) {
        int nx = adj[x1][y1][i].first;
        int ny = adj[x1][y1][i].second;
        if (visited[nx][ny] != TT)
            if (alcanca(nx,ny,x2,y2)) return true;
    }
    return false;
}

bool alcancaoutro(int x1, int y1, int xo, int yo, int x2, int y2) {
    visited[x1][y1] = TT;
    if (ii(x1,y1) != ii(xo, yo) and ii(x1,y1) != ii(x2,y2) and rot[x1][y1] != -1)
        return true;
    for (int i=0;i<(int)adj[x1][y1].size();i++) {
        int nx = adj[x1][y1][i].first;
        int ny = adj[x1][y1][i].second;
        if (visited[nx][ny] != TT)
            if (alcancaoutro(nx,ny,xo,yo,x2,y2)) return true;
    }
    return false;
}

bool ok() {
    for(int i=0;i<2*(n+m);i+=2) {
        TT++;
        if (!alcanca(pos[v[i]].first,pos[v[i]].second,
                     pos[v[i^1]].first, pos[v[i^1]].second)) {
                return false;
        }
        TT++;
        if (alcancaoutro(pos[v[i]].first,pos[v[i]].second,
                     pos[v[i]].first,pos[v[i]].second,
                     pos[v[i^1]].first, pos[v[i^1]].second))
            return false;
    }
    return true;

}

bool vai(int i, int j) {
    if (i==n)
        return ok();
    if (j==m) return vai(i+1,0);

    M[i][j] = '/';
    adj[2*i][2*j+1].push_back(ii(2*i+1,2*j));
    adj[2*i+1][2*j].push_back(ii(2*i,2*j+1));
    adj[2*i+1][2*j+2].push_back(ii(2*i+2, 2*j+1));
    adj[2*i+2][2*j+1].push_back(ii(2*i+1, 2*j+2));
    if (vai(i,j+1)) return true;
    adj[2*i][2*j+1].pop_back();
    adj[2*i+1][2*j].pop_back();
    adj[2*i+1][2*j+2].pop_back();
    adj[2*i+2][2*j+1].pop_back();
    M[i][j] = '\\';
    adj[2*i][2*j+1].push_back(ii(2*i+1, 2*j+2));
    adj[2*i+1][2*j+2].push_back(ii(2*i, 2*j+1));
    adj[2*i+1][2*j].push_back(ii(2*i+2, 2*j+1));
    adj[2*i+2][2*j+1].push_back(ii(2*i+1, 2*j));
    if (vai(i,j+1)) return true;
    adj[2*i][2*j+1].pop_back();
    adj[2*i+1][2*j].pop_back();
    adj[2*i+1][2*j+2].pop_back();
    adj[2*i+2][2*j+1].pop_back();
    return false;
}

int main() {

    memset(visited,0,sizeof(visited));
    TT=0;
    for(scanf("%d",&T);T--;) {
        printf("Case #%d:\n",C++);
        scanf("%d %d",&n,&m);
        for (int i=0;i<2*(n+m);i++)
            scanf("%d",v+i);
        memset(rot,0xff,sizeof(rot));
        int tt=1;
        for (int j=1;j<=2*m-1;j+=2)
            rot[0][j] = tt++;
        for (int i=1;i<=2*n-1;i+=2)
            rot[i][2*m] = tt++;
        for (int j=2*m-1;j>=1;j-=2)
            rot[2*n][j] = tt++;
        for (int i=2*n-1;i>=1;i-=2)
            rot[i][0] = tt++;

        for (int i=0;i<=2*n;i++)
            for (int j=0;j<=2*m;j++) {
                adj[i][j].clear();
                if (rot[i][j] != -1)
                    pos[ rot[i][j] ] = ii(i,j);
            }
        if (!vai(0,0))
            printf("IMPOSSIBLE\n");
        else {
            for (int i=0;i<n;i++) {
                for (int j=0;j<m;j++)
                    printf("%c",M[i][j]);
                printf("\n");
            }
        }
    }

    return 0;
}
