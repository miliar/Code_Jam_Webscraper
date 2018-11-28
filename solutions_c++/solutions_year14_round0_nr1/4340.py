#include<iostream>
using namespace std;
int main()
{
int test,k,i,j,a1,a2,matrix1[4][4],matrix2[4][4],l,ans;
cin>>test;
for(k=1;k<=test;k++)
{
l=0;
cin>>a1;
for(i=0;i<4;i++)
 for(j=0;j<4;j++)
  cin>>matrix1[i][j];
cin>>a2;
for(i=0;i<4;i++)
 for(j=0;j<4;j++)
  cin>>matrix2[i][j];
for(i=0;i<4;i++)
 for(j=0;j<4;j++)
  if(matrix1[a1-1][i]==matrix2[a2-1][j])
   {l++; ans=matrix1[a1-1][i];break;}
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
