#include <iostream>

using namespace std;

long long gcd(long long a,long long b)
{
  if (b==0)
  return a;
  return gcd(b,a%b);
}

int main()
{
  int n;
  cin>>n;
  for (int q=1;q<=n;q++)
  {
    long long a,b;
    cin>>a;
    char r;
    cin>>r>>b;
    long long g=gcd(a,b);
    a/=g;
    b/=g;
    
    bool z=1;
    long long t=b;
    while (t)
    {
      if (t%2)
      {
        z=0;t=0;
      }
      if (t==2)
      break;
      t/=2;
    }
    int x=1;
    double d=a*1.0/b;
    if (z)
    {
      while (d<0.5-1e-9)
      {
        d*=2;
        x++;
      }
    }
    
    cout<<"Case #"<<q<<": ";
    if (z) cout<<x<<endl;
    else cout<<"impossible\n";
  }
  return 0;
}
