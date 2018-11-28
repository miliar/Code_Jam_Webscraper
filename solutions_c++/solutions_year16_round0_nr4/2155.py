#include <stdlib.h>
#include <iostream>

using namespace std;

void solve(long long K, long long C, long long S)
{
  if (S * C < K) {
    cout << "IMPOSSIBLE";
    return;
  }

  for (int i = 0; i < (K + C - 1) / C; i++) {
    long long ans = 0;
    for (int j = 0; j < C; j++) {
      ans *= K;
      ans += min(i * C + j, K - 1);
    }
    cout << " " << ans + 1;
  }
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    long long K, C, S;
    cin >> K >> C >> S;
    cout << "Case #" << t << ":";
    solve(K, C, S);
    cout << "\n";
  }
}

