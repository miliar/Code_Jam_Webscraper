#include<iostream>
using namespace std;
int main()
{
int t,k;
cin>>t;
for(k=1;k<=t;k++)
{
int n,m,i,j,a[5][5],b[20]={0},ct=0,ma;
cin>>n;
for(i=1;i<=4;i++)
for(j=1;j<=4;j++)
cin>>a[i][j];
for(i=1;i<=4;i++)
b[a[n][i]]=1;
cin>>m;
for(i=1;i<=4;i++)
for(j=1;j<=4;j++)
cin>>a[i][j];
for(i=1;i<=4;i++)
if(b[a[m][i]]==1)
{
ct++;
ma=a[m][i];
}
cout<<"Case #"<<k<<": ";
if(ct>1)
cout<<"Bad magician!\n";
else if(ct==0)
cout<<"Volunteer cheated!\n";
else
cout<<ma<<endl;
}
return 0;
}
