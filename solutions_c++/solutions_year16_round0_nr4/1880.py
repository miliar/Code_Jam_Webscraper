#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

string solve(uint64_t k, uint64_t c, uint64_t s) {
  if (s == 0) {
    return "IMPOSSIBLE";
  }

  if (c >= k) {
    // only need to check one tile: 012..(k-1)0..0 position
    uint64_t tile = 0;
    for (uint64_t i = 0; i < k; ++i) {
      tile *= k;
      tile += i;
    }
    for (uint64_t i = 1; i <= c-k; ++i) {
      tile *= k;
    }

    // shift by 1!
    ++tile;
    stringstream ss;
    ss << tile;
    return ss.str();
  } else {
    // need to check k+1-c tiles
    if (s < (k+1-c)) {
      return "IMPOSSIBLE";
    }

    // traverse 01..(c-1) then check last k+1-c == k - (c+1) tiles
    uint64_t offset = 0;
    for (uint64_t i = 0; i < c; ++i) {
      offset *= k;
      offset += i;
    }
    
    // shift by 1!
    ++offset;
    stringstream ss;
    for (uint64_t i = 1; i <= k+1-c; ++i) {
      // TODO check for off-by-1 errors
      ss << offset + (i-1);
      if (i != (k+1-c)) {
        ss << ' ';
      }
    }
    return ss.str();
  }
}

int main(int argc, char* argv[]) {
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    int K;
    int C;
    int S;

    cin >> K >> C >> S;

    cout << "Case #" << t << ": ";
    cout << solve(K, C, S);
    cout << endl;
  }

  return 0;
}
