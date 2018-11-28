#include <iostream>
#include <set>
using namespace std;
int main() {
  int T, N;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    cin >> N;
    cout << "Case #" << cas << ": ";
    if (N == 0) {
      cout << "INSOMNIA" << endl;
      continue;
    }
    set<int> ss;
    for (int i = 1; ; ++i) {
      int n = N * i;
      while (n) {
        ss.insert(n%10);
        n /= 10;
      }
      if (ss.size() == 10) {
        cout << N * i << endl;
        break;
      }
    }
  }
  return 0;
}
