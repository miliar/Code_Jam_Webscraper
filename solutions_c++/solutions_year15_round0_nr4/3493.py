#include <iostream>

using namespace std;


int main()
{
  int n,x,r,c;
  bool flag;
  cin>>n;
  for(int i=0;i<n;i++)
  {
    flag=1;
    cin>>x>>r>>c;
    if(x==1)
      flag=0;
    else if(x==2)
    {
      if(r==2||c==2)
        flag=0;
      else if(r==4)
        flag=0;
      else if(c==4)
        flag=0;
    }
    else if(x==3)
    {
      if(r==3&&c>1)
        flag=0;
      else if(c==3&&r>1)
        flag=0;
    }
    else if(x==4)
    {
      if(r==4&&c>2)
        flag=0;
      else if(c==4&&r>2)
        flag=0;
    }
    if(flag==0)
      cout<<"Case #"<<i+1<<": GABRIEL\n";
    else
      cout<<"Case #"<<i+1<<": RICHARD\n";
  }

  return 0;
}