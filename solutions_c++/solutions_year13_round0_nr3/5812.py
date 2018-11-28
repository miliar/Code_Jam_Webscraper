#include<stdio.h>
int a[1002];
int main()
{   int i,t,l,u;
    
    a[1]=1;
    a[4]=1;
    a[9]=1;
    a[121]=1;
    a[484]=1;
    
    for(i=2;i<=1002;i++)
    a[i]=a[i-1]+a[i];
    
    
    
    
    scanf("%d",&t);
    
    for(i=1;i<=t;i++)
    {
                     scanf("%d %d",&l,&u);
                     printf("Case #%d: %d\n",i,a[u]-a[l-1]);
    }
    
    
    
    
   
    return 0;
}
