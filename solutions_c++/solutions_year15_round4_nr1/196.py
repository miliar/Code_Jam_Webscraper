#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int dx[] = {-1,0,1,0};
const int dy[] = {0,1,0,-1};
int n,m,a[105][105];

bool go(int x,int y, int k) {
    int xx = x + dx[k], yy = y + dy[k];
    while (xx >= 1&&xx<=n&&yy>=1&&yy<=m) {
        if (a[xx][yy] != -1) return false;
        xx += dx[k], yy += dy[k];
    }
    return true;
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin >> T;
    for (int o = 1; o <= T; o++) {
        memset(a,0,sizeof a);
        cin >> n >> m;
        for (int i = 1; i <= n; i++) {
            string s;
            cin >> s;
            for (int j = 1; j <= m; j++) {
                if (s[j-1]=='.') a[i][j]=-1;
                if (s[j-1]=='^') a[i][j]=0;
                if (s[j-1]=='>') a[i][j]=1;
                if (s[j-1]=='v') a[i][j]=2;
                if (s[j-1]=='<') a[i][j]=3;
            }
        }
        bool impo = false;
        int ans = 0;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) {
                if (a[i][j]==-1) continue;
                int num = 0;
                for (int k = 0; k < 4; k++) {
                    bool out = go(i,j,k);
                    if (out) num++;
                    if (out && a[i][j]==k) ans++;
                }
                if (num==4)impo = true;
            }
        if (impo) printf("Case #%d: IMPOSSIBLE\n",o);
        else printf("Case #%d: %d\n",o,ans);
    }
}
