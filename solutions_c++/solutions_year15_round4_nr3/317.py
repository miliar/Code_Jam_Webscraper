#include <bits/stdc++.h>
using namespace std;
template<typename T> inline void checkMin(T &a, T b) { if(b<a) a=b; }
template<typename T> inline void checkMax(T &a, T b) { if(a<b) a=b; }
#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

map<string, int> mp;

inline int gid(const string &s) {
  auto it = mp.find(s);
  if (it != mp.end()) {
    return it->Y;
  }
  int id = SZ(mp);
  return mp[s] = id;
}

int n;
set<int> st[32];
int mark[5000][2];

int solve() {
  mp.clear();
  fill(mark[0], mark[5000], 0);

  scanf("%d", &n);
  string s;
  getline(cin, s);
  REP (i, n) {
    getline(cin, s);
    stringstream ss(s);
    st[i].clear();
    while (ss >> s) {
      st[i].insert(gid(s));
    }
    if (i < 2) {
      for (int x: st[i]) {
        ++mark[x][i == 0 ? 0 : 1];
      }
    }
  }

  cerr << "-" << endl;
  int ans = SZ(mp);
  REP (mask, 1 << (n - 2)) {
    REP (i, n - 2) {
      int y = (mask >> i) & 1;
      for (int x: st[i + 2]) {
        ++mark[x][y];
      }
    }
    int temp = 0;
    REP (x, SZ(mp)) {
      temp += mark[x][0] > 0 && mark[x][1] > 0;
    }
    checkMin(ans, temp);
    REP (i, n - 2) {
      int y = (mask >> i) & 1;
      for (int x: st[i + 2]) {
        --mark[x][y];
      }
    }
  }
  return ans;
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: %d\n", index, solve());
  }
  return 0;
}
