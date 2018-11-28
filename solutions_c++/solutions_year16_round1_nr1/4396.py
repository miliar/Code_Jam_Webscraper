#include <stdio.h>
#include<string.h>
int main ()
{
int t,i,j,k,z,b,c [10000],d [10000],l;
char a [10000];
scanf ("%d",&t);
for (i=0;i <t;i++)
{
z=1;
k=1;
scanf ("%s",a);
l=strlen (a);
b=a [0];
for (j=1;j <l;j++)
{
if (a [j]>=b)
{
c [k++]=a[j];
b=a [j];
}
else if (a [j]<b)
{
d [z++]=a [j];
}
}
printf ("Case #%d: ",i+1);k--;
z--;
for (j=k;j>=1;j--)
printf ("%c",c [j]);
printf ("%c",a [0]);
for (j=1;j <=z;j++)
printf ("%c",d [j]);
printf ("\n");
}
return 0;
}