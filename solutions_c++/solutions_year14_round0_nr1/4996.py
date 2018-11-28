#include<fstream.h>
#include<stdio.h>
#include<conio.h>
void main()
{
clrscr();
int i,j,t,a,b,count=0,res=0;
int a1[4][4],b1[4][4];
freopen("ppp.in","r",stdin);
freopen("res.txt","w",stdout);
cin>>t;
for(int p=1;p<=t;p++)
{
count=0;
cin>>a;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
cin>>a1[i][j];
}
cin>>b;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
cin>>b1[i][j];
}
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(a1[a-1][i]==b1[b-1][j])
{
res=a1[a-1][i];
count++;
}
}
}
if(count==1)
cout<<"Case #"<<p<<": "<<res<<endl;
else if(count==0)
cout<<"Case #"<<p<<": Volunteer cheated!"<<endl;
else if(count>1)
cout<<"Case #"<<p<<": Bad magician!"<<endl;
}
}