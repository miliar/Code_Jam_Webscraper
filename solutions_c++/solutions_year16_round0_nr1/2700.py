#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int n,i,x[10],z;
long long a,j,k;
cin>>n;
for(i=1;i<=n;i++)
{
cin>>a;
if(a==0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
else
{
for(j=0;j<10;j++) x[j]=0;
j=0;
z=0;
for(;;)
{
j+=a;
k=j;
while(k>0)
{
if(x[k%10]==0) x[k%10]=1,z++;
k/=10;
}
if(z==10)
{
cout<<"Case #"<<i<<": "<<j<<endl;
break;
}
}
}
}
return 0;
}