#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
int n,m,sum,count,i,j;
char str[7];
scanf("%d",&n);
j=1;
while(j<=n)
{
scanf("%d %s",&m,str);
if(strlen(str)==1)
{if(str[0]=='0')
{
sum=1;}
else
sum=0;
}
else
{
sum=0;
count=0;
for(i=0;i<m;i++)
{
count=count+(str[i]-48);
if(count<(i+1))
{sum++;
count++;
}
}
}
printf("Case #%d: %d\n",j,sum);
j++;
}
return 0;
}
