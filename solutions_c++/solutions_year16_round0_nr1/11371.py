#include<conio.h>
#include<stdio.h>
#include<iostream.h>
void main()
{
freopen("small2.txt","r",stdin);
freopen("sai.txt","w",stdout);
int k,j,n,i,rem,t,a[200],l,m,o,p,q,r,s,u,v,w;
scanf("%d",&t);
for(j=1;j<=t;j++)
scanf("%d",&a[j]);
for(j=1;j<=t;j++)
{
l=m=o=p=q=r=s=w=u=v=0;
n=a[j];
if(a[j]==0)
printf("Case #%d: INSOMNIA\n",j);
else
{
for(i=1;;i++)
{
if(l>0&&m>0&&o>0&&p>0&&q>0&&r>0&&s>0&&w>0&&u>0&&v>0)
break;
k=n*i;
while(k!=0)
{
rem=k%10;
switch(rem)
{
case 0:m++;break;
case 1:l++;break;
case 2:o++;break;
case 3:p++;break;
case 4:q++;break;
case 5:r++;break;
case 6:s++;break;
case 7:w++;break;
case 8:u++;break;
case 9:v++;
}
k=k/10;
}
}
i--;
printf("Case #%d:  %d\n",j,n*i--);
}
}
}