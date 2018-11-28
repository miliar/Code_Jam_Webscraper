#include <iostream>
using namespace std;
int P[1010];
int work()
{
  int D;
  cin >> D;
  int m = 0;
  for(int i=1; i<=D; ++i)
  {
    cin >> P[i];
    if (P[i] > m)
      m = P[i];
  }
  int ans = 10000;
  for(int k=1; k<=m; ++k)
  {
    int tmp = k;
    for(int i=1; i<=D; ++i)
        tmp += (P[i]-1)/k;
    if (tmp < ans)
      ans = tmp;
  }
  return ans;
}
int main()
{
  int T;
  cin >> T;
  for(int i=1; i<=T; ++i)
  {
    cout << "Case #" << i << ": " << work() << endl;
  }
}
