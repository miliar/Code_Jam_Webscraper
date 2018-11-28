#include<iostream>

using namespace std;


int main()
{
int T=0;
cin>>T;
for(int i=0;i<T;i++)
{
int res=0;
int resVal=0;
int ans1=0,ans2=0;
int cardsb[4][4];
int cardsa[4][4];
cin>>ans1;
for(int j=0;j<4;j++)
{
for(int k=0;k<4;k++)
{
cin>>cardsb[j][k];
}
}
cin>>ans2;
for(int j=0;j<4;j++)
{
for(int k=0;k<4;k++)
{
cin>>cardsa[j][k];
}
}
for(int j=0;j<4;j++)
{
for(int k=0;k<4;k++)
{
if(cardsb[ans1-1][j]==cardsa[ans2-1][k])
{
res++;
resVal=cardsb[ans1-1][j];
}
}
}
if(res==1)
{
cout<<"Case #"<<i+1<<": "<<resVal<<endl;
}
else if(res>1)
{
cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
}
else if(res==0)
{
cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
}
}
return 0;
}