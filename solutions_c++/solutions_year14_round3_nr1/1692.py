#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <queue>
#include <map>
#include <set>
using namespace std;

int main() {
  int T;
  cin >> T;

  for (int testcase = 1; testcase <= T; ++testcase) {
    long long P, Q;
    char c;
    cin >> P >> c >> Q;

    long long QQ = Q;
    while (QQ % 2 == 0) {
      QQ /= 2;
    }

    cout << "Case #" << testcase << ": ";
    if (QQ == 1 || QQ == P) {
      int cnt = 0;
      for ( ; ; ) {
        if (P * 2 >= Q)
          break;
        P *= 2;
        ++cnt;
      }
      cout << cnt+1 << endl;
    } else {
      cout << "impossible" << endl;
    }
  }
  return 0;
}
