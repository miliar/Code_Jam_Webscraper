#include<stdio.h>
#include<algorithm>
using namespace std;
int in1[5][5],in2[5][5],w[20],w2[20];
int main(){
    
    int n,m,i,j,k,a,b,p,t,x;
    
    
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    
    scanf("%d",&t);
    for(x=1;x<=t;x++)
       {
        scanf("%d",&a);
        for(i=1;i<=4;i++)
           for(j=1;j<=4;j++)
              {scanf("%d",&in1[i][j]);
               w[in1[i][j]] = i;
              }
        
        scanf("%d",&b);
        for(i=1;i<=4;i++)
           for(j=1;j<=4;j++)
              {scanf("%d",&in2[i][j]);
               w2[in2[i][j]] = i;
              }
        p=0;
        for(i=1;i<=16;i++)
           {
            if(w[i] == a && w2[i] == b)
               {p++;
                k=i;
               }
           }
        printf("Case #%d: ",x);
        
        if(p>1) printf("Bad magician!\n");
        else if(p==1) printf("%d\n",k);
        else printf("Volunteer cheated!\n");
        
       }
    
    
 scanf(" ");
 return 0;
}
