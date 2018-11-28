#include<iostream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
int t,i,j=1,n;
char cc[10];
cin.getline(cc,sizeof(cc));
int s=0,r=0;
char a[1010];
t=atoi(cc);
while(t--)
{
s=r=0;
//fgets(a, 1010, stdin);
cin.getline(a,sizeof(a));
s=a[2]-'0';
n=a[0]-'0';
for(i=1;i<=n;i++)
{
if(a[i+2]-'0'>0)
{
if(s-i>=0)
s=s+a[i+2]-'0';
else
{r+=i-s; s=s+r+a[i+2]-'0';}
}
}
printf("Case #%d: %d\n",j++,r);
}
return 0;
}
