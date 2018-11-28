#include<iostream>
using namespace std;
int main()
{
int i,test,len,row,col;
cin>>test;
for(i=1; i<=test; i++)
{
cin>>len;
cin>>row;
cin>>col;
cout<<"Case #"<<i<<": ";
if(len==1)
{ cout<<"GABRIEL"; }
if(len==2)
{  if((row*col)%2==0)
    { cout<<"GABRIEL"; }
   else
    { cout<<"RICHARD"; }
}
if(len==3)
{
   if(((row*col)%3==0) && ((row*col)!=3))
    { cout<<"GABRIEL"; }
   else
    { cout<<"RICHARD"; }
}
if(len==4)
{ if(((row*col)==12)||((row*col)==16))
   { cout<<"GABRIEL";}
  else
   { cout<<"RICHARD"; }
}
cout<<endl;
}
return 0;
}
