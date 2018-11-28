#include <iostream>
#include <string>
#include <climits>
using namespace std;

#define FOR(i,a,b) for(typeof(a) i=(a);i<(b);++i)
#define sz size()
#define BIG_NUM 0x3fffffff

int sol(int A[1025], int S, int K) {
  int res = 0;
  FOR(i,K,S+1) {
    if(A[i-K]) {
      ++res;
      FOR(j,0,K) A[i-K+j] = 1-A[i-K+j];
    }
  }
  FOR(i,1,K) if (A[S-K+i]) return BIG_NUM;
  return res;
}

void do_case(int te) {
  int res = BIG_NUM;
  string a;
  int K;
  cin >> a >> K;
  int S = a.sz;
  int A[1024];
  FOR(i,0,S) A[i]=(a[i]=='-');
  res = min(res,sol(A,S,K));
  if (res == BIG_NUM) cout << "Case #" << te << ": IMPOSSIBLE" << endl;
  else cout << "Case #" << te << ": " << res << endl;
}

int main() {
  int te, T=1;
  cin >> te;
  while(te--) {
    do_case(T);
    ++T;
  }
}