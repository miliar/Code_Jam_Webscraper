#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
int t,n;
char s[1001];
scanf("%d",&t);
for(int x=1;x<=t;x++)
{
int c=0,needed=0;
scanf("%d",&n);
scanf("%s",s);
c=s[0]-48;
for(int i=1;i<=n;i++)
{
if(c<i)
{
needed+=i-c;
c=i;
}
c=c+s[i]-48;
}
printf("Case #%d: %d\n",x,needed);
}
}
