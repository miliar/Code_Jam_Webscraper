#include <stdio.h>
int main ()
{
long long a [10]={0},n,t,i,j=0,k,z,c;
scanf ("%lld",&t);
for (i=1;i <=t;i++)
{
k=1;
for (j=0;j <10;j++)
a [j]=0;
scanf ("%lld",&n);
if (n==0)
printf ("Case #%lld: INSOMNIA\n",i);
else{
k=1;
while (1)
{
c=k*n;
z=c;
while (z!=0)
{
a [z%10]=1;
z/=10;
}
if (a [0]==1&&a [1]==1&&a [2]==1&&a [3]==1&&a [4]==1&&a [5]==1&&a [6]==1&&a [7]==1&&a [8]==1&&a [9]==1)
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