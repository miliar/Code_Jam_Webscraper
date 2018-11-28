#include<iostream>
#include<bits/stdc++.h> 
#include<fstream>
#include<set>
#include<map>
#define up(j,n,i) for(i=j;i<n;i++)
using namespace std;
typedef long long int lld;
int main()
{
lld t,k=0;
fstream I,O;
I.open("in.in",ios::in);
O.open("out.txt",ios::out);
I>>t;
k=1;
while(k<=t)
{
lld sp[210],sn[210],i,ans=0;
string a;
I>>a;
if(a[0]=='+')
{
sp[0]=0;
sn[0]=1;
}
else
{
sp[0]=1;
sn[0]=0;
}
lld j;
up(1,a.size(),i)
{
if(a[i]=='-')
sp[i]=1+sn[i-1];
else
{
j=i;
while(a[j]!='-'&&j>=0)
j--;
if(j<0)
sp[i]=0;
else
sp[i]=sp[j];
}
if(a[i]=='+')
sn[i]=1+sp[i-1];
else
{
j=i;
while(a[j]!='+'&&j>=0)j--;
if(j<0)
sn[i]=0;
else
sn[i]=sn[j];
}
}
ans=sp[a.size()-1];
O<<"Case #"<<k<<": ";
O<<ans<<endl;
k++;
}
return 0;
}
