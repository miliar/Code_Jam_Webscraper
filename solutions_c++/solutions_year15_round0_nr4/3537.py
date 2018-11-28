#include<iostream>
using namespace std;
int main()
{
int k,t,x,ro,co;
cin>>t;
for(k=1; k<=t; k++)
{
cin>>x;
cin>>ro;
cin>>co;
cout<<"Case #"<<k<<": ";
if(x==1)
{ cout<<"GABRIEL"; }
if(x==2)
{  if((ro*co)%2==0)
    { cout<<"GABRIEL"; }
   else
    { cout<<"RICHARD"; }
}
if(x==3)
{
   if(((ro*co)%3==0) && ((ro*co)!=3))
    { cout<<"GABRIEL"; }
   else
    { cout<<"RICHARD"; }
}
if(x==4)
{ if(((ro*co)==12)||((ro*co)==16))
   { cout<<"GABRIEL";}
  else
   { cout<<"RICHARD"; }
}
cout<<endl;
}
return 0;
}
