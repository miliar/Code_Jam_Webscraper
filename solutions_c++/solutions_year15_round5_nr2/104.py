#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

int main() {
  int T; cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int N, K; cin >> N >> K;
    vector<long long> S(N-K+1);
    REP(i,N-K+1) cin >> S[i];
    vector<long long> diff(N-K);
    REP(i,N-K) diff[i] = S[i+1] - S[i];
    vector<long long> v(K);
    long long rest = S[0];
    REP(i,K) {
      long long sum = 0, mi = 0, ma = 0;
      for (int j = i; j < N-K; j += K) {
        sum += diff[j];
        mi = min(mi, sum);
        ma = max(ma, sum);
      }
      v[i] = ma - mi;
      rest = ((rest + mi) % K + K) % K;
    }
    sort(ALL(v));
    REP(i,K) rest = max(0LL, rest - (v.back() - v[i]));
    long long res = v.back();
    if (rest > 0) ++res;
    cout << "Case #" << cas << ": " << res << endl;
  }
  return 0;
}
