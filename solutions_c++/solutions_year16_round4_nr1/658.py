#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <cassert>
#include <iostream>
#include <cstring>
#include <cmath>

#define pb push_back
#define all(x) (x).begin(), (x).end()

#ifdef LOCAL
  #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
  #define eprintf(...) 0
#endif

using namespace std;

template<class T> inline void umax(T &a,T b){if(a < b) a = b;}
template<class T> inline void umin(T &a,T b){if(a > b) a = b;}
template<class T> inline T abs(T a){return a > 0 ? a : -a;}

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int inf = 1e9 + 143;
const ll longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

const int N = 1e5 + 100;

const char name[3] = {'R', 'P', 'S'};

#define move moveASD

int n;
int cnt[3];
vi roots[3], nroots[3];
int move[N];
int leftCh[N], rightCh[N];

void readInput() {
  n = read();
  for (int i = 0; i < 3; i++) {
    cnt[i] = read();
  }
}

string calc(int u) {
  int l = leftCh[u];
  int r = rightCh[u];
  if (!l) {
    string res = "";
    res += move[u];
    return res;
  }
  string sl = calc(l);
  string sr = calc(r);
  string res = sl + sr;
  if (res > sr + sl) {
    res = sr + sl;
  }
  return res;
}

void solve() {
  int tick = 0;
  for (int i = 0; i < 3; i++) {
    roots[i].clear();
    for (int j = 0; j < cnt[i]; j++) {
      ++tick;
      move[tick] = name[i];
      leftCh[tick] = 0;
      rightCh[tick] = 0;
      roots[i].pb(tick);
    }
  }
  for (int i = 0; i < n; i++) {
    bool bad = false;
    int battle01 = cnt[0] + cnt[1] - cnt[2];
    if (battle01 % 2 == 1) {
      bad = true;
    }
    battle01 /= 2;
    int battle12 = cnt[1] - battle01;
    int battle02 = cnt[0] - battle01;

    if (battle01 < 0 || battle02 < 0 || battle12 < 0) {
      bad = true;
    }
    if (battle01 + battle02 != cnt[0]) {
      bad = true;
    }
    if (battle12 + battle01 != cnt[1]) {
      bad = true;
    }
    if (battle02 + battle12 != cnt[2]) {
      bad = true;
    }
    if (bad) {
      puts("IMPOSSIBLE");
      return;
    }

    for (int i = 0; i < 3; i++) {
      nroots[i].clear();
    }

    auto fight = [&](int win, int lose) {
      int uwin = roots[win].back();
      int ulose = roots[lose].back();
      roots[win].pop_back();
      roots[lose].pop_back();
      ++tick;
      nroots[win].push_back(tick);
      leftCh[tick] = uwin;
      rightCh[tick] = ulose;
    };

    while (battle01) {
      fight(1, 0);
      cnt[0]--;
      battle01--;
    }
    while (battle02) {
      fight(0, 2);
      cnt[2]--;
      battle02--;
    }
    while (battle12) {
      fight(2, 1);
      cnt[1]--;
      battle12--;
    }

    for (int i = 0; i < 3; i++) {
      roots[i] = nroots[i];
    }
  } 

  int root = -1;
  for (int i = 0; i < 3; i++) {
    if (roots[i].size()) {
      assert(roots[i].size() == 1);
      root = roots[i][0];
    }
  }

  assert(root != -1);
  string res = calc(root);
  printf("%s\n", res.c_str());
  int tot = 1;
  while (n--) {
    tot *= 2;
  }
  assert(res.size() == tot);
}

void preCalc() {
}

int main() {
  preCalc();
  
  int numTestCases = read();
  int fromTest = 0;
  int toTest = int(1e9);
  
  #ifdef PART
    fromTest = FROM
    toTest = TO
  #endif
  
  for (int i = 1; i <= numTestCases; i++) {
    printf("Case #%d: ", i);
    readInput();
    if (i >= fromTest && i <= toTest) {
      solve();
      eprintf("Test %d is done..\n", i);
      fflush(stderr);
      fflush(stdout);  
    }
  }

  return 0;  
}