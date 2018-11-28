#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

bool is(long long x)
{
  vector<int> y;
  while (x>0)
  {
    y.push_back(x%10);
    x/=10;
  }
  for (int i=0;i<y.size();i++)
    if (y[i]!=y[y.size()-i-1])
      return false;
  return true;
}

int main()
{
  int t;
  cin>>t;
  vector<long long> v;
  for (long long i=1;i<=10000000;i++)
    if (is(i))
      if (is(i*i))
        v.push_back(i*i);
  for (int i=1;i<=t;i++)
  {
    long long a,b;
    cin>>a>>b;
    cout<<"Case #"<<i<<": ";
    int c=0;
    for (int j=0;j<v.size();j++)
      if (v[j]>=a&&v[j]<=b)
        c++;
    cout<<c<<endl;
  }  
  return 0;
}
