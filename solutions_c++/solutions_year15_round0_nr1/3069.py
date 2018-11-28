#include <iostream>
using namespace std;

int solve(int smx, string s)
{
  int ret=0;
  int clap=s[0]-'0';
  for (int i=1;i<=smx;i++)
  {
    int si=s[i]-'0';
    if (si && i>clap)
    {
      ret+=(i-clap);
      clap+=(i-clap);
    }
    clap+=si;
  }
  return ret;
}

int main()
{
  int T;
  cin>>T;
  for (int z = 1; z <= T; z++)
  {
    int smx;
    string s;
    cin>>smx;
    cin>>s;
    cin.ignore();
    //cout<<"Case #"<<z<<solve(smx, s)<<endl;
    printf("Case #%d: %d\n", z, solve(smx, s));
  }

  return 0;
}
