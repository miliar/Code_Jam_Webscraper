#include<stdio.h>
#include<algorithm>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<vector>

using namespace std;
int main()
{
 int test,l,num,j,k,n,n1;;
 double naomi[1000],ken[1000];
 scanf("%d",&test);
 for(l=1;l<=test;l++)
 {
 n=0,n1=0;
  scanf("%d",&num);
  for(j=0;j<num;j++)
   scanf("%lf",&naomi[j]);
  sort(naomi,naomi+num);
  reverse(naomi,naomi+num);
  for(j=0;j<num;j++)
   scanf("%lf",&ken[j]);
  sort(ken,ken+num);
  reverse(ken,ken+num);
  for(j=0,k=0;j<num;j++)
	if(naomi[j]>ken[k])
		n++;
	else
	  k++;

 reverse(ken,ken+num);
 for(j=0,k=num-1;naomi[k]<ken[j] && k>-1;k--);
 reverse(ken,ken+k+1);
 j=k;
 while(j>-1)
 {
  if(naomi[j]>ken[k])
		{n1++;j--;k--;}
  else
      j--;
}
printf("Case #%d: %d %d\n",l,n1,n);
}
   return 0;
}
