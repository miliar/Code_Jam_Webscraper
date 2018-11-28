#include <iostream>
#include <fstream>

using namespace std;

int main ()
{
  freopen("D-small-attempt0.in","r",stdin);   
  freopen("Ds.txt","w",stdout);
  
  int T, k, c, s;
  cin>>T;
  for (int t=1;t<=T;++t)
  {
          cin>>k>>c>>s;
          cout<<"Case #"<<t<<":";
          for (int i=1; i<=s; ++i)
              cout<<" "<<i;
          cout<<"\n";
  }
  
  return 0;
}
