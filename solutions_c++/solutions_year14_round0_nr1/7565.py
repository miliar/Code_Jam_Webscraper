#include<iostream>
using namespace std;

int main()
{
freopen("A-small-attempt2.in", "r", stdin);
   freopen("jamcode1.txt", "w", stdout);
int test;
cin>>test;
for(int k=1;k<=test;k++)
{
cout<<"Case #"<<k<<": ";
int ans1, g1[5][5],g2[5][5],i,j,ans2;
cin>>ans1;
for(i=1;i<=4;i++)
{
 for(j=1;j<=4;j++)
 {
   cin>>g1[i][j];
 }
}
cin>>ans2;
for(i=1;i<=4;i++)
{
 for(j=1;j<=4;j++)
 {
  cin>>g2[i][j];
  }
}
int cnt=0,ele;
for(i=1;i<=4;i++)
{
for(j=1;j<=4;j++)
{
if(g1[ans1][i]== g2[ans2][j])
{
ele = g1[ans1][i];
cnt++;
}
}
}
if(cnt==1 )
{
cout<<ele<<endl;
}
else if(cnt==0)
{
cout<<"Volunteer cheated!"<<endl;
}
else 
{
cout<<"Bad magician!"<<endl;
}
}
return 0;
}