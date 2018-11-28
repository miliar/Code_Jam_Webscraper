#include <iostream>
using namespace std;

int N,K;
double p[500];
double dp[1<<16][20];

int main(void) {
  int T; cin >> T;
  for(int ts=1; ts<=T; ts++) {
    cout << "Case #" << ts << ": ";
    int N,K; cin >> N >> K;
    for(int i=0; i<N; i++) cin >> p[i];
    dp[0][0]=1;
    double best=0;
    for(int msk=1; msk<(1<<N); msk++) {
      int i;
      for(i=0; i<N; i++) if(msk&(1<<i)) break;
      int msk2=msk^(1<<i);
      for(int j=0; j<=N; j++)
        dp[msk][j] = (j?p[i]*dp[msk2][j-1]:0) + (1-p[i])*dp[msk2][j];
      int cnt=0; for(int j=0; j<N; j++) if(msk&(1<<j)) cnt++;
      if(cnt==K) best=max(best, dp[msk][K/2]);
    }
    printf("%.8lf\n", best);
  }
}
