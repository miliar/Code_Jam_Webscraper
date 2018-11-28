#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string.h>
#include <utility>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctype.h>
#include <sstream>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <sys/time.h>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long LL;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define MP make_pair
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define PII pair<int, int>
#define PLL pair<long long, long long>
#define CLEAR(a) memset(a, 0, sizeof(a))
#define prev eruyvuy
#define INF 2000000007
#define next abc
#define y1 uu1
#define y2 uu2
const double EPS = 1E-12;
const double PI = acos(-1.0);

using namespace std;

int s[1000005];
//int m[1000005];
vector<int> g[1000005];
int n,d;

LL s0,m0,as,cs,rs,am,cm,rm;

int bst;
set<int> p;

void pre(int idx) {
  p.insert(s[idx]);

  vector<int> upd;
  FOR(i, g[idx].size()) {
    if (s[g[idx][i]] < s[0] - d || s[g[idx][i]] > s[0] + d) {
      continue;
    } else {
      upd.push_back(g[idx][i]);
    }
  }

  g[idx] = upd;
  FOR(i, g[idx].size()) {
    pre(g[idx][i]);
  }
}

int cur;
set<int> ms;
set<int> trem,tadd;

void rem(int idx) {
  trem.insert(idx);
  FOR(i, g[idx].size()) {
    if (ms.find(g[idx][i]) != ms.end())
      rem(g[idx][i]);
  }
}

void ext(int idx) {
  //cout << "EXT " << idx << ' ' << g[idx].size() << endl;
  FOR(i, g[idx].size()) {
    if (s[g[idx][i]] >= cur && s[g[idx][i]] <= cur+d && ms.find(g[idx][i]) == ms.end()) {
      tadd.insert(g[idx][i]);
      ext(g[idx][i]);
    }
  }
}

void proc() {
  // [cur; cur+d]
  trem.clear();
  set<int>::iterator it = ms.begin();
  while (it != ms.end()) {
    if (s[*it] < cur) {
      rem(*it);
    }
    it++;
  }

  // REMOVE rem
  set<int>::iterator it2 = trem.begin();
  while (it2 != trem.end()) {
    ms.erase(*it2);
    it2++;
  }
  //cout << "HERE21" << endl;

  tadd.clear();
  it = ms.begin();
  while (it != ms.end()) {
    ext(*it);
    it++;
  }

  it2 = tadd.begin();
  while (it2 != tadd.end()) {
    ms.insert(*it2);
    it2++;
  }

  bst = max(bst, (int)ms.size());
}

void solve() {
  bst = 1;
  cin >> n >> d;
  cin >> s0 >> as >> cs >> rs;
  cin >> m0 >> am >> cm >> rm;

  s[0] = s0;
  //m[0] = 0;

  FOR(i,n)
  g[i].clear();

  FOR(i, n-1) {
    s0 = (s0*as+cs)%rs;
    m0 = (m0*am+cm)%rm;
    //m0 = m0 % (i+1);
    //cout << m0 << ' ' << m0 % (i+1) << ' ' << s0 << endl;

    //m0 = m0 % (i+1);

    //m[i+1] = m0 % (i+1);
    s[i+1] = s0;

    
    g[m0 % (i+1)].push_back(i+1);
  }

  //cout << g[0].size() << ' ' << g[1].size() << endl;

  p.clear();
  pre(0);

  ms.clear();
  ms.insert(0);

  set<int>::iterator it = p.begin();
  while (it != p.end()) {
    cur = *it;
    proc();
    it++;
  }

  cout << bst << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  FOR(tt,t) {
    cout << "Case #" << tt+1 << ": ";
    solve();
  }
  return 0;
}
