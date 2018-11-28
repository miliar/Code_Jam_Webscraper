#include<iostream>
using namespace std;
int main()
{
 int a[4][4],b[4][4],r1,r2,c,i,j,ct,d,e=1;
 cin>>c;
 do
 {
 ct=0;
 cin>>r1;
 for(i=0;i<4;i++)
 {
  for(j=0;j<4;j++)
  {
    cin>>a[i][j];
  }
 }  
 
 
 r1=r1-1;
 cin>>r2;
 for(i=0;i<4;i++)
 {
  for(j=0;j<4;j++)
  {
    cin>>b[i][j];
  }
 }
 
 r2=r2-1;
 for(i=0;i<4;i++)
 {
  for(j=0;j<4;j++)
  {
   if(a[r1][j]==b[r2][i])
    {
	 ct++;
	 d=b[r2][i];
	}
  }
 }
  if(ct==1)
  {
   cout<<"Case #"<<e<<": "<<d<<endl;
  }
  else if(ct>1)
  {
   cout<<"Case #"<<e<<": "<<"Bad Magician!"<<endl;
  }
  else if(ct==0)
  {
   cout<<"Case #"<<e<<": "<<"Volunteer cheated!"<<endl;
  }++e;
}
while(c>=e);
return 0;
}
