#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int n,i,j,x,k;
string s;
cin>>n;
for(i=1;i<=n;i++)
{
cin>>s;
s+='+';
x=s.length()-1;
//while(x>=0 && s[x]=='+') x--;
k=0;
for(j=0;j<x;j++)
{
if(j<s.length()-1 && s[j]!=s[j+1]) k++;
}
cout<<"Case #"<<i<<": "<<k<<endl;
}
return 0;
}