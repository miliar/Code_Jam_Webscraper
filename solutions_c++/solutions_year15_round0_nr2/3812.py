#include <bits/stdc++.h>

using namespace std;

map< vector<int>, int> mapa;

int go(vector<int> v) {
  vector<int> novo;
  for (int i = 0; i < v.size(); ++i) {
    if (v[i] > 0) novo.push_back(v[i]);
  }
  if (novo.empty()) return 0;
  sort(novo.begin(), novo.end());
  vector<int> before = novo;
  map< vector<int>, int >::iterator it = mapa.find(novo);
  if (it != mapa.end()) return it->second;
  for (int i = 0; i < novo.size(); ++i) {
    --novo[i];
  }
  int ans = go(novo) + 1;
  for (int i = 0; i < novo.size(); ++i) {
    ++novo[i];
  }
  int x = novo[novo.size()-1];
  novo.push_back(0);
  for (int i = 1; i < x; ++i) {
    novo[novo.size()-2] = x - i;
    novo[novo.size()-1] = i;
    ans = min(ans, 1 + go(novo));
  }
  return mapa[before] = ans;
}

int main() {
  int nt; scanf("%d", &nt);
  for (int _ = 1; _ <= nt; ++_) {
    int n; scanf("%d", &n);
    vector<int> v;
    for (int i = 0; i < n; ++i) {
      int x; scanf("%d", &x);
      v.push_back(x);
    }
    printf("Case #%d: %d\n", _, go(v));
  }
  return 0;
}