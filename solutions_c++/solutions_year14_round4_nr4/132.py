#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define MOD 1000000007

long long fact[10000];
long long comb[1001][1001];
int M, N, nn;
vector<string> v;

vector<long long> doit(int s, int e, int p) {
  nn += min(e-s, N);
  vector<long long> ret(N+1, 1);
  if (p == v[s].size()) {
    for (int i = 0; i <= N; i++) ret[i] = i;
  }
  for (int i = s + (p==v[s].size()), j; i < e; i = j) {
    for (j = i+1; j < e && v[j][p] == v[i][p]; j++)
      ;
    vector<long long> cur = doit(i, j, p+1);
    for (int i = 0; i <= N; i++)
      ret[i] = (ret[i] * cur[i]) % MOD;
  }
  if (e-s <= N) {
    for (int i = 0; i < e-s; i++) ret[i] = 0;
    for (int i = e-s; i <= N; i++) {
      ret[i] = 1;
      for (int j = 0; j < e-s; j++)
        ret[i] = (ret[i] * (i-j)) % MOD;
    }
  } else {
//for (int i = 0; i <= N; i++) cout << ret[i] << ' ';
//cout << endl;
    for (int i = 1; i <= N; i++) {
      for (int j = 0; j < i; j++) {
        ret[i] = (ret[i] - ret[j]*comb[i][j]) % MOD;
      }
    }
//for (int i = 0; i <= N; i++) cout << ret[i] << ' ';
//cout << endl;
    for (int i = 0; i < N; i++) ret[i] = 0;
  }
//cout << s << ' ' << e << ' ' << p << ' ' << v[s] << ' ' << ret[N] << endl;
  return ret;
}

main() {
  fact[0] = 1;
  for (int i = 1; i < 10000; i++) {
    fact[i] = (fact[i-1]*i) % MOD;
  }
  for (int i = 0; i <= 1000; i++) {
    comb[i][0] = comb[i][i] = 1;
    for (int j = 1; j < i; j++)
      comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD;
  }

  int T, prob=1;
  for (cin >> T; T--;) {
    cin >> M >> N;
    v = vector<string>(M);
    for (int i = 0; i < M; i++) cin >> v[i];
    sort(v.begin(), v.end());
    nn = 0;
    vector<long long> ret = doit(0, v.size(), 0);
    cout << "Case #" << prob++ << ": " << nn << ' ' << (ret[N]+MOD)%MOD << endl;
  }
}
