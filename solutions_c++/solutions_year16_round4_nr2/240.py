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

using Table = vector<vector<double>>;

double Dp(int x, int y, const vector<double>& A, Table& dp) {
  if (x == 0 && y == 0) {
    return 1;
  }
  if (x < 0 || y < 0) {
    return 0;
  }

  double& r = dp[x][y];
  if (r != -1) {
    return r;
  }

  int n = x + y - 1;
  r = Dp(x - 1, y, A, dp) * A[n] + Dp(x, y - 1, A, dp) * (1.0 - A[n]);
  return r;
}

void Solve() {
  int N, K;
  cin >> N >> K;

  vector<double> A(N);
  for (auto& a : A) {
    cin >> a;
  }

  sort(A.begin(), A.end());

//  cout.precision(2);
//  cout << '\n';
//  for (auto i : A) {
//    cout << fixed << i << ' ';
//  }
//  cout << '\n';

//  double result = 0;
//  vector<double> XX;
//  int NN = 1 << N;
//  for (int mask = 0; mask < NN; ++mask) {
//    if (__builtin_popcount(mask) != K) {
//      continue;
//    }

//    vector<double> B;
//    B.reserve(K);
//    Table dp(K + 1, vector<double>(K + 1, -1));

//    for (int i = 0; i < N; ++i) {
//      if ((1 << i) & mask) {
//        B.push_back(A[i]);
//      }
//    }

//    double cand = Dp(K / 2, K / 2, B, dp);
//    if (result < cand) {
//      result = cand;
//      XX = B;
//    }
//  }

//  for (auto i : XX) {
//    cout << fixed << i << ' ';
//  }
//  cout << '\n';

  double result = 0;
  for (int c = 0; c <= K; ++c) {
    Table dp(K + 1, vector<double>(K + 1, -1));

    vector<double> B;
    B.reserve(K);
    for (int i = 0; i < c; ++i) {
      B.push_back(A[i]);
    }
    for (int i = N - K + c; i < N; ++i) {
      B.push_back(A[i]);
    }
    assert(B.size() == K);

    result = max(result, Dp(K / 2, K / 2, B, dp));
  }

  cout.precision(10);
  cout << fixed << result << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/B-large.in", "rb", stdin);
  freopen("../Console/B-large.out", "wb", stdout);
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
