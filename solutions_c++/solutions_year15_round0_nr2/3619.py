#include <bits/stdc++.h>

using namespace std;

int solve(){
  int n;
  scanf("%d", &n);
  vector<int> v(n);
  for(int i = 0; i < n; ++i){
    scanf("%d", &v[i]);
  }
  int best = 100000;
  for(int i = 1; i <= 1000; ++i){
    int ans = 0;
    for(int j = 0; j < n; ++j) ans += (v[j] - 1) / i;
    best = min(ans + i, best);
  }
  return best;
}

int main(){
  int t;
  scanf("%d", &t);
  for(int i = 0; i < t; ++i) printf("Case #%d: %d\n", i + 1, solve());
}
