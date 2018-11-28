#include<cstdio>
#include<cstring>
using namespace std;
int map[105][105],a[105],b[105];
int main()
{
    int t,i,j,n,m,tp,ok,cas=0;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    while(t--){
       printf("Case #%d: ",++cas);
       scanf("%d%d",&n,&m);
       memset(a,0,sizeof(a));
       memset(b,0,sizeof(b));
       for(i=0;i<n;i++)
         for(j=0;j<m;j++)
           scanf("%d",&map[i][j]);
       for(i=0;i<n;i++)
         for(j=0;j<m;j++){
            if(map[i][j]>a[i])
              a[i]=map[i][j];
         }
       for(j=0;j<m;j++)
         for(i=0;i<n;i++){
            if(map[i][j]>b[j])
               b[j]=map[i][j];
         }
       ok=0;
       for(i=0;i<n;i++)
         for(j=0;j<m;j++){
            if(map[i][j]!=a[i]&&map[i][j]!=b[j])
            {
                ok=1;
                break;
            }
         }
       if(ok)
          printf("NO\n");
       else printf("YES\n");
    }
    return 0;
}
