#define MODULUS 1000002013LL
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<string>
#include<set>
#include<vector>
#include<utility>

using namespace std;

long long price(int s, int f, int N, long long p){
  if (s == f) return 0LL;
  long long up = ((long long)(N) * 2LL + s - f + 1) * (f - s) / 2;
  return ((up % MODULUS) * p) % MODULUS;
}

int main() {
  int T, n, i, j, cn, w, m, p, q;
  int curpos, curstart, curfin;
  long long curtraffic, curmin, diffres;
  pair<int, long long> A[2200];
  long long B[2200];
  int C[2200];
  int X, Y;
  long long r;
  cin >> T;
  for(cn=0; cn<T; cn++){
    long long res = 0LL;
    long long oldres = 0LL;
    cin >> n >> m;
    for (i=0; i<m; i++) {
      cin >> p >> q >> r;
      A[i*2].first = p;
      A[i*2].second = -r;
      A[i*2+1].first = q;
      A[i*2+1].second = r;
      oldres = (oldres + price(p, q, n, r)) % MODULUS;
    }
    sort(A, A+(2*m));
 //   for(i=0; i<2*m; i++) cout << A[i].first << " " << A[i].second << "\n";
    C[0] = A[0].first;
    B[0] = -A[0].second;
    curpos = 0;
    for(i=1; i<2*m; i++){
      if (A[i].first == A[i-1].first) {
	B[curpos] = B[curpos] - A[i].second;
      } else {
	curpos++;
	C[curpos] = A[i].first;
	B[curpos] = B[curpos-1] - A[i].second;
      }
    }
 //   for(i=0; i<=curpos; i++) cout << B[i] << " " << C[i] << "\n"; cout << "---\n";
    while (1) {
      curstart = 0;
      while (B[curstart] == 0 && curstart < curpos) curstart++;
      if (curstart == curpos) break;
      curmin = B[curstart];
      curfin = curstart;
      while (B[curfin] > 0 && curfin < curpos) {
	if (B[curfin] < curmin) curmin = B[curfin];
	curfin++;
      }
      res = (res + price(C[curstart], C[curfin], n, curmin)) % MODULUS;
      for(i=curstart; i<curfin; i++) B[i] = B[i] - curmin;
 //     for(i=0; i<=curpos; i++) cout << B[i] << " " << C[i] << "\n"; cout << "---\n";
    }
    diffres = (oldres + MODULUS - res) % MODULUS;
    cout << "Case #" << cn+1 << ": " << diffres << "\n";
   }
  return 0;
}