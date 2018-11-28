#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <utility>
using namespace std;
void flip(string& s, int i, int j) {
  for (int k = i; k <= j; ++k) {
    s[k] = s[k] == '-' ? '+' : '-';
  }
}

void solve() {
  string s;
  int K;
  cin >> s;
  scanf("%d",&K);
  int N = s.size();
  int cnt = 0;
  for (int i = N-K; i >= 0; --i) {
    int j = i + K - 1;
    if (s[j] == '-') {
      flip(s, i, j);
      ++cnt;
    }
  }
  bool ok = true;
  for (int i = 0; ok && i < N; ++i) {
    if (s[i] == '-') {
      ok = false;
    }
  }
  if (ok) {
    printf(" %d", cnt);
  } else {
    printf(" IMPOSSIBLE");
  }
}

int main(){
  int T;
  scanf("%d",&T);
  for (int TC=1;TC<=T;++TC) {
    printf("Case #%d:", TC);
    solve();
    printf("\n");
  }
  return 0;
}