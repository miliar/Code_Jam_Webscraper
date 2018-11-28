#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void solve() {
  int N;
  cin >> N;
  priority_queue<pair<int, char>> q;
  int s = 0;
  for (int i = 0; i < N; ++i) {
    int t;
    cin >> t;
    q.push(make_pair(t, 'A' + i));
    s += t;
  }

  if (s % 2) {
    auto t = q.top();
    q.pop();
    cout << " " << t.second;
    q.push(make_pair(t.first - 1, t.second));
  }

  while (q.top().first > 0) {
    string ans = "";
    for (int i = 0; i < 2; ++i) {
      auto t = q.top();
      q.pop();
      ans += t.second;
      q.push(make_pair(t.first - 1, t.second));
    }
    cout << " " << ans;
  }
  cout << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    printf("Case #%d:", i + 1);
    solve();  
  }
  return 0;
}
