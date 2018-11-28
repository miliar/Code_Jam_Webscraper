#include <bits/stdc++.h>

using namespace std;

map<string, int> id;

vector<int> s[20];
int was[5000], work[5000];

int main() {
  freopen("C.in", "rt", stdin);
  freopen("C.out", "wt", stdout);
  string line;
  int t; getline(cin, line);
  sscanf(line.c_str(), "%d", &t);
  for(int test = 1; test <= t; ++test) {
    id.clear();
    int n; getline(cin, line);
    sscanf(line.c_str(), "%d", &n);
    for(int i = 0; i < n; ++i) {
      s[i].clear();
      getline(cin, line);
      stringstream ss(line);
      while(ss >> line) {
        if(id.count(line) == 0) {
          int sz = id.size();
          id[line] = sz;
        }
        s[i].push_back(id[line]);
      }
    }
    memset(was, 0, sizeof was);
    for(int i = 0; i < 2; ++i) {
      for(int x : s[i]) {
        was[x] |= 1 << i;
      }
    }
    int ans = 1 << 30;
    for(int msk = 0; msk < (1 << n); ++msk) {
      if((msk & 1) || !(msk & 2)) continue;
      memcpy(work, was, sizeof was);
      for(int i = 2; i < n; ++i) {
        if((msk >> i) & 1) {
          for(int x : s[i]) {
            work[x] |= 2;
          }
        }else {
          for(int x : s[i]) {
            work[x] |= 1;
          }
        }
      }
      int res = 0;
      for(int i = 0; i < (int)id.size(); ++i) {
        res += work[i] == 3;
      }
      ans = min(ans, res);
    }
    printf("Case #%d: %d\n", test, ans);
  }
  return 0;
}
