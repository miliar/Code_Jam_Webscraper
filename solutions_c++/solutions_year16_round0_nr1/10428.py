#include <iostream>
using namespace std;
int main() {
int T,N,i,n2,k,dig,n1;
int c[9];
cin>>T;
for(i=1;i<=T;i++)
{
int j=1;
cin>>N;
for(k=0;k<=9;k++)
{
c[k]=0;
}
if(N==0)
{
cout<<"Case #"<<i<<": "<<"INSOMNIA";
}
else
{
int k,cnt=0;
while(cnt!=9)
{
cnt=-1;
n1=N*j;
n2=n1;
while(n1!=0)
{
dig=n1%10;
c[dig]=c[dig]+1;
n1=n1/10;
}
j++;
for(k=0;k<=9;k++)
{
if(c[k]>0)
{
cnt++;
}
}
}
cout<<"Case #"<<i<<": "<<n2<<"\n";
}
}
return 0;
}