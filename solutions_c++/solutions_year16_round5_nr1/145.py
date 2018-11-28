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
#define PROBLEM_ID "A"

#pragma comment(linker,"/STACK:32000000")

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
    string s;
    cin >> s;    
    int n = s.length();
    vvi max_score(n + 1, vi(n + 1, 0));
    for (int len = 2; len <= n; len += 2) {
      for (int begin = 0; begin + len <= n; ++begin) {
        int end = begin + len - 1;
        for (int k = begin + 1; k <= end; ++k) {
          max_score[begin][end] = max(max_score[begin][end], max_score[begin + 1][k - 1] + max_score[k + 1][end] + (s[begin] == s[k] ? 10 : 5));
        }
        //max_score[begin][end] = max(max_score[begin][end], max_score[begin + 1][end]);
      }
    }
    int result = 0;
    for (int i = 0; i < n; ++i) {
      result = max(result, max_score[i][n - 1]);
    }
    cout << "Case #" << (test_index + 1) << ": " << result << endl;
    cerr << "Case #" << (test_index + 1) << ": " << result << endl;
    
  }
  return 0;
}
