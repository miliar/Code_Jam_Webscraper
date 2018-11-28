#define LOCAL
#include <stdio.h>
int main(){
#ifdef LOCAL
       freopen("data.txt", "r", stdin);
       freopen("data.out", "w", stdout);
#endif
       int t,n;
       scanf("%d",&t);
       for(n=1;n<=t;n++){
       printf("Case #%d: ",n);
       void work();
       work();
       }
       return 0;
}
int n,m;
int a[101][101];
int find(int x,int y){
    int i,ans=0;
    for(i=0;i<m;i++){ans=ans>a[x][i]?ans:a[x][i];
                     }
    if(ans<=a[x][y])return 0;
    ans=0;
    for(i=0;i<n;i++){ans=ans>a[i][y]?ans:a[i][y];
                     }
    if(ans<=a[x][y])return 0;
    printf("NO\n");
    return 1;
}
void work(){
     
     scanf("%d%d",&n,&m);
     int i,j;
     for(i=0;i<n;i++)
     for(j=0;j<m;j++){
                      scanf("%d",&a[i][j]);
                      }
     for(i=0;i<n;i++)
     for(j=0;j<m;j++){
                      if(find(i,j))return ;
                      }
     printf("YES\n");
     
}
