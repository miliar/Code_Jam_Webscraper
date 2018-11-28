#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int n,m,a[105][105],x[105][105],y[105][105],i,j,l,t,tt;
cin>>tt;
for(t=1;t<=tt;t++)
{
cin>>n>>m;
for(i=0;i<=100;i++)
{
for(j=0;j<=100;j++)
{
x[i][j]=y[i][j]=0;
}
}
for(i=1;i<=n;i++)
{
for(j=1;j<=m;j++)
{
cin>>a[i][j];
x[i][a[i][j]]++;
y[j][a[i][j]]++;
}
}
for(l=1;l<=100;l++)
{
for(i=1;i<=n;i++)
{
if(x[i][l]+x[i][0]==m)
{
for(j=1;j<=m;j++)
{
if(a[i][j]) a[i][j]=0,x[i][l]--,y[j][l]--,x[i][0]++,y[j][0]++;
}
}
}
for(j=1;j<=m;j++)
{
if(y[j][l]+y[j][0]==n)
{
for(i=1;i<=n;i++)
{
if(a[i][j]) a[i][j]=0,x[i][l]--,y[j][l]--,x[i][0]++,y[j][0]++;
}
}
}
}
l=0;
for(i=1;i<=n;i++)
{
for(j=1;j<=m;j++)
{
l=max(l,a[i][j]);
}
}
cout<<"Case #"<<t<<": "<<(l?"NO":"YES")<<endl;
}
return 0;
}