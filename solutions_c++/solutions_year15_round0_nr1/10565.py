#include<bits/stdc++.h>
using namespace std;
int main()
{
int t,n,i,j;
cin>>t;
for(j=0;j<t;j++)
{
int s=0,c=0;
cin>>n;
char arr[n+1];
cin>>arr;
for(i=0;i<n+1;i++)
{
if(i==0)
{
s=s+(arr[i]-'0');
}
else if(i<=s)
{
s=s+(arr[i]-'0');
}
else
{
c=c+1;
s=s+(arr[i]-'0')+1;
}
}
cout<<"Case #"<<j+1<<": "<<c<<endl;
}
}
