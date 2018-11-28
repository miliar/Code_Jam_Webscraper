#include<cstdio>
#include<algorithm>
using namespace std;
int cate,aux,bit,n,m,C,nr,maxi,X,pt,T,i,j,k,dp[12][4096],ap[1009][109],mask;
char a[109][109];
int vec(int i,int j)
{
    int nr=0;
    if(a[i-1][j]=='*') nr++;
    if(a[i+1][j]=='*') nr++;
    if(a[i][j+1]=='*') nr++;
    if(a[i][j-1]=='*') nr++;
    if(a[i-1][j+1]=='*') nr++;
    if(a[i+1][j+1]=='*') nr++;
    if(a[i-1][j-1]=='*') nr++;
    if(a[i+1][j-1]=='*') nr++;
    return nr;
}
void fill(int i,int j)
{
    if(i<1||j<1||i>n||j>m) return ;
    if(ap[i][j]==1||a[i][j]=='*') return ;
    ap[i][j]=1;
    if(vec(i,j)==0)
    {
        fill(i-1,j-1);
        fill(i-1,j);
        fill(i-1,j+1);
        fill(i,j-1);
        fill(i,j+1);
        fill(i+1,j-1);
        fill(i+1,j);
        fill(i+1,j+1);
    }
}
bool Ok()
{
    int i,j;
    for(i=1;i<=n+1;i++)
        for(j=1;j<=m+1;j++)
            ap[i][j]=0;
    fill(1,1);
    for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)
            if(ap[i][j]==0&&a[i][j]=='.') return 0;
    return 1;
}
int main()
{
//freopen("input","r",stdin);
//freopen("output","w",stdout);
scanf("%d",&T);
while(T)
{
    pt++;
    T--;
    printf("Case #%d:\n",pt);
    scanf("%d%d%d",&n,&m,&C);
    if(C+1==n*m)
    {
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
                a[i][j]='*';
        a[1][1]='c';
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
                printf("%c",a[i][j]);
            printf("\n");
        }
        continue;
    }
    if(n==1&&m==1) cate=1;
    else
    if(n>2&&m>2) cate=3;
    else cate=2;
    for(mask=0;mask<(1<<(n*m-cate));mask++)
    {
        for(i=1;i<=n+1;i++)
            for(j=1;j<=m+1;j++)
                a[i][j]='.';
        bit=aux=0;
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
            {
                if(i<=2&&j<=2) continue;
                if(mask&(1<<bit))
                {
                    a[i][j]='*';
                    aux++;
                }
                bit++;
            }
        if(aux!=C) continue;
        if(a[1][1]=='*') continue;
        if(Ok())
            break;
    }
    if(mask==(1<<(n*m-cate)))
    {
        printf("Impossible\n");
        continue;
    }
    a[1][1]='c';
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=m;j++)
            printf("%c",a[i][j]);
        printf("\n");
    }
}
return 0;
}
