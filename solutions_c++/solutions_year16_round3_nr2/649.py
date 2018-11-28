#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

typedef long long LL;
LL T, B, M;
LL mx;

int main()
{
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ":";
    cin >> B >> M;

    mx = 1;
    for (int j = 0; j < B - 2; ++j)
      mx *= 2;

    if (M > mx) {
      cout << " IMPOSSIBLE" << endl;
      continue;
    }

    cout << " POSSIBLE" << endl;

    vector<int> v(B, 0);
    LL MM = M;
    if (M == mx) {
      for (int j = 0; j < B - 1; ++j)
        v[j] = 1;
    } else {
      for (int j = 1; j < B - 1; ++j) {
        v[j] = M % 2;
        M /= 2;
      }
    }

    for (int j = 0; j < B - 1; ++j) {
      for (int k = 0; k < B - 1; ++k)
        cout << (int)(j < k);
      cout << v[j];
      cout << endl;
    }
    for (int k = 0; k < B; ++k)
      cout << 0;
    cout << endl;
  }

  return 0;
}
