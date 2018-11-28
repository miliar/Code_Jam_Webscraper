#include<iostream>
using namespace std;
int main()
{
int d;
cin>>d;
int x=1;
while(x<=d)
{
 long long r,t;
  cin>>r>>t;
  long long count=0;
  while(1)
  {
   long long temp;
   temp=2*r+1;
   t=t-temp;
   
   if(t<0)
    break;
    count++;
   r=r+2;
  }
  cout<<"Case #"<<x<<": "<<count<<endl;
 x++;
}
}
