#include <stdio.h>
#include <string.h>
int n,m;
int c[7][7];
int g[7][7];
int u[7][7],uid;
int sv[7][7][26][7][7];
void fill(int x,int y){
    if(u[x][y]==uid || g[x][y]) return;
    u[x][y] = uid;
    fill(x-1,y-1);
    fill(x+1,y-1);
    fill(x-1,y+1);
    fill(x+1,y+1);
    fill(x,y-1);
    fill(x,y+1);
    fill(x-1,y);
    fill(x+1,y);
}
void dfs(int x,int y,int d){
    if(x==n+1){
        int flag = 1;
        int ff = 0;
        int sx,sy;
        uid++;
        for( int i=1; i<=n; i++ ){
            for( int j=1; j<=m; j++ ){
                if(g[i][j]==0){
                    if(u[i][j]!=uid){
                        if(ff){
                            flag = 0;
                            goto out;
                        }
                        ff = 1;
                        fill(i,j);
                        sx = i;
                        sy = j;
                    }
                }else if(c[i][j]==0){
                    if(g[i-1][j]&&g[i+1][j]&&g[i][j-1]&&g[i][j+1]&&
                            g[i-1][j-1]&&g[i-1][j+1]&&g[i+1][j-1]&&g[i+1][j+1]){
                        flag = 0;
                        goto out;
                    }
                }
            }
        }
out:
        if(flag){
            if(sv[n][m][d][0][0]) return;
            sv[n][m][d][0][0] = 1;
            for( int i=1; i<=n; i++ ){
                for( int j=1; j<=m; j++ ){
                    sv[n][m][d][i][j] = c[i][j];
                }
            }
            sv[n][m][d][sx][sy] = 2;
        }
    }else{
        if(y==m){
            dfs(x+1,1,d);
            c[x][y] = 1;
            g[x][y]++; g[x][y-1]++; g[x][y+1]++;
            g[x-1][y]++; g[x-1][y-1]++; g[x-1][y+1]++;
            g[x+1][y]++; g[x+1][y-1]++; g[x+1][y+1]++;
            dfs(x+1,1,d+1);
            c[x][y] = 0;
            g[x][y]--; g[x][y-1]--; g[x][y+1]--;
            g[x-1][y]--; g[x-1][y-1]--; g[x-1][y+1]--;
            g[x+1][y]--; g[x+1][y-1]--; g[x+1][y+1]--;
        }else{
            dfs(x,y+1,d);
            g[x][y]++; g[x][y-1]++; g[x][y+1]++;
            g[x-1][y]++; g[x-1][y-1]++; g[x-1][y+1]++;
            g[x+1][y]++; g[x+1][y-1]++; g[x+1][y+1]++;
            c[x][y] = 1;
            dfs(x,y+1,d+1);
            c[x][y] = 0;
            g[x][y]--; g[x][y-1]--; g[x][y+1]--;
            g[x-1][y]--; g[x-1][y-1]--; g[x-1][y+1]--;
            g[x+1][y]--; g[x+1][y-1]--; g[x+1][y+1]--;
        }
    }
}
int main(){
    int TT;
    int r;
    for( n=1; n<=5; n++ ){
        for( m=1; m<=5; m++ ){
            memset(g,0,sizeof(g));
            for( int i=0; i<=n+1; i++ ){
                g[i][0] = g[i][m+1] = 100;
            }
            for( int i=0; i<=m+1; i++ ){
                g[0][i] = g[n+1][i] = 100;
            }
            dfs(1,1,0);
        }
    }
    scanf("%d",&TT);
    for( int tt=1;tt<=TT; tt++ )
    {
        scanf("%d %d %d",&n,&m,&r);
        printf("Case #%d:\n",tt);
        if(r==n*m-1){
            for( int i=1; i<=n; i++ ){
                for( int j=1; j<=m; j++ ){
                    printf("%c",(i==1&&j==1)?'c':'*');
                }
                puts("");
            }
        }else if(!sv[n][m][r][0][0]){
            puts("Impossible");
        }else{
            for( int i=1; i<=n; i++ ){
                for( int j=1; j<=m; j++ ){
                    if(sv[n][m][r][i][j]==0){
                        printf(".");
                    }else if(sv[n][m][r][i][j]==1){
                        printf("*");
                    }else{
                        printf("c");
                    }
                }
                puts("");
            }
        }
    }
    return 0;
}
