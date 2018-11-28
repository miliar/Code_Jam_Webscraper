#include<iostream>
#include<string>
using namespace std;

int main()
{
long int t,n,x,i,j;
cin>>t;
string s[t+1];
long y[t];
for(i=1;i<=t;i++)
{cin>>n;
cin>>s[i];
x=0;
y[i]=0;
for( j=0;j<=n;j++)
{
if((x<j) && ((s[i].at(j)-'0')!=0))
{y[i]+=j-x;
x+=y[i];}
x+=s[i].at(j)-'0';

}}
for(long i=1;i<=t;i++)
{
cout<<"Case #"<<i<<": "<<y[i]<<"\n";

}
return 0;}
