#include<iostream>
using namespace std;
int main()
{
freopen("A-small-attempt0.in","r",stdin);
freopen("outcsmall.in","w",stdout);
int tt;
cin>>tt;
for(int t=1;t<=tt;t++)
{
int arr[4];
int arr1[4];
int count=0;
int count1=0;
int x,x2;
cin>>x;
x-=1;
for(int u=0;u<4;u++)
{
for(int y=0;y<4;y++)
{
int p;
cin>>p;
if(u==x)
arr[y]=p;
}}
cin>>x2;
x2-=1;
for(int u=0;u<4;u++)
{
for(int y=0;y<4;y++)
{
int p;
cin>>p;
if(u==x2)
arr1[y]=p;
}}
int ans=0;
int total=0;
for(int g=0;g<4;g++)
{
for(int er=0;er<4;er++)
{
if(arr[g]==arr1[er])
{
ans=arr[g];
total++;
}}}
if(total==0)
cout<<"Case "<<"#"<<t<<": "<<"Volunteer cheated!"<<endl;
else if(total>1)
cout<<"Case "<<"#"<<t<<": "<<"Bad magician!"<<endl;
else
cout<<"Case "<<"#"<<t<<": "<<ans<<endl;
}
return 0;
}
