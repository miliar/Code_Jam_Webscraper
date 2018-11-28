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

int e[10005];
int p,x;
map<LL,LL> m;
map<LL,LL> cnt;
vector<int> cur;

void solve() {
  m.clear();
  cur.clear();
  cnt.clear();
  cin >> p;
  FOR(i, p) {
    cin >> e[i];
  }
  FOR(i,p) {
    cin >> x;
    m[e[i]] = x;
  }

  cnt[0] = 1;

  map<LL,LL>::iterator it = m.begin();
  while (it != m.end()) {
    if (it->second - cnt[-it->first] == 0) {
      it++;
      continue;
    }

    //cout << it->second << endl;
    while (it->second - cnt[-it->first] > 0) {
      LL x = it->first;
      //m[x]--;
      map<LL,LL>::iterator it2 = cnt.begin();
      while (it2 != cnt.end()) {
        cnt[it2->first - x] += it2->second;
        it2++;
      }
      //cout << "ADD " << x << endl;
      cur.push_back(x);
    }

    it++;
  }

  sort(ALL(cur));
  FOR(i,cur.size()) {
    cout << ' ' << cur[i];
  }
  cout << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  FOR(tt,t) {
    cout << "Case #" << tt+1 << ":";
    solve();
  }
  return 0;
}
