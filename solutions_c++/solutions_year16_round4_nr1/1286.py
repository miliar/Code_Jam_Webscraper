#include<iostream>
#include<algorithm>
#define R 2
#define P 1
#define S 4
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,tt,n,r,p,s,i,j,rr[15],pp[15],ss[15],a[15][5000],z;
string x[15][5000];
cin>>tt;
for(t=1;t<=tt;t++)
{
cin>>n>>r>>p>>s;
z=0;
for(j=1;j<=3;j++)
{
rr[0]=(j==1);
pp[0]=(j==2);
ss[0]=(j==3);
for(i=1;i<=n;i++)
{
rr[i]=rr[i-1]+pp[i-1];
pp[i]=pp[i-1]+ss[i-1];
ss[i]=ss[i-1]+rr[i-1];
}
if(rr[n]==r && pp[n]==p && ss[n]==s) z=j;
//cout<<rr[n]<<" "<<pp[n]<<" "<<ss[n]<<endl;
}
if(z==0) cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
else
{
a[0][1]=(z==1?R:(z==2?P:S));
for(i=1;i<=n;i++)
{
for(j=1;j<=(1<<i);j+=2)
{
a[i][j]=a[i-1][(j+1)/2];
a[i][j+1]=(a[i-1][(j+1)/2]==R?S:(a[i-1][(j+1)/2]==P?R:P));
}
}
for(j=1;j<=(1<<n);j++) x[n][j]=a[n][j]+'0';
for(i=n-1;i>=0;i--)
{
for(j=1;j<=(1<<n);j++)
{
x[i][j]=min(x[i+1][j*2-1],x[i+1][j*2])+max(x[i+1][j*2-1],x[i+1][j*2]);
}
}
cout<<"Case #"<<t<<": ";
for(j=0;j<(1<<n);j++) cout<<(x[0][1][j]==P+'0'?"P":(x[0][1][j]==R+'0'?"R":"S"));
//cout<<x[0][1];
cout<<endl;
}
}
return 0;
}