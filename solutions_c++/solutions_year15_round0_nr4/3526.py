#include<iostream>
using namespace std;
int main()
{
int t,x,r,c;
int flag=0;
cin>>t;
for(int j=0;j<t;j++)
{
  cin>>x>>r>>c;
  if(x>=7)
    flag=1;
  else if(x==1)
    flag=0;
  else if(x==2)
  {
     if(r%2!=0&&c%2!=0)
       flag=1;
     else flag=0;
  }
  else if(x==3)
  {
    if((r==3&&c!=1)||(c==3&&r!=1))
      flag=0;
    else flag=1;
  }
  else if(x==4)
  {
    if(r==4&&(c==3||c==4))
      flag=0;
    else if(c==4&&(r==3||r==4))
     flag=0;
    else flag=1;
  }
   cout<<"Case #"<<j+1<<": ";
   if(flag==1)
     cout<<"RICHARD"<<endl;
   else cout<<"GABRIEL"<<endl;
}
return 0;
}
