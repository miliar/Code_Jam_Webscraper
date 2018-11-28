#include<bits/stdc++.h>
using namespace std;

int go() {
  int n;
  cin >> n;
  priority_queue<int> qOrig;
  for(int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    qOrig.push(x);
  }
  int best = 999999999;
  for(int limit = 1010; limit >= 0; --limit) {
    int time = 0;
    auto q = priority_queue<int>(qOrig);
    while(q.top() > limit && time < best) {
      int t = q.top();
      q.pop();
      t -= limit;
      q.push(t);
      ++time;
    }
    time += limit;
    best = min(best, time);
  }
  return best;
}

int main() {
  int t;
  cin >> t;
  for(int i = 0; i < t; ++i) {
    printf("Case #%d: %d\n", i + 1, go());
  }
}
