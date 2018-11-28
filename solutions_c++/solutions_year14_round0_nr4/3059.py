#include <iostream>
using namespace std;
double data1[1000], data2[1000];
int n;
int calc1()
{
  int i=0,j=0;
  for(;i<n;++i)
  {
    while(data2[j]<data1[i]&&j<n)++j;
    if(j==n) return n-i;
    else ++j;
  }
  return 0;
}
int calc2()
{
  int i=n-1, j=n-1, it=0, ans=0;
  for(;i>=it&&j>=0;)
  {
    if(data1[i]<data2[j])
    {
      ++it; --j;
    }
    else
    {
      --i; --j; ++ans;
    }
  }
  return ans;
}
int main()
{
  int t;
  cin >> t;
  for (int delta = 1; delta <= t; ++ delta)
  {
    cout << "Case #" << delta << ": ";
    cin >> n;
    for(int i=0;i<n;++i) cin >> data1[i];
    sort(data1,data1+n);
    for(int i=0;i<n;++i) cin >> data2[i];
    sort(data2,data2+n);
    cout << calc2() << " " << calc1() << endl;
  }
  return 0;
}
