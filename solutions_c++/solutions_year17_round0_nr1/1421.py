/* prosto beresh' i jahaesh' */

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <cassert>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

#define f first
#define s second

#define pb push_back
#define mp make_pair

using namespace std;

const int N = (int) 1e6 + 7;
const int MOD = (int) 1e9 + 7;

void solve() {
  string s;
  int k;
  cin >> s >> k;
  int n = (int) s.size();
  int cnt = 0;
  for (int i = 0; i + k - 1 < n; i++) {
    if (s[i] == '+')
      continue;
    ++cnt;
    for (int j = i; j < i + k; j++) {
      if (s[j] == '-') {
        s[j] = '+';
      } else {
        s[j] = '-';
      }
    }
  }
  bool bad = 0;
  for (int i = 0; i < n; i++)
    bad |= (s[i] == '-');
  if (!bad) {
    cout << cnt << endl;
  } else {
    cout << "IMPOSSIBLE\n";
  }
}

int main() {
  #ifdef LOCAL
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif

  int t;
  scanf("%d", &t);
  for (int cases = 1; cases <= t; cases++) {
    printf("Case #%d: ", cases);
    solve();
    cerr << cases << " done\n";
  }


  return 0;
}