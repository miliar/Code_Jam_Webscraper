#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "1"

#pragma comment(linker, "/STACK:36777216")

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

int GetMaxDif(const vi& arr) {
  int max = 0;
  for (int i = 1; i < arr.size(); ++i) {
    int dif = arr[i - 1] - arr[i];
    if (dif <= 0 || dif < max)
      continue;
    max = dif;
  }

  if (max == 0) return 0;

  double v = (double)max / 10;
  double sum = 0;

  for (int i = 0; i < arr.size() - 1; ++i) {
    sum += min((double)arr[i], v * 10);
  }

  return sum;
}

int GetSumDiff(const vi& arr) {
  int sum = 0;
  for (int i = 1; i < arr.size(); ++i) {
    int dif = arr[i - 1] - arr[i];
    if (dif > 0)
      sum += dif;
  }
  return sum;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
      cin >> arr[i];
    }

    cout << "Case #" << test_index + 1 << ": " << GetSumDiff(arr) << " " << GetMaxDif(arr) << endl;
  }
  return 0;
}
