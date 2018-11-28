#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int q_1 = 1;
const int q_i = 2;
const int q_j = 3;
const int q_k = 4;

const int target[] = { q_i, q_j, q_k };
const int table[5][5] = {
  { 0,   0,    0,    0,    0 },
  { 0, q_1,  q_i,  q_j,  q_k },
  { 0, q_i, -q_1,  q_k, -q_j },
  { 0, q_j, -q_k, -q_1,  q_i },
  { 0, q_k,  q_j, -q_i, -q_1 }
};

int memo[10010][3][10];

bool f(int i, int k, int val, vector<int> const& x) {
  if (k >= 3)                                return i >= x.size();
  if (val == target[k] && f(i, k+1, q_1, x)) return true;
  if (i >= x.size())                         return false;

  int& res = memo[i][k][val + q_k];
  if (res != -1) return res;
  return res = f(i+1, k, (val < 0 ? -1 : 1) * table[abs(val)][x[i]], x);
}

string solve(vector<int> const& x) {
  memset(memo, -1, sizeof(memo));
  return f(0, 0, q_1, x) ? "YES" : "NO";
}

int main() {
  int T;
  cin >> T;

  for (int i = 1; i <= T; ++i) {
    string x;
    int L, X;

    vector<int> input;
    cin >> L >> X >> x;
    for (int j = 0; j < X; ++j) {
      for (char c : x) {
        input.push_back(q_i + (c - 'i'));
      }
    }

    cout << "Case #" << i << ": " << solve(input) << endl;
  }

  return 0;
}
