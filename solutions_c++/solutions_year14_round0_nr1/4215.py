#include<iostream>
using namespace std;
int main()
{
int t,k,i,j,ans1,ans2,m1[4][4],m2[4][4],l,ans;
cin>>t;
for(k=1;k<=t;k++)
{
l=0;
cin>>ans1;
for(i=0;i<4;i++)
 for(j=0;j<4;j++)
  cin>>m1[i][j];
cin>>ans2;
for(i=0;i<4;i++)
 for(j=0;j<4;j++)
  cin>>m2[i][j];
for(i=0;i<4;i++)
 for(j=0;j<4;j++)
  if(m1[ans1-1][i]==m2[ans2-1][j])
   {l++; ans=m1[ans1-1][i];break;}
cout<<"Case #"<<k;
switch(l)
{
case 0:cout<<": Volunteer cheated!"<<endl;
       break;
case 1:cout<<": "<<ans<<endl;
       break;
default:cout<<": Bad magician!"<<endl;
}
}
return 0;
}
