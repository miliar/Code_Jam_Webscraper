#include<cstdio>
#include<cstring>
using namespace std;
int n,m;
int ma[110][110];
int r[110],c[110];
void init()
{
    int i,j;
     for(i=0;i<n;i++)
    {
        for(j=1,r[i]=ma[i][0];j<m;j++)
        if(r[i]<ma[i][j])r[i]=ma[i][j];
    }
    for(j=0;j<m;j++)
    {
        for(i=1,c[j]=ma[0][j];i<n;i++)
        if(c[j]<ma[i][j])c[j]=ma[i][j];
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("textB.out","w",stdout);
    int T,ca=1;
    int i,j;
    int flag;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        scanf("%d",&ma[i][j]);
        printf("Case #%d: ",ca++);
        if(n==1||m==1){puts("YES");continue;}
        init();
        for(i=0,flag=0;i<n;i++){
            for(j=0;j<m;j++)
            if(ma[i][j]<r[i]&&ma[i][j]<c[j]){flag=1;break;}
            if(flag)break;
        }
        if(flag)puts("NO");
        else puts("YES");
    }
    return 0;
}
