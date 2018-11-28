#include <iostream>

using namespace std;

int main()
{
 int t,x,r,c;
 cin>>t;
 for(int k=1;k<=t;k++)
 {
  cin>>x>>r>>c;
  if((x==4 && r==2 && c==4) || (x==4 && r==4 && c==2))
  {
   cout<<"Case #"<<k<<": "<<"RICHARD\n";
   continue;
  }
  else if(x==1 && r==1 && c==1)
  {
   cout<<"Case #"<<k<<": "<<"GABRIEL\n";
   continue;
  }
  else if((x==2 && r==2 && c==1) || (x==2 && r==1 && c==2))
  {
   cout<<"Case #"<<k<<": "<<"GABRIEL\n";
   continue;
  }
  else if((2*x)>(r*c))
  {
   cout<<"Case #"<<k<<": "<<"RICHARD\n";
   continue;
  }
  else if((r*c)%x!=0)
  {
   cout<<"Case #"<<k<<": "<<"RICHARD\n";
   continue;
  }
  else if(r<x && c<x)
  {
   cout<<"Case #"<<k<<": "<<"RICHARD\n";
   continue;
  }
  else
  {
   cout<<"Case #"<<k<<": "<<"GABRIEL\n";
   continue;
  }
 }
 return 0;
}
