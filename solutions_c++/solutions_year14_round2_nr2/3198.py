#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
  int t, a, b, k, m;

  cin >> t;
  for (int ii = 1; ii <= t; ++ii)
  {
    cin >> a >> b >> k;
    m = 0;
    for (int i = 0; i <a; ++i)
    {
      for (int j = 0; j < b; ++j)
      {
        if ((i & j) < k)
          ++m;
      }
    }
    cout << "Case #" << ii << ": " << m << endl;
  }
  return 0;
}
