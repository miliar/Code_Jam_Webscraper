#include <iostream>
#include <cstdio>
#include <cstring>
#define N 110
#define inf 2000000
#define rep(i,l,r) for (int i = l;i <= r;i ++)
#define drep(i,r,l) for (int i = r;i >= l;i --)
using namespace std;

int row[N],col[N],n,m,map[N][N];

int main (){
    int cas,c = 0;
    scanf ("%d",&cas);
    while (cas --){
        memset (row,0,sizeof(row));
        memset (col,0,sizeof(col));
        scanf ("%d%d",&n,&m);
        rep(i,1,n){
            rep(j,1,m){
                scanf ("%d",&map[i][j]);
                row[i] = max(row[i],map[i][j]);
                col[j] = max (col[j],map[i][j]);
            }
        }
        bool flag = true;
        rep(i,1,n){
            if (!flag) break;
            rep (j,1,m){
                if (row[i] > map[i][j] && col[j] > map[i][j]){
                    flag = false;
                    break;
                }
            }
        }
        printf ("Case #%d: ",++ c);
        if (flag) puts("YES");
        else puts("NO");
    }
    return 0;
}