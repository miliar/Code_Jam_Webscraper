#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long i64;
typedef vector<int> VI;
typedef vector<string> VS;
#define REP(i,n) for(int _n=n, i=0;i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define PB push_back

int N, M;
int MOD=1000002013;
int O[2000],E[2000];
i64 P[2000];
map<int, i64> in, out;
set<int> gg;

i64 rst;

i64 Z(int a) {
  if(a==0) return 0;
  return ((i64)a*((i64)(a-1)) / 2)%MOD;
}

void play() {
  //cout<<Z(1)<<" "<<Z(2)<<" "<<Z(5)<<endl;
  rst=0;
  REP(i,M) {
    i64 t = (Z(E[i]-O[i]) * P[i]) % MOD;
    rst = (rst+MOD-t)%MOD;
  }

  VI S;
  for(set<int>::iterator it = gg.begin(); it!=gg.end(); ++it) {
    S.PB(*it);
  }
  SORT(S);
  map<int, i64> cnt;
  REP(i, S.size()) {
    int x = S[i];
    cnt[-x] += in[x];
    int z = out[x];
    for (map<int, i64>::iterator it = cnt.begin(); it!=cnt.end(); ++it) {
      int y = it->first;
      i64 a = it->second;
      if(a >= z) {
        cnt[y]-=z;
        //cout<<x<<" "<<y<<" ~ "<<z<<endl;
        i64 t = (Z(x+y) * z)%MOD;
        rst=(rst+t)%MOD;
        break;
      } else {
        z-=a; cnt[y]=0;
        i64 t = (Z(x+y) * a)%MOD;
        //cout<<x<<" "<<y<<" | "<<a<<endl;
        rst=(rst+t)%MOD;
      }
    }
  }
}

int main() {
  int Ts;
  cin>>Ts;
  FOR(cs, 1, Ts) {
    cin>>N>>M;
    gg.clear();
    in.clear();out.clear();
    REP(i,M) {
      cin>>O[i]>>E[i]>>P[i];
      in[O[i]] += P[i];
      out[E[i]] += P[i];
      gg.insert(O[i]); gg.insert(E[i]);
    }
    play();
    cout << "Case #" << cs << ": " <<rst<<endl;
  }
  return 0;
}
