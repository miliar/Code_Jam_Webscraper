#include<iostream>
#include<vector>
using namespace std;
bool ispalin(int a)
{
string b="",c="";
while(a!=0)
{
b=b+(char)(a%10+48);
c=(char)(a%10+48)+c;
a=a/10;
}
if(c==b)
return 1;
return 0;
}
int main()
{
int i;
vector<int>a(1001,0);
for(i=1;i*i<=1000;i++)
{
if(ispalin(i)&&ispalin(i*i))
{a[i*i]=1;
}
}
for(i=1;i<=1000;i++)
a[i]=a[i-1]+a[i];
int t,A,B,k=1;
cin>>t;
while(t--)
{
cout<<"Case #"<<k<<": ";
k++;
cin>>A>>B;
cout<<a[B]-a[A-1]<<endl;
}
}
