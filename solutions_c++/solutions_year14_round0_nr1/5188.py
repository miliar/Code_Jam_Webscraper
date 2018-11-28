#include<stdio.h>
#include<iostream>

using namespace std;
int main()
{
int t,ans1,ans2,j,k,i,y;
int a1[4][4];
int a2[4][4];
int out=0;
cin>>t;

for(i=1;i<=t;i++)
{
  cin>>ans1;
  for(j=1;j<=4;j++)
  {
   for(k=1;k<=4;k++)
 {
 cin>>a1[j][k];
  }
}
cin>>ans2;
for(j=1;j<=4;j++)
{
for(k=1;k<=4;k++)
{
cin>>a2[j][k];
}
}
out=0;
for(j=1;j<=4;j++)
{
for(k=1;k<=4;k++)
{
if(a1[ans1][j]==a2[ans2][k])
{
out++;
y=a1[ans1][j];
}
}
}
if(out==1)
cout<<"Case #"<<i<<": "<<y<<"\n";
else if(out>=1)
cout<<"Case #"<<i<<": "<<"Bad magician!"<<"\n";
else if(out==0)
cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<"\n";
}
return 0;
}

