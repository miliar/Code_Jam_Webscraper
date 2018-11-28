#include<stdio.h>
#include<algorithm>
int main()
{
 int t,i,n,k,cn,j,war=0,D_war;
 double naomi[1000],ken[1000];
 scanf("%d",&t);
 for(i=1;i<=t;i++)
 {
 war=0,D_war=0;
  scanf("%d",&n);
  for(j=0;j<n;j++)
   scanf("%lf",&naomi[j]);
  std::sort(naomi,naomi+n);
  std::reverse(naomi,naomi+n);
  for(j=0;j<n;j++)
   scanf("%lf",&ken[j]);
  std::sort(ken,ken+n);
  std::reverse(ken,ken+n);
  for(j=0,k=0;j<n;j++)
	if(naomi[j]>ken[k])
		war++;
	else
	  k++;
	
 std::reverse(ken,ken+n);
 for(j=0,k=n-1;naomi[k]<ken[j] && k>-1;k--);
 std::reverse(ken,ken+k+1);
 j=k;
 while(j>-1)
 {
  if(naomi[j]>ken[k])
		{D_war++;j--;k--;}
  else
      j--;
}
printf("Case #%d: %d %d\n",i,D_war,war);	
}
   return 0;
}
