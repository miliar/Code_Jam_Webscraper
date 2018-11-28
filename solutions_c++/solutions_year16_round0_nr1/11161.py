#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
	FILE *fout = freopen("A-large.out", "w", stdout);
int t,d=1,i,j,flag1[100][10],flag[100],r,c;
long long int n[100];
cin>>t;
for(i=0;i<t;i++)
{
cin>>n[i];
flag[i]=0;
}
for(i=0;i<t;i++)
{for(j=0;j<10;j++)
{flag1[i][j]=0;
}}
for(i=0;i<t;i++)
{
d=1;
while((d<100)&&(flag[i]!=10))
{
c=n[i]*d;
while(c)
{
r=c%10;
c=c/10;
for(j=0;j<10;j++)
{
if(r==j)
{
flag1[i][j]++;
}
if(flag1[i][j]==1)
{
    flag[i]++;
    flag1[i][j]++;
}}
}
d++;
}
n[i]=n[i]*(d-1);
}
for(i=0;i<t;i++)
{
if(flag[i]==10) cout<<"Case #"<<i+1<<": "<<n[i]<<"\n";
else cout<<"Case #"<<i+1<<": INSOMNIA\n";
}
return 0;
}
