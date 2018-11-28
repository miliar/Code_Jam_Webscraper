#include<iostream>
using namespace std;
bool isp(long long x)
{
long long y=0,z=x;
while(z) y=y*10+z%10,z/=10;
return x==y;
}
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
long long a,l,r,k;
int t,tt;
cin>>tt;
for(t=1;t<=tt;t++)
{
cin>>l>>r;
k=0;
for(a=1;a*a<=r;a++)
{
if(isp(a) && isp(a*a) && a*a>=l) k++;
}
cout<<"Case #"<<t<<": "<<k<<endl;
}
return 0;
}