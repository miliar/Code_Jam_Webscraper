#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
int t,i;int c=1;
cin>>t;
while(c<=t)
{
int flag=0;
int a[10];
for(i=0;i<10;i++)
{
a[i]=0;
}
long int n,m=0;
cin>>n;
if(n!=0)
{
while(!flag)
{
m++;
long int x=n*m;
while(x>0)
{
int d=x%10;
a[d]=1;
x/=10;
}
int meta=1;
for(i=0;i<10;i++)
{
if(a[i]==0)
{
meta=0;
}
}
flag=meta;
}
cout<<"Case #"<<c<<": "<<n*m<<endl;
}
else
{
cout<<"Case #"<<c<<": INSOMNIA"<<endl;
}

c++;
}

return 0;
}
