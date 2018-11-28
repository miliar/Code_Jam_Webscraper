#include<iostream>
using namespace std;
int main()
{
long int n;
cin>>n;
for(long int i=0;i<n;i++)
{
long int c=0,s,a[10];
cin>>s;
if(s==0)
cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<"\n";
else
{
long int o,k=s;
for(o=0;o<10;o++)
a[o]=0;
for(o=1;;o++)
{
k=s*o;
while(k>0)
{
if(a[k%10]==0)
c++;
a[k%10]=1;
k/=10;
}
if(c==10)
break;
}
cout<<"Case #"<<i+1<<": "<<s*o<<"\n";
}}
return 0;
}

