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

const string NAMES = "RPS";
int N;
vector<int> TOT;

void ReadInput() {
  cin >> N;
  TOT.assign(3, 0);
  REP(i,3) cin >> TOT[i];
}

string CalcForWinner(int N, int winner) {
  if(N==0) return string(1, NAMES[winner]);
  string a = CalcForWinner(N-1, winner);
  string b = CalcForWinner(N-1, (winner+2)%3);
  if(a>b) swap(a,b);
  return a+b;
}

string Calc() {
  string best = "Z";
  REP(i,3) {
    string s = CalcForWinner(N, i);
    vector<int> cnt(3,0);
    for(char c : s) {
      REP(j,3) if(c==NAMES[j]) ++cnt[j];
    }
    if(cnt==TOT && s<best) best=s;
  }
  if(best=="Z") return "IMPOSSIBLE";
  else return best;
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

