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

int N,L;
vector<string> G;
string B;

void ReadInput() {
  cin >> N >> L;
  G.clear();
  REP(i,N) {
    string s; cin >> s; G.push_back(s);
  }
  cin >> B;
}

string Calc() {
  for(const auto &s : G) if(s==B) return "IMPOSSIBLE";
  string res;
  REP(i,L) res += "01";
  res += "0?1 ";
  REP(i,L-1) res += '?';
  res += '0';
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

