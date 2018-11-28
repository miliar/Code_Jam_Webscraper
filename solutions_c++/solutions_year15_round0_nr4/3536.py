#include<iostream>
using namespace std;
int main()
{
int i,t,x,r,c;
cin>>t;
for(i=1; i<=t; i++)
{
cin>>x;
cin>>r;
cin>>c;
cout<<"Case #"<<i<<": ";
if(x==1)
{ cout<<"GABRIEL"; }
if(x==2)
{  if((r*c)%2==0)
    { cout<<"GABRIEL"; }
   else
    { cout<<"RICHARD"; }
}
if(x==3)
{
   if(((r*c)%3==0)&&((r*c)!=3))
    { cout<<"GABRIEL"; }
   else
    { cout<<"RICHARD"; }
}
if(x==4)
{ if(((r*c)==12)||((r*c)==16))
   { cout<<"GABRIEL";}
  else
   { cout<<"RICHARD"; }
}
cout<<endl;
}
return 0;
}
