#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
ifstream a;
a.open("B-small-attempt0.in");
ofstream qq;
qq.open("output.txt");
int x;
a>>x;
for(int i=0;i<x;i++)
{
        qq<<"Case #"<<i+1<<":"<<" ";
 int w,y,max=0;
 a>>w>>y;
  int b[w][y],c[w][y];
  for(int k=0;k<w;k++)
  for(int j=0;j<y;j++)
    a>>b[k][j];
    for(int k=0;k<w;k++)
  for(int j=0;j<y;j++)
    if(b[k][j]>max)
    max=b[k][j];
    for(int k=0;k<w;k++)
  for(int j=0;j<y;j++)
    c[k][j]=max;
    for(int k=0;k<w;k++)
    {
  for(int j=0;j<y;j++)
{
  if(b[k][j]==1)
  {
  int flag=1;
  for(int l=0;l<y;l++)
  if(b[k][l]!=1)
    {
  flag=0;
  break;
    }
    if(flag==1)
     for(int l=0;l<y;l++)
     c[k][l]=1;
  
  flag=1;
  for(int p=0;p<w;p++)
  if(b[p][j]!=1)
  {
  flag=0;
  break;
  }
  if(flag==1)
  for(int p=0;p<w;p++)
  c[p][j]=1;
  }
 } 
}
int flag1=1;
for(int vv=0;vv<w;vv++)
for(int bb=0;bb<y;bb++)
if(b[vv][bb]!=c[vv][bb])
flag1=0;
if(flag1==1)
qq<<"YES"<<endl;
else
qq<<"NO"<<endl;
}
cin>>x;
}
