#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

void flip(vector<bool>& v, int start, int k) {
  for (int i = 0; i < k; ++i)
    v[start + i] = !v[i + start];
}

void generate() {
  int size = 8;
  int k = 3;
  int test = 100;
  vector<bool> v(size, true);

  cout << test << endl;

  for (int i = 0; i < test; ++i) {
    for (auto e : v)
      if (e)
        cout <<"+";
      else
        cout <<"-";

    cout << " " << k << endl;

    flip(v, rand() % (size - k + 1), k);
  }
}

int main() {
  // generate();
  // return 0;
  int T = 0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    int k = 0;
    string s;

    cin >> s >> k;

    vector<bool> v(s.size());

    for (size_t i = 0; i < s.size(); ++i)
      if (s[i] == '+')
        v[i] = true;
      else
        v[i] = false;

    int solve = 0;

    for (size_t i = 0; i <= v.size() - k; ++i) {
      if (v[i] == false) {
        flip(v, i, k);
        solve++;
      }
    }

    for (size_t i = 0; i < v.size(); ++i)
      if (v[i] == false) {
        solve = -1;
        break;
      }

    if (solve != -1) {
      cout << "Case #" << test << ": " << solve << endl;
    } else {
      cout << "Case #" << test << ": IMPOSSIBLE" << endl;
    }

  }
}
