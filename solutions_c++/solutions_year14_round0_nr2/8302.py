//Im namen Gottes
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

void solve()
{
  long double c,f,x;
  cin>>c>>f>>x;
  long double tme=0;
  long double ans=x/2;
  for(int k=0;k<=1e6+40;++k)
    {
      if(k!=0)
	tme+=c/(2+(k-1)*f);
      ans=min(ans,tme+x/(2+k*f));
    }
  cout<<fixed<<setprecision(10)<<ans<<endl;
}

int main()
{
  ios::sync_with_stdio(0);
  int t;
  cin>>t;
  for(int i=1;i<=t;++i)
    {
      cout<<"Case #"<<i<<": ";
      solve();
    }
  return 0;
}
