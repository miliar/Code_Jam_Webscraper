#include<iostream>
#include<stdio.h>
#include<fstream>
#include<vector>
using namespace std;
#define M 4
char st[M][M];
int find(char h)
{
int i,j,n=0,x=-1,y=-1,k,l,m;
for(i=0;i<M;i++)
for(j=0;j<M;j++)
if(st[i][j]=='.')
{
n=1;
}
else if(st[i][j]=='T')
{
st[i][j]=h;
x=i;
y=j;
}
for(i=0;i<M;i++)
{
for(j=0;j<M;j++)
{
if(st[i][j]!=h)
break;
}
if(j==M)
{
if(x!=-1&&y!=-1)
st[x][y]='T';
return 1;
}
}
for(j=0;j<M;j++)
{
for(i=0;i<M;i++)
{
if(st[i][j]!=h)
break;
}
if(i==M)
{
if(x!=-1&&y!=-1)
st[x][y]='T';
return 1;
}
}
if((st[0][0]==h&&st[1][1]==h&&st[2][2]==h&&st[3][3]==h)||(st[0][3]==h&&st[1][2]==h&&st[2][1]==h&&st[3][0]==h))
{
if(x!=-1&&y!=-1)
st[x][y]='T';
return 1;
}
if(x!=-1&&y!=-1)
st[x][y]='T';
if(n==0)
return -1;
return 0;
}
int main()
{
int i,j,t,k,n,a,b;
cin>>t;
for(k=1;k<=t;k++)
{
for(i=0;i<M;i++)
cin>>st[i];
j=find('X');
if(j==-1)
cout<<"Case #"<<k<<": Draw\n";
else if(j==1)
cout<<"Case #"<<k<<": X won\n";
else
{
j=find('O');
if(j==1)
cout<<"Case #"<<k<<": O won\n";
else
cout<<"Case #"<<k<<": Game has not completed\n";
}
}
return 0;
}
