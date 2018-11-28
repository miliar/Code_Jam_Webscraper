#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <random>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

typedef int64_t i64;
using namespace std;

// TODO: need to test on max size large (CJCJCJCJCJJCJCJCJCJC)
int main() {
  i64 Z;
  cin >> Z;
  char buf[20005];
  for (i64 T = 1; T <= Z; T++) {
    cin >> buf;
    i64 N = strlen(buf);
    vector<bool> removed(N, false);
    i64 ans = 0;
    i64 numRemoved = 0;
    while (true) {
      bool progress = false;
      i64 prev = -1;
      for (i64 i = 0; i < N; i++) {
        if (removed[i])
          continue;
        if (prev != -1 && buf[i] == buf[prev]) {
          ans += 10;
          removed[i] = true;
          removed[prev] = true;
          prev = -1;
          progress = true;
          numRemoved += 2;
        } else {
          prev = i;
        }
      }
      if (!progress) {
        break;
      }
    }
    ans += 5 * (N - numRemoved) / 2;
    cout << "Case #" << T << ": " << ans << endl;
  }
  return 0;
}
