#include <iostream>
#include <vector>
#include <assert.h>
using namespace std;

vector<int64_t> solve(int64_t tiles, int64_t pow, int64_t students) {
  if (pow * students < tiles) {
    return {};
  }  
  
  vector<int64_t> res;
  int64_t lvl = 0, pos = 1;
  for (int64_t tile = 1; tile <= tiles || lvl > 0; tile++) {
    pos = (pos - 1) * tiles + min(tile, tiles);
    lvl++;

    if (lvl == pow) {
      res.push_back(pos);
      lvl = 0;
      pos = 1;
    }
  }
  return res;
}

void test() {
  assert(solve(4, 3, 1).empty());
  assert(solve(4, 4, 1).size() == 1);
  assert(solve(4, 2, 4).size() == 2);
  assert(solve(27, 3, 100).size() == 9);
  assert(solve(27, 2, 100).size() == 14);
  assert(solve(27, 26, 100).size() == 2);
  assert(solve(27, 13, 100).size() == 3);
  assert(solve(27, 13, 2).empty());
  assert(solve(1, 1, 1) == ((vector<int64_t>) {1}));
  assert(solve(4, 1, 100) == ((vector<int64_t>) {1, 2, 3, 4}));
  assert(solve(4, 2, 100) == ((vector<int64_t>) {2, 12}));
  assert(solve(4, 3, 100) == ((vector<int64_t>) {7, 64}));
  assert(solve(4, 4, 100) == ((vector<int64_t>) {28}));
  assert(false);
}

int main() {
  //test();

  int64_t T;
  cin >> T;
  for (int64_t t = 1; t <= T; t++) {
    int64_t k, c, s;
    cin >> k >> c >> s;
    auto res = solve(k, c, s);
    cout << "Case #" << t << ": ";
    if (res.size() == 0) {
      cout << "IMPOSSIBLE\n";
    } else {
      for (int64_t p : res) {
        cout << p << ' ';
      }
      cout << "\n";
    }
  }
  return 0;
}
