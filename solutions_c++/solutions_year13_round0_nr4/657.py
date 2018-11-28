#include <cstdio>
#include <cstdlib>
#include <cstring>
int t,k[25],n,c[25][205],s[25],pre[1048576],log[1048576],p[25];
void print(int x)
{
    if(pre[x]) {print(pre[x]); printf(" %d",log[x^pre[x]]+1);}
}
bool go(int x)
{
    /*
    memcpy(tc,c[0],sizeof(c[0]));
    for(int i=0;i<n;++i) if(!((x>>i)&1))
    {
        --tc[s[i+1]];
        for(int j=1;j<=40;++j) tc[j]+=c[i+1][j];
    }
    */
    for(int i=0;i<n;++i) if((x>>i)&1&&!pre[x^(1<<i)]&&c[0][s[i+1]])
    {
        pre[x^(1<<i)]=x; --c[0][s[i+1]];
        for(int j=0;j<k[i+1];++j) ++c[0][c[i+1][j]];
        go(x^(1<<i)); ++c[0][s[i+1]];
        for(int j=0;j<k[i+1];++j) --c[0][c[i+1][j]];
    }
}
int main()
{
    freopen("in4","r",stdin);
    freopen("out4","w",stdout);
    scanf("%d",&t);
    p[0]=1; for(int i=1;i<25;++i) p[i]=p[i-1]<<1;
    for(int i=1;i<1048576;++i) log[i]=log[i-1]+(i==p[log[i-1]+1]);
    for(int I=1;I<=t;++I)
    {
        scanf("%d%d",&k[0],&n); memset(c,0,sizeof(c)); int x;
        for(int i=0;i<k[0];++i) {scanf("%d",&x); ++c[0][x];}
        for(int i=1;i<=n;++i)
        {
            scanf("%d%d",&s[i],&k[i]);
            for(int j=0;j<k[i];++j) scanf("%d",&c[i][j]);
        }
        memset(pre,0,sizeof(pre)); go((1<<n)-1);
        if(pre[0]) {printf("Case #%d:",I); print(0); printf("\n");}
        else printf("Case #%d: IMPOSSIBLE\n",I);
    }
    return 0;
}
