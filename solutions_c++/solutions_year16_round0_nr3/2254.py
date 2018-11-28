#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int n,j,i,l;
cin>>i>>n>>j;
cout<<"Case #1:"<<endl;
for(i=1;i<=j;i++)
{
cout<<"11";
for(l=0;l<(n-4)/2;l++)
{
if((1<<l)&i) cout<<"11";
else cout<<"00";
}
cout<<"11 ";
for(l=3;l<=11;l++) cout<<l<<" ";
cout<<endl;
}
return 0;
}