#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

typedef long long LL;

int T, K, C, S;

int main()
{
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> K >> C >> S;
    cout << "Case #" << i << ":";

    if (C * S < K) {
      cout << " IMPOSSIBLE" << endl;
    } else {
      for (int r = 0; r * C < K; ++r) {
        LL A = 1; for (int j = 1; j < C; ++j) A *= K;
        
        LL pos = 1;
        for (int j = 1; j <= C; ++j, A /= K) {
          int k = r * C + j; if (k > K) k = K;
          pos += A * (k - 1);
        }

        cout << " " << pos;
      };
      cout << endl;
    }
  }

  return 0;
}
