/* Written by Filip Hlasek 2013 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

#define MOD 1000002013

int N, M;
vector<pair<int, int> > v;
map<int, long long> m;

long long cost (int n) {
  return ((long long)(N + (N - n + 1)) * n / 2) % MOD;
}

int main(int argc, char *argv[]){
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%d%d", &N, &M);
    v.clear();
    int original = 0, hack = 0;
    REP(i, M) {
      int o, e, p;
      scanf("%d%d%d", &o, &e, &p);
      v.push_back(make_pair(o, -p));
      v.push_back(make_pair(e, p));
      original = (original + cost(e - o) * p) % MOD;
    }
    sort(v.begin(), v.end());
    m.clear();
    m[-v[0].first] = -v[0].second;
    FOR(i, 1, v.size()-1) {
      if(v[i].second < 0) m[-v[i].first] += -v[i].second;
      else {
        int cnt = v[i].second;
        while(cnt) {
          int d = min((long long)cnt, m.begin()->second);
          cnt -= d;
          hack = (hack + cost(v[i].first + m.begin()->first) * d) % MOD;
          if((m.begin()->second -= d) == 0) m.erase(m.begin());
        }
      }
    }
    printf("Case #%d: %d\n", t, ((original - hack) % MOD + MOD) % MOD);
  }
  return 0;
}
