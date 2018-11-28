#include <iostream>
#include <stdio.h>

using namespace std;

int T, K;
string S;

int main() {
  //freopen("test.in", "r", stdin);
  cin >> T;
  for (int t = 1;t <= T;++t) {
    cin >> S >> K;
    int ans = 0;
    for (int i = 0;i < S.size() - K + 1;++i) {
      if (S[i] == '-') {
        ans++;
        for (int j = i;j < i + K;++j) {
          S[j] = (S[j] == '+') ? '-' : '+';
        }
      }
    }
    
    bool poss = true;

    for (int i = 0;i < S.size();++i)
      if (S[i] != '+')
        poss = false;

    cout << "Case #" << t << ": ";
    if (poss)
      cout << ans << "\n";
    else
      cout << "IMPOSSIBLE\n";
  }
  return 0;
}
