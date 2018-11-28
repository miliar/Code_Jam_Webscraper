# include<iostream>
using namespace std;
int main()
{
int t,i,j,k,a[105][105],n,m,x=0,y=0,z=0,l;
cin>>t;
for(l=1;l<=t;l++)
{
cin>>n>>m;
for(i=0;i<n;i++)
{
for(j=0;j<m;j++)
{
cin>>a[i][j];
}
}
z=0;
for(i=0;i<n;i++)
{
for(j=0;j<m;j++)
{
x=0;
y=0;
for(k=0;k<m;k++)
x=x+a[i][k];
for(k=0;k<n;k++)
y=y+a[k][j];
if((x>(m*a[i][j]))&&(y>(n*a[i][j])))
z=1;
}
}
if(z==1)
cout<<"Case #"<<l<<": NO"<<"\n";
else
cout<<"Case #"<<l<<": YES"<<"\n";
}
return 0;
}
