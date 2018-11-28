#include<cstdio>
#include<cstring>
#define N 110

int a[N][N];
bool u[N][N];

int main(){
    int cas,tt=0;
    int n,m,i,j,k,l,sum,nn;
    bool flag;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&cas);
    while(cas--){
        scanf("%d%d",&n,&m);
        nn=0;
        memset(u,0,sizeof(u));
        for(i=1;i<=n;++i)
            for(j=1;j<=m;++j){scanf("%d",&a[i][j]);if(a[i][j]>nn)nn=a[i][j];}
        flag=true;
        for(k=1;k<=nn;++k){
            for(i=1;i<=n;++i)
                for(j=1;j<=m;++j)if(a[i][j]==k){
                    for(l=1;l<=n;++l)if(a[l][j]!=k&&!u[l][j])break;
                    if(l>n)for(l=1;l<=n;++l)u[l][j]=1;
                    for(l=1;l<=m;++l)if(a[i][l]!=k&&!u[i][l])break;
                    if(l>m)for(l=1;l<=m;++l)u[i][l]=1;
                }
        }
        for(i=1;i<=n;++i)for(j=1;j<=m;++j)flag=flag&u[i][j];
        printf("Case #%d: ",++tt);
        if(flag)puts("YES");else puts("NO");
    }
    return 0;
}
