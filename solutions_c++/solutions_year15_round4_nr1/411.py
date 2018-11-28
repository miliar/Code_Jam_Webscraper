#include<bits/stdc++.h>
using namespace std;
const int maxn=100+10 ;

char G[maxn][maxn] ;
int x[maxn],y[maxn] ;
int n,m ;
int check(int x0,int y0)
{
    if(x[x0]==1 && y[y0]==1) return -1 ;
    int dx,dy ;
    if(G[x0][y0]=='^') dx=-1 , dy=0 ;
    if(G[x0][y0]=='>') dx=0 , dy=1 ;
    if(G[x0][y0]=='<') dx=0 , dy=-1 ;
    if(G[x0][y0]=='v') dx=1 , dy=0 ;
    for(int i=1;;i++)
    {
        int nx=x0+i*dx , ny=y0+i*dy ;
        if(nx<0 || nx>=n || ny<0 || ny>=m) return 1 ;
        if(G[nx][ny]!='.') return 0 ;
    }
}

main()
{
    if(fopen("A.in","r"))
        freopen("A.in","r",stdin) ,
        freopen("A.out","w",stdout) ;
    int T,tc=0 ; scanf("%d",&T) ;
    while(T--)
    {
        printf("Case #%d: ",++tc) ;
        scanf("%d%d",&n,&m) ;
        for(int i=0;i<n;i++) scanf("%s",G[i]) ;
        memset(x,0,sizeof(x)) ; memset(y,0,sizeof(y)) ;
        for(int i=0;i<n;i++) for(int j=0;j<m;j++)
            if(G[i][j]!='.') x[i]++ , y[j]++ ;

        int ans=0,ok=0 ;
        for(int i=0;!ok && i<n;i++) for(int j=0;j<m;j++)
            if(G[i][j]!='.')
        {
            int tmp=check(i,j) ;
            if(tmp==-1){printf("IMPOSSIBLE\n") ; ok=1 ; break ;}
            else ans+=tmp ;
        }
        if(!ok) printf("%d\n",ans) ;
    }
}
