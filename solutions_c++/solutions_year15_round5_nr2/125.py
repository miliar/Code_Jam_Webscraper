#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

typedef long long int64;

const int oo = 0x3f3f3f3f;

bool isPossible(
    const int k,
    const vector<int> &lengths,
    const int maxPosition,
    const int remainder) {
  vector<bool> dp = vector<bool>(k, false);
  dp[0] = true;
  for (const auto &l: lengths) {
    vector<bool> newDP = vector<bool>(k, false);
    for (int r = 0; r < k; ++r)
      for (int begin = 0; begin + l - 1 <= maxPosition && !newDP[r]; ++begin)
        if (dp[(r - begin + k) % k])
          newDP[r] = true;
    dp = newDP;
  }
  return dp[remainder];
}

int Solve(const int k, const vector<int> &lengths, const int remainder) {
  int maxLength = 0;
  for (const auto &l: lengths)
    maxLength = max(maxLength, l);
  int left = 0, right = k - 1, maxOffset = k;
  while (left <= right) {
    int middle = (left + right) / 2;
    if (isPossible(k, lengths, maxLength + middle - 1, remainder)) {
      right = middle - 1;
      maxOffset = middle;
    } else {
      left = middle + 1;
    }
  }
  return maxLength + maxOffset;
}

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  int testCount;
  cin >> testCount;
  for (int test = 1; test <= testCount; ++test) {
    int n, k;
    vector<int> sums;
    cin >> n >> k;
    sums = vector<int>(n - k + 1);
    for (int i = 0; i < n - k + 1; ++i)
      cin >> sums[i];
    vector<int> coefficient = vector<int>(n, 0);
    for (int i = k; i < n; ++i)
      coefficient[i] = coefficient[i - k] + sums[i - k + 1] - sums[i - k];
    vector<int> lengths = vector<int>(k);
    int remainder = (sums[0] % k + k) % k;
    for (int i = 0; i < k; ++i) {
      int cmin = 0, cmax = 0;
      for (int j = i + k; j < n; j += k) {
        cmin = min(cmin, coefficient[j]);
        cmax = max(cmax, coefficient[j]);
      }
      remainder = (remainder + cmin % k + k) % k;
      lengths[i] = cmax - cmin;
    }
    cout << "Case #" << test << ": " << Solve(k, lengths, remainder) << "\n";
  }
  cin.close();
  cout.close();
  return 0;
}
