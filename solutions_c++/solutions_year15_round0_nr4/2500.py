//------------Author: Aashit Singh-----------//

#include "iostream"
#include "cstring"
#include "cstdlib"
#include "cstdio"
#include "cmath"

using namespace std;

int main(int argc, char const *argv[])
{
  freopen("small_in", "r", stdin);
  freopen("out", "w", stdout);
  int t,b;
  cin>>t;
  for(b=1;b<=t;b++)
  {
    int x,r,c;
    cin>>x>>r>>c;
    if(x==1)
    {
      cout<<"Case #"<<b<<": GABRIEL\n";
    }
    else if(x==2)
    {
      if(r==1&&c==1)
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==1&&c==2)||(r==2&&c==1))
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if((r==1&&c==3)||(r==3&&c==1))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==1&&c==4)||(r==4&&c==1))
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if(r==2&&c==2)
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if((r==2&&c==3)||(r==3&&c==2))
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if((r==2&&c==4)||(r==4&&c==2))
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if(r==3&&c==3)
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==3&&c==4)||(r==4&&c==3))
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if(r==4&&c==4)
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
    }
    else if(x==3)
    {
      if(r==1&&c==1)
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==1&&c==2)||(r==2&&c==1))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==1&&c==3)||(r==3&&c==1))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==1&&c==4)||(r==4&&c==1))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if(r==2&&c==2)
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==2&&c==3)||(r==3&&c==2))
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if((r==2&&c==4)||(r==4&&c==2))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if(r==3&&c==3)
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if((r==3&&c==4)||(r==4&&c==3))
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if(r==4&&c==4)
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
    }
    else if(x==4)
    {
      if(r==1&&c==1)
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==1&&c==2)||(r==2&&c==1))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==1&&c==3)||(r==3&&c==1))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==1&&c==4)||(r==4&&c==1))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if(r==2&&c==2)
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==2&&c==3)||(r==3&&c==2))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==2&&c==4)||(r==4&&c==2))
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if(r==3&&c==3)
      {
        cout<<"Case #"<<b<<": RICHARD\n";
      }
      else if((r==3&&c==4)||(r==4&&c==3))
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
      else if(r==4&&c==4)
      {
        cout<<"Case #"<<b<<": GABRIEL\n";
      }
    }
  }
  return 0;
}