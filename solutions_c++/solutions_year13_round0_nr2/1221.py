#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
using namespace std;
int table[105][105];
int main(){
    
    int n,m,i,j,k,a,b,x,y,t,check,temp,hori,ver;
    
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
    scanf("%d",&t);
    for(k=1;k<=t;k++)
       {
        scanf("%d%d",&n,&m);
        
        for(i=1;i<=n;i++)
           for(j=1;j<=m;j++)
              scanf("%d",&table[i][j]);
        
        check = 1;
        for(i=1;i<=n;i++)
           {
            for(j=1;j<=m;j++)
               {
                
                ver = 1;
                hori = 1;
                for(a = 1;a<=n;a++)
                   if(table[a][j] > table[i][j]) 
                      {ver = 0;
                       break;
                      }
                for(a = 1;a<=m;a++)
                   if(table[i][a] > table[i][j])
                      {
                       hori = 0;
                       break;
                      }
                if(hori == 0 && ver == 0)
                   {check = 0;
                    break;
                   }
               }
            if(check == 0) break;
           }
        printf("Case #%d: ",k);
        if(check == 0) printf("NO\n");
        else printf("YES\n");
        
       }
    
    
    
 scanf(" ");
 return 0;
}
