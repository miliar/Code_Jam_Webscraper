#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
const int MAXN = 200 + 10, seed = 1e9 + 7;
VI s[MAXN];

map<LL, int> Cache;
int ID(LL x) {
  if (Cache.count(x)) return Cache[x];
  int sz = Cache.size();
  Cache[x] = sz; return sz;
}

LL HH(string s) {
  LL r = 0;
  for (size_t i = 0; i < s.size(); ++ i) {
    r = r * seed + s[i];
  }
  return r;
}

int main() {
  int T; cin >> T;
  for (int cas = 1; cas <= T; ++ cas) {
    printf("Case #%d: ", cas);
    int n; cin >> n; Cache.clear();
    string buf; getline(cin, buf);
    for (int i = 0; i < n; ++ i) {
      getline(cin, buf); s[i].clear();
      stringstream sin(buf);
      while (sin >> buf) {
        s[i].push_back(ID(HH(buf)));
      }
    }
    int ret = 1e9, m = Cache.size();
    cerr << m << endl;
    static int mp[100000];
    for (int msk = 0; msk < (1 << (n - 2)); ++ msk) {
      for (int i = 0; i < m; ++ i) mp[i] = 0;
      for (auto &x: s[0]) mp[x] |= 1;
      for (auto &x: s[1]) mp[x] |= 2;
      for (int i = 0; i < n - 2; ++ i) {
        if (msk >> i & 1) {
          for (auto &x: s[i + 2]) mp[x] |= 1;
        }
        else {
          for (auto &x: s[i + 2]) mp[x] |= 2;
        }
      }
      int tmp = 0;
      for (int i = 0; i < m; ++ i) tmp += mp[i] == 3;
      ret = min(ret, tmp);
    }
    printf("%d\n", ret);
  }
  return 0;
}