#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for (int i=0;i<t;i++)
  {
    double c,f,x;
    cin>>c>>f>>x;
    double r=2;
    double t=0;
    while (1)
    {
      double d=x/r;
      double v=c/r+x/(r+f);
      //cout<<d<<' '<<v<<endl;
      if (d<v)
      break;
      t+=c/r;
      r+=f;
    }
    cout<<"Case #"<<i+1<<": ";
    cout<<setprecision(20)<<t+x/r<<endl;
  }
  return 0;
}
