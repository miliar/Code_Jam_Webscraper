#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long int int64;
#define REP(i,a,b) for (int64 i=int64(a); i<int64(b); ++i)
void unittest();

int64 N, M;
// const int MM=1001;

typedef pair<int64, int64> PII;
typedef vector<PII> VPII;
VPII events;
typedef map<int64, int64> MII;
MII ts;
typedef set<int64> SI;
SI ps;

const int64 MOD = 1000002013;

int64 calc(int64 i) {
  int64 t1 = N * (N+1) / 2;
  int64 e = N - i;
  int64 t2 = e * (e+1) / 2;
  int64 tt = (t1-t2);
  tt %= MOD;

  return tt;
}

void solve(int caseNum) {
  cin>>N>>M;

  events.clear();
  ts.clear();
  ps.clear();

  int64 ans1 = 0;

  REP(i, 0, M) {
    int64 o, e, p;
    cin>>o>>e>>p;
    events.push_back(PII(o, p));
    events.push_back(PII(e, -p));

    int64 gain = calc(e-o);
    gain *= p;
    gain %= MOD;

    ans1 += gain;
    ans1 %= MOD;
  }
  sort(events.begin(), events.end());

  int64 curP=0;//, curT=-1;
  REP(i, 0, events.size()) {
    PII& e = events[i];

    curP += e.second;
    ts[e.first] = curP;
  }
  assert(curP==0);

  for (MII::iterator it=ts.begin(); it!=ts.end(); ++it) {
    ps.insert(it->second);
  }

  int64 ans2 = 0;
  int64 lastP = 0;

  for (SI::iterator sit=ps.begin(); sit!=ps.end(); ++sit) {
    int64 p = *sit;
    if (p==0) continue;
    bool running = false;
    int64 start = -1;
    // printf("runP = %lld - %lld\n", p, lastP);
    int64 runP = p - lastP;

    for (MII::iterator it=ts.begin(); it!=ts.end(); ++it) {
      int64 curP = it->second;
      if (!running) {
        if (curP>=p) {
          start = it->first;
          running = true;
        }
      } else { // running
        if (curP<p) {
          int64 gain = calc(it->first - start);
          // printf("gain: %lld * %lld\n", gain, runP);
          gain *= runP;
          gain %= MOD;

          ans2 += gain;
          ans2 %= MOD;
          running = false;
        }
      }
    }
    // printf("Processing %lld -> %lld\n", p, ans2);
    lastP = p;
  }

  // printf("%lld, %lld\n", ans1, ans2);
  int64 ans = ans1 + MOD - ans2;
  ans %= MOD;

  printf("Case #%d: %lld", caseNum, ans);
  printf("\n", caseNum);
}

int main() {
  unittest();

  int caseCount;
  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
}

