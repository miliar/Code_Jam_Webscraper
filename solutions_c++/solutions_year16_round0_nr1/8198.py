#include <stdio.h>
int main ()
{
long long arr [10]={0},no,test,i,j=0,k,z,c;
scanf ("%lld",&test);
for (i=1;i <=test;i++)
{
k=1;
for (j=0;j <10;j++)
arr [j]=0;
scanf ("%lld",&no);
if (no==0)
printf ("Case #%lld: INSOMNIA\n",i);
else{
k=1;
while (1)
{
c=k*no;
z=c;
while (z!=0)
{
arr [z%10]=1;
z/=10;
}
if (arr [0]==1&&arr [1]==1&&arr [2]==1&&arr [3]==1&&arr [4]==1&&arr [5]

==1&&arr [6]==1&&arr [7]==1&&arr [8]==1&&arr [9]==1)
{
printf ("Case #%lld: %lld\n",i,c);
break;
}
k++;
}
}
}
return 0;
}