#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int G[105][105],Z[105][105];
int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
int n,m,ch[255];
int geto(int x,int y,int d){
    x+=dx[d];
    y+=dy[d];
    while(1){
        if(x<1||x>n||y<1||y>m)return 0;
        if(Z[x][y])return Z[x][y];
        x+=dx[d];
        y+=dy[d];
    }
}
int main(){
    int i,j,k,l,T;
    memset(ch,0xff,sizeof(ch));
    ch['>']=0;
    ch['v']=1;
    ch['<']=2;
    ch['^']=3;
    scanf("%d",&T);
    for(int tt=1;tt<=T;tt++){
        int noa=0;
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++){
                char cc;
                cc=getchar();
                while(cc!='.'&&cc!='>'&&cc!='v'&&cc!='<'&&cc!='^')cc=getchar();
                G[i][j]=ch[cc];
                Z[i][j]=0;
            }
        int gs=0,ans=0;
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
                if(G[i][j]>=0)Z[i][j]=++gs;
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
                if(Z[i][j]){
                    k=geto(i,j,G[i][j]);
                    int fl=0;
                    for(int p=0;p<4;p++)if(geto(i,j,p)!=0)fl=1;
                    if(!fl)noa=1;
                    if(!k)ans++;
                }
        printf("Case #%d: ",tt);
        if(noa)printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}
