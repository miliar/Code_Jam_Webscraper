#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int main()
{
freopen("A-large", "r", stdin );
freopen("output.txt","w",stdout);

int t,i,j,sum,ct;
int Smax;
char s[1005]="";
cin>>t;
for(i=1;i<=t;i++)
{
sum=0;ct=0;
cin>>Smax;
cin>>s;
for(j=0;j<strlen(s);j++)
if(sum>=j)
sum=sum+(s[j]-48);
else
{
ct+=j-sum;
sum=j+(s[j]-48);
}
cout<<"Case #"<<i<<": "<<ct<<"\n";
}
return 0;
}