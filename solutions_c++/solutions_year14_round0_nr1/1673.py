#include<iostream>
using namespace std;
int main()
{
int T,first,sec;
int i,j,k;
int a[4][4],b[4][4];
cin>>T;
int cnt[T],no[T];
for(i=0;i<T;i++)
{
cin>>first;
for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{
cin>>a[j][k];
}
}
cin>>sec;
for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{
cin>>b[j][k];
}
}
cnt[i]=0;
for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{
if(a[first-1][j]==b[sec-1][k])
{
cnt[i]++;no[i]=a[first-1][j];
}
}
}
}
for(i=0;i<T;i++)
{
cout<<"Case #"<<i+1<<": ";
if(cnt[i]==1) cout<<no[i] ;
else if(cnt[i]==0) cout<<"Volunteer cheated!";
else cout<<"Bad magician!";
cout <<"\n" ;
}
return 0 ;
}
