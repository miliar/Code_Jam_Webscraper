#define NDEBUG
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

#define ALL(x) (x).begin(), (x).end()

int solve1() {
  int n;
  cin >> n;
  vector<int> seq(n);
  for (int i=0; i<n; ++i) {
    cin >> seq[i];
  }
  vector<int> seq_sorted = seq;
  sort(ALL(seq_sorted));
  int out = 0;
  for (int x : seq_sorted) {
    auto it = find(ALL(seq), x);
    assert(it != seq.end());
    out += min(it - seq.begin(), seq.end() - it - 1);
    seq.erase(it);
  }
  return out;
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: %d\n", tt, solve1());
  }
}
