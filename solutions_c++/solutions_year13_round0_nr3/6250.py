#include<stdio.h>
int main()
{int a[]={1,4,9,121,484},t,i,a1,b,co,j;
scanf("%d",&t);
for(i=0;i<t;i++)
{scanf("%d",&a1);
scanf("%d",&b);
co=0;
printf("case #%d: ",i+1);
for(j=0;j<5;j++)
if(a[j]>=a1&&a[j]<=b)co++;
printf("%d\n",co);
}
}
