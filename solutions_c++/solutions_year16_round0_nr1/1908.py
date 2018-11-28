#include <bits/stdc++.h>
using namespace std;

set<int> digits(int x)
{
  set<int> ans;
  if (x==0) ans.insert(0);
  while (x>0)
  {
    ans.insert(x%10);
    x/=10;
  }
  return ans;
}

void solve(int n)
{
  if (n == 0)
  {
    cout<<"INSOMNIA"<<endl;
    return;
  }
  int bits = 0;
  int k = 0;
  while (bits!=0b1111111111)
  {
    k+=n;
    set<int> dig = digits(k);
    for (auto i = dig.begin(); i!=dig.end(); ++i)
      bits |= (1<<(*i));
  }
  cout<<k<<endl;
}

main()
{
  int T;
  cin>>T;
  for (int t = 1;t<=T;++t)
  {
    cout<<"Case #"<<t<<": ";
    int n;
    cin>>n;
    solve(n);
  }
}
