#include<iostream>
using namespace std;
int main ()
{
int t;
cin>>t;
int x=0;
do
{
int r1,r2,p;
cin>>r1;
r1=r1-1;
int i,j,a[4][4],b[4][4];
for(i=0;i<4;++i)
{
for(j=0;j<4;++j)
{
cin>>a[i][j];
}
}
cin>>r2;
r2=r2-1;
for(i=0;i<4;++i)
{
for(j=0;j<4;++j)
cin>>b[i][j];
}
int count=0;
for(i=0;i<4;++i)
{
for(j=0;j<4;++j)
{
if(a[r1][i]==b[r2][j])
{
count=count+1;
p=a[r1][i];
}
}
}
x++;
if(count==0)
cout<<"Case #"<<x<<": Volunteer cheated! \n";
if(count==1)
cout<<"Case #"<<x<<": "<<p<<"\n";
if(count>1)
cout<<"Case #"<<x<<": Bad magician!"<<"\n";
}while(x!=t);
return 0;
}
