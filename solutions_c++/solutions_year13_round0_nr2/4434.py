#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define N 110
int  n, m;
int L[N][N], R[N][N], U[N][N], D[N][N];
int maze[N][N];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1; cas <= T; cas ++){
        scanf("%d%d",&n,&m);
        for(int  i = 0; i <= n + 1; i ++)
            for(int j = 0; j <= m + 1; j++)
                L[i][j] = R[i][j] = U[i][j] = D[i][j] = 0;
        for(int  i = 1; i <= n; i++)
            for(int j = 1; j <= m; j++)
                scanf("%d",&maze[i][j]);
//        for(int  i = 1; i <= n; i++)
//        {
//            for(int j = 1; j <= m; j++)
//                cout << maze[i][j] <<" ";
//            cout << endl;
//        }
        for(int  i = 1; i <= n; i++)
            for(int j = 1; j <= m; j++)
                R[i][j] = max(R[i][j-1],maze[i][j]);

       for(int  i = 1; i <= n; i++)
            for(int j = m; j >= 1; j--)
                L[i][j] = max(L[i][j+1],maze[i][j]);
       for(int j = 1; j <= m; j++)
           for(int i = 1; i <= n; i++)
               D[i][j] = max(D[i-1][j],maze[i][j]);
       for(int j = 1; j <= m; j++)
           for(int i = n; i >= 1; i--)
               U[i][j] = max(U[i+1][j],maze[i][j]);
       int num = 0;
       for(int i = 1; i <= n; i++)
       {
           for(int j = 1; j <= m; j++)
               if((R[i][j-1] <= maze[i][j] && L[i][j+1] <= maze[i][j])||
                       (D[i-1][j] <= maze[i][j] && U[i+1][j] <= maze[i][j]))
                   num ++;
       }
       if(num  ==  n * m) printf("Case #%d: YES\n",cas);
       else printf("Case #%d: NO\n",cas);
           
    }
    return 0;
}