#include<bits/stdtr1c++.h>
using namespace std;

int main () {
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    int MAX, fill = 0, total = 0; string S;
    cin >> MAX >> S;
    for (int i = 0; i <= MAX; ++i) {
      fill += max(i - total, 0);
      
      total = max(i + S[i] - '0', total + S[i] - '0');
    }
    cout << "Case #" << t << ": " << fill << endl;
  }
  return 0;
}
