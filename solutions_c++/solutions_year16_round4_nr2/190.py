// Author: Chi-Kit (George) LAM
#include <bits/stdc++.h>
using namespace std;
namespace jam{
  typedef long long LL;
  int InitJam() {
    cout.precision(9);
    return 0;
  }
} // namespace jam
using namespace jam;
int initjam = InitJam();

int N, K;
double P[201];
double Q[201];

double G[201][201];
double f() {
  for (int i=0; i<=K; ++i) {
    for (int j=0; j<=K; ++j) {
      if (i == 0) {
        G[i][j] = (j==0) ? 1 : 0;
      } else if (j == 0) {
        G[i][j] = (1-Q[i-1]) * G[i-1][j];
      } else {
        G[i][j] = Q[i-1] * G[i-1][j-1] + (1-Q[i-1]) * G[i-1][j];
      }
      //cout << i << " " << j << " " << G[i][j] << " " << Q[i-1] << endl;
    }
  }
  return G[K][K/2];
}

void solve(int T) {
  cin >> N >> K;
  for (int i=0; i<N; ++i) {
    cin >> P[i];
  }
  sort(P,P+N);
  double ans = 0;
  for (int i=0; i<=K; ++i) {
    for (int k=0; k<i; ++k) {
      Q[k] = P[k];
    }
    for (int k=0; k<(K-i); ++k) {
      Q[i+k] = P[N-(K-i)+k];
    }
    for (int k=0; k<K; ++k) {
      //cout << "Q " << Q[k] << endl;
    }
    ans = max(ans, f());
  }
  
  //cout << F[2][1][0] << endl;
  //cout << F[3][2][1] << endl;
  cout << "Case #" << T << ": " << ans << endl;
}
int main(){
  int T;
  cin >> T;
  for (int i=0; i<T; ++i) {
    solve(i+1);
  }
  return 0;
}
