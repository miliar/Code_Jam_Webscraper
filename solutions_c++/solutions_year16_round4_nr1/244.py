#include <algorithm>
#include <bitset>
#include <cassert>
#include <cinttypes>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

string Winner(char type, int N) {
  if (N == 0) {
    string result;
    result += type;
    return result;
  }

  string left, right;
  if (type == 'P') {
    left = Winner('P', N - 1);
    right = Winner('R', N - 1);
  } else if (type == 'R') {
    left = Winner('R', N - 1);
    right = Winner('S', N - 1);
  } else {
    left = Winner('P', N - 1);
    right = Winner('S', N - 1);
  }

  return min(left + right, right + left);
}

bool Check(const string& str, int R, int P, int S) {
  if (count(str.begin(), str.end(), 'R') != R) {
    return false;
  }
  if (count(str.begin(), str.end(), 'P') != P) {
    return false;
  }
  if (count(str.begin(), str.end(), 'S') != S) {
    return false;
  }
  return true;
}

void Solve() {
  int N, R, P, S;
  cin >> N >> R >> P >> S;

  vector<string> result;
  string types = "PRS";
  for (char type : types) {
    string r = Winner(type, N);
    if (Check(r, R, P, S)) {
      result.push_back(r);
    }
  }

  if (result.empty()) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << *min_element(result.begin(), result.end()) << endl;
  }
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/A-large.in", "rb", stdin);
  freopen("../Console/A-large.out", "wb", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    cout << "Case #" << tc + 1 << ": ";
    Solve();
  }

  return 0;
}
