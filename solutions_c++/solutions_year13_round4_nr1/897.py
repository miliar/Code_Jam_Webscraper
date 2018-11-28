#include <cstdio>
#include <queue>
#include <utility>
#include <functional>
#include <map>
#include <algorithm>
using namespace std;

const int MOD = 1000002013;

int testcase() {
  vector<pair<int, int> > Q;
  map<int, long long> cnt;
  vector<int> cst;

  int N, M;
  scanf("%d%d", &N, &M);
  int tot = 0;

  cst.resize(N);
  cst[0] = 0;
  for(int i = 1; i < N; ++i)
    cst[i] = N - i + cst[i - 1];

  for(int i = 0; i < M; ++i) {
    int o, e, p;
    scanf("%d%d%d", &o, &e, &p);
    Q.push_back(make_pair(o, -p));
    Q.push_back(make_pair(e,  p));

    tot = (tot + (long long) p * cst[e - o]) % MOD;
  }

  sort(Q.begin(), Q.end());
  for(auto event : Q) {
    if(event.second < 0) {
      cnt[event.first] += -event.second;
    }
    else {
      while(event.second) {
        long long nm = min(cnt.rbegin()->second, (long long) event.second);
        tot = (tot - (long long) nm * cst[event.first - cnt.rbegin()->first]);
        cnt.rbegin()->second -= nm;
        event.second -= nm;

        if(0 == cnt.rbegin()->second) {
          cnt.erase(--cnt.end());
        }
      }
    }
  }

  return tot;
}

int main() {
  int T;
  scanf("%d", &T);
  for(int tc = 1; tc <= T; ++tc) {
    printf("Case #%d: %d\n", tc, testcase());
  }
}
