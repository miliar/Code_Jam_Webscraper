// {{{ template
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<pii> vpii;
// }}}

char buff[10000000];

int ns;
map<string, int> s;
set<int> eng, fre;

vi get() {
  gets(buff);
  string x = buff;
  stringstream ss(x);
  vi ret;
  while (ss >> x) {
    if (s.count(x) == 0) {
      s[x] = ns++;
    }
    ret.push_back(s[x]);
  }
  return ret;
}

int st[3005];
int who[3005];

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int n;
    scanf("%d", &n);
    gets(buff);
    int m = n - 2;
    s.clear();
    ns = 0;
    vi english = get();
    vi french = get();
    eng.clear();
    fre.clear();
    memset(st, 0, sizeof(st));
    for (int i : english) {
      eng.insert(i);
      st[i] |= 1;
    }
    for (int i : french) {
      fre.insert(i);
      st[i] |= 2;
    }
    vvi a(m);
    for (int i = 0; i < m; i++) {
      a[i] = get();
    }
    int ans = (int)1e9;
    int add = 0;
    for (int i = 0; i < 3000; i++) {
      add += st[i] == 3;
    }
    for (int mask = 0; mask < (1 << m); mask++) {
      int cur = add;
      for (int i = 0; i < m; i++) {
        if (mask & (1 << i)) {
          for (int j : a[i]) {
            if (~st[j] & 1) {
              st[j] |= 1;
              who[j] |= (1 << i);
              cur += st[j] == 3;
            }
          }
        } else {
          for (int j : a[i]) {
            if (fre.count(j) == 0) {
              if (~st[j] & 2) {
                st[j] |= 2;
                who[j] |= (1 << i);
                cur += st[j] == 3;
              }
            }
          }
        }
      }
      ans = min(ans, cur);
      for (int i = 0; i < m; i++) {
        for (int j : a[i]) {
          if (who[j] & (1 << i)) {
            who[j] ^= 1 << i;
            if (mask & (1 << i)) {
              st[j] ^= 1;
            } else {
              st[j] ^= 2;
            }
          }
        }
      }
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}

