#include <bits/stdc++.h>
#define MAX_N 110
using namespace std;

int mat[MAX_N][MAX_N], r, c, t, dir[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
bool done[MAX_N][MAX_N];

int main(void) {
    if (fopen("a-large.in","r")) {
        freopen("a-large.in","r",stdin);
        freopen("a-large.out","w",stdout);
    }
    cin >> t;
    for (int ii=1; ii<=t; ii++) {
        cin >> r >> c;
        for (int i=0; i<r; i++) {
            for (int j=0; j<c; j++) {
                char c;
                cin >> c;
                if (c=='<') mat[i][j]=3;
                else if (c=='v') mat[i][j]=0;
                else if (c=='>') mat[i][j]=1;
                else if (c=='^') mat[i][j]=2;
                else mat[i][j]=-1;
            }
        }
        int ans=0;
        bool poss=true;
        for (int i=0; i<r && poss; i++) {
            for (int j=0; j<c && poss; j++) {
                bool done=false;
                int tot=0;
                while (!done && mat[i][j]>=0 && tot<4) {
                    int nx=i+dir[mat[i][j]][0], ny=j+dir[mat[i][j]][1];
                    while (nx>=0 && ny>=0 && nx<r && ny<c && mat[nx][ny]==-1) {
                        nx+=dir[mat[i][j]][0];
                        ny+=dir[mat[i][j]][1];
                    }
                    if (nx>=0 && ny>=0 && nx<r && ny<c) {
                        if (tot>0) ans++;
                        done=true;
                    }
                    else {
                        mat[i][j]++;
                        mat[i][j]%=4;
                    }
                    tot++;
                }
                if (!done && mat[i][j]>=0) poss=false;
            }
        }
        cout << "Case #" << ii << ": ";
        if (poss) cout << ans << "\n";
        else cout << "IMPOSSIBLE\n";
    }
    return 0;
}
