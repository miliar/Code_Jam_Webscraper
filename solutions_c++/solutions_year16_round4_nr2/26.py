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

int N,K;
vector<double> prob;

void ReadInput() {
  cin >> N >> K;
  prob.resize(N);
  for(double &p : prob) cin >> p;
  sort(prob.begin(), prob.end());
}

double Calc(const vector<double> &pp) {
  vector<double> cur(K+1, 0.0);
  cur[0] = 1.0;
  for(double p : pp) {
    vector<double> cur2(K+1,0.0);
    REP(i,K+1) cur2[i] += (1-p) * cur[i];
    REP(i,K) cur2[i+1] += p * cur[i];
    cur = cur2;
  }
  return cur[K/2];
}

double Calc(int left) {
  vector<double> prob2;
  REP(i,left) prob2.push_back(prob[i]);
  REP(i,K-left) prob2.push_back(prob[N-1-i]);
  return Calc(prob2);
}

double Calc() {
  double res = 0;
  FOR(left,0,K) res = max(res, Calc(left));
  return res;
}

int main(int argc, char **argv) {
  int ntc; cin >> ntc;
  FOR(tc,1,ntc) {
    ReadInput();
    if(argc==2 && tc!=atoi(argv[1])) continue;
    auto res = Calc();
    printf("Case #%d: %.16f\n", tc, res);
  }
}

