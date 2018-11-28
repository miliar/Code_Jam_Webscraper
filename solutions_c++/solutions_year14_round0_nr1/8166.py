#include<iostream>
#include<cstdio>
using namespace std;
void magic(int a[5][5], int b[5][5], int x, int y, int z)
{
 x-=1;
 y-=1;
 int h,i,j,flag=0;
 for(i=0;i<5;i++)
 {
  for(j=0;j<5;j++)
  {
   if(a[x][i]==b[y][j])
    {
     flag++;
     h=a[x][i];
    }
  }
 }
 if(flag==1)
  cout<<"Case #"<<z<<": "<<h<<"\n";
 if(flag>1)
  cout<<"Case #"<<z<<": Bad Magician!\n";
 if(flag==0)
  cout<<"Case #"<<z<<": Volunteer cheated!";
}
int main()
{
 freopen("ab.txt","r",stdin);
 freopen("cd.txt","w",stdout);
 int a[5][5],b[5][5],x,t,y;
 //cout<<"Enter t\n";
 cin>>t;
 for(int i=1;i<=t;i++)
 {
  //cout<<"Enter x\n";
  cin>>x;
  for(int m=0;m<4;m++)
   for(int n=0;n<4;n++)
    cin>>a[m][n];
  //cout<<"Enter y\n";
  cin>>y;
  for(int m=0;m<4;m++)
    for(int n=0;n<4;n++)
     cin>>b[m][n];
  magic(a,b,x,y,i);
 }
 return 0;
}
