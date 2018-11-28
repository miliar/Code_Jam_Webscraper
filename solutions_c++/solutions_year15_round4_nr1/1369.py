#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 1000000000
#define UNIQUE(x) (x).resize(distance((x).begin(),unique(all(x))))
#define die -1
#define live 1
#define idk 0;
#define SET(x) memset((x),0,sizeof(x))
int state[105][105],r,c;
char grid[105][105];
int jright[105][105],jleft[105][105],jup[105][105],jdown[105][105];

int main() {
    int tc;
    scanf("%d",&tc);
    for (int kk=0;kk<tc;kk++) {
        SET(state);
        SET(jleft);
        SET(jright);
        SET(jup);
        SET(jdown);
        SET(grid);
        scanf("%d%d",&r,&c);
        for (int i=0;i<r;i++) {
            scanf("%s",grid[i]);
        }
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                if (i==0) jup[i][j]=-INF;
                else {
                    if (grid[i-1][j]=='.') jup[i][j]=jup[i-1][j]+1;
                    else jup[i][j]=1;
                }
                if (j==0) jleft[i][j]=-INF;
                else {
                    if (grid[i][j-1]=='.') jleft[i][j]=jleft[i][j-1]+1;
                    else jleft[i][j]=1;
                }
            }
        }
        for (int i=r-1;i>=0;i--) {
            for (int j=c-1;j>=0;j--) {
                if (i==r-1) jdown[i][j]=-INF;
                else {
                    if (grid[i+1][j]=='.') jdown[i][j]=jdown[i+1][j]+1;
                    else jdown[i][j]=1;
                }
                if (j==c-1) jright[i][j]=-INF;
                else {
                    if (grid[i][j+1]=='.') jright[i][j]=jright[i][j+1]+1;
                    else jright[i][j]=1;
                }
            }
        }
        /*
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                if (grid[i][j]=='.') continue;
                if (state[i][j]==idk) {
                    SET(visited);
                    dfs(i,j);
                }
            }
        }
        */
        int ans=0;
        bool pos=1;
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                if (grid[i][j]=='.') continue;
                if (grid[i][j]=='>') {
                    if (jright[i][j]<0) ans++;
                } else if (grid[i][j]=='<') {
                    if (jleft[i][j]<0) ans++;
                } else if (grid[i][j]=='v') {
                    if (jdown[i][j]<0) ans++;
                } else if (grid[i][j]=='^') {
                    if (jup[i][j]<0) ans++;
                }
                if (jright[i][j]<0&&jleft[i][j]<0&&jdown[i][j]<0&&jup[i][j]<0) pos=0;
            }
        }
        if (!pos) printf("Case #%d: IMPOSSIBLE\n", kk+1);
        else printf("Case #%d: %d\n",kk+1, ans);
    }
}