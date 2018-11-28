#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
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
#define PROBLEM_ID "B"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int n, K;
    cin >> n >> K;
    vector<double> p(n);
    for (int i = 0; i < n; ++i) {
      cin >> p[i];
    }
    sort(p.begin(), p.end());
    vector< vector< vector<double> > > prob(K + 1, vector< vector<double> >(K + 1, vector<double>(K + 1, 0)));
    prob[0][0][0] = 1;
    for (int a = 0; a <= K; ++a) {
      for (int b = 0; a + b < K; ++b) {
        if (a + 1 <= K) {
          for (int i = 0; i <= a + b + 1; ++i) {
            prob[a + 1][b][i] = 0;
            if (i > 0) {
              prob[a + 1][b][i] += p[a] * prob[a][b][i - 1];
            }
            if (i <= a + b) {
              prob[a + 1][b][i] += (1 - p[a]) * prob[a][b][i];
            }
          }
        }
        if (b + 1 <= K) {
          for (int i = 0; i <= a + b + 1; ++i) {
            prob[a][b + 1][i] = 0;
            if (i > 0) {
              prob[a][b + 1][i] += p[n - (b + 1)] * prob[a][b][i - 1];
            }
            if (i <= a + b) {
              prob[a][b + 1][i] += (1 - p[n - (b + 1)]) * prob[a][b][i];
            }
          }
        }
      }
    }
    double res = 0;
    for (int a = 0; a <= K; ++a) {
      int b = K - a;
      if (prob[a][b][K / 2] > res) {
        res = prob[a][b][K / 2];
      }
    }
    cout << "Case #" << (test_index + 1) << ": ";
    cerr << "Case #" << (test_index + 1) << ": ";
    printf("%g\n", res);
    fprintf(stderr, "%g\n", res);    
  }
  return 0;
}
