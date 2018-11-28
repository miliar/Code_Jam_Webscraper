#include<stdio.h>
#include<conio.h>
int main()
{
int t;
clrscr();
freopen("a.txt","r",stdin);
freopen("output.txt","w",stdout);
scanf("%d",&t);
int m=t;
while(t--)
{
int n;
char a[1000];
scanf("%d",&n);
int i;
int s=0;
int k=0;
scanf("%s",a);
for(i=0;i<=n;i++)
{
k=k+((int)a[i]-48);
if(a[i]=='0'&&k<i+1)
{
k++;
s++;
}
}
printf("Case #%d: %d\n",m-t,s);
}
return 0;
}
