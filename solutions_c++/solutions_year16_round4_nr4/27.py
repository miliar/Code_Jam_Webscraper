#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << (x) << endl;

typedef long long LL;
typedef unsigned long long ULL;
const int INF = 1000000000; const LL INFLL = LL(INF) * LL(INF);
template<class T> inline int size(const T&c) { return c.size(); }

int N;
vector<unsigned> skills;

void ReadInput() {
  cin >> N;
  skills.assign(N, 0u);
  REP(x,N) {
    string s; cin >> s;
    REP(i,N) {
      if(s[i]=='1') skills[x] |= 1u << i;
    }
  }
}

int cache[16][16];

int OKrec(const vector<unsigned> &skills2, unsigned workers, unsigned machines) {
  int &res = cache[workers][machines];
  if(res!=-1) return res;
  res = 1;
  REP(i,N) if(workers & (1u<<i)) {
    unsigned mm = machines & skills2[i];
    if(mm==0) { res=0; break; }
    REP(j,N) if(mm & (1u<<j)) {
      if(!OKrec(skills2, workers & ~(1u<<i), machines & ~(1u<<j))) { res=0; goto done; }
    }
  }
done:
  return res;
}

bool OK(const vector<unsigned> &skills2) {
  memset(cache, -1, sizeof(cache));
  return OKrec(skills2, (1u<<N)-1u, (1u<<N)-1u);
}

int Calc() {
  unsigned minimalSet = 0;
  REP(i,N) minimalSet |= skills[i] << (i*N);
  int res = INF;
  for(unsigned ss = 0; ss < (1u<<(N*N)); ++ss) {
    if((ss & minimalSet) != minimalSet) continue;
    vector<unsigned> skills2(N);
    REP(i,N) skills2[i] = (ss >> (i*N)) & ((1u<<N)-1u);
    if(OK(skills2)) {
      int v = __builtin_popcount(ss) - __builtin_popcount(minimalSet);
      res = min(res, v);
    }
  }
  return res;
}

int main(int argc, char **argv) {
  int ntc; cin >> ntc;
  FOR(tc,1,ntc) {
    ReadInput();
    if(argc==2 && tc!=atoi(argv[1])) continue;
    auto res = Calc();
    cout << "Case #" << tc << ": " << res << "\n";
  }
}

