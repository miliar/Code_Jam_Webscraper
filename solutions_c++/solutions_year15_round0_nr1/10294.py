#include<stdio.h>
#include<string.h>

int main()
{
  int n,c,t,i,k,s;
  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {
     c=0;
     scanf("%d",&n);
     int a[n+1];
     char cr,b[n+1];
     scanf("%s",b);
     for(k=0;k<=n;k++)
     {
     cr=b[k];	
     a[k]=(int)cr-48;
     }
     s=0;
     for(k=0;k<n;k++)
     {
     s=s+a[k];
     if((k+1)>s)
     {
     c++;
     s++;
     }
     }
     printf("\nCase#%d:%d",i,c);
  }
return 0;
}
