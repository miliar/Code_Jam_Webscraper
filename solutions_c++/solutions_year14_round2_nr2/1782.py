#include<stdio.h>
int main()
{ int t,i,j,k,l,ans,a,b;
scanf("%d",&t);
for(i=1;i<=t;i++)
{
scanf("%d %d %d",&a,&b,&k);
printf("Case #%d: ",i);
ans=0;
for(j=0;j<a;j++)
 for(l=0;l<b;l++)
  if((j&l)<k) ans++;
printf("%d\n",ans);              
}
return 0;
}
