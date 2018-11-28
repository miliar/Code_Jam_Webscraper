#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>


using namespace std;

double get(const vector<double> &P, const vector<int64_t> &newcomb, int64_t k) {
  vector<vector<double>> dp(k+1, vector<double>(k/2+1));
  dp[0][0]=1.0;
  for(int64_t i=1;i<=k;i++) {
    for(int64_t j=0;j<=min(i,k/2);j++) {
      if(j > 0) {
        dp[i][j]=P[newcomb[i-1]]*dp[i-1][j-1] + (1-P[newcomb[i-1]])*dp[i-1][j];
      } else {
        dp[i][0]=(1 - P[newcomb[i-1]])*dp[i-1][0];
      }
    }
  }
  return dp[k][k/2];
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(12);

  int64_t T;
  cin >> T;

  for(int64_t t=1;t<=T;t++) {
    cout << "Case #" << t << ": ";
    int64_t n, k;
    cin >> n >> k;

    vector<double> P(n);
    for(int64_t i=0;i<n;i++) {
      cin >> P[i];
    }

    sort(P.begin(), P.end());

    vector<int64_t> comb(k);
    for(int64_t i=0;i<k;i++) comb[i]=i;

    double maxprob=get(P, comb, k);
    bool improves=true;
    while(improves) {
      improves=false;
      for(int64_t m=k-1;m>=0;m--) {
        if(m < k-1 && comb[m]==comb[m+1]-1) continue;
        if(m == k-1 && comb[m] == P.size()-1) continue;
        vector<int64_t> newcomb=comb;
        if(m < k-1) newcomb[m]=newcomb[m+1]-1;
        else newcomb[m]=P.size()-1;
        /*vector<vector<double>> dp(k+1, vector<double>(k/2+1));
        dp[0][0]=1.0;
        for(int64_t i=1;i<=k;i++) {
          for(int64_t j=0;j<=min(i,k/2);j++) {
            if(j > 0) {
              dp[i][j]=P[newcomb[i-1]]*dp[i-1][j-1] + (1-P[newcomb[i-1]])*dp[i-1][j];
            } else {
              dp[i][0]=(1 - P[newcomb[i-1]])*dp[i-1][0];
            }
          }
        }*/
        double foo=get(P, newcomb, k);
        if(foo >= maxprob) {
          improves=true;
          comb=newcomb;
          maxprob=foo;
        }
      }
      for(int64_t m=0;m<k;m++) {
        if(m > 0 && comb[m]==comb[m-1]+1) continue;
        if(m == 0 && comb[m] == 0) continue;
        vector<int64_t> newcomb=comb;
        if(m > 0) newcomb[m]=newcomb[m-1]+1;
        else newcomb[m]=0;
        vector<vector<double>> dp(k+1, vector<double>(k/2+1));
        /*dp[0][0]=1.0;
        for(int64_t i=1;i<=k;i++) {
          for(int64_t j=0;j<=min(i,k/2);j++) {
            if(j > 0) {
              dp[i][j]=P[newcomb[i-1]]*dp[i-1][j-1] + (1-P[newcomb[i-1]])*dp[i-1][j];
            } else {
              dp[i][0]=(1 - P[newcomb[i-1]])*dp[i-1][0];
            }
          }
        }*/
        double foo=get(P, newcomb, k);
        if(foo > maxprob) {
          improves=true;
          comb=newcomb;
          maxprob=dp[k][k/2];
        }
      }

    }
    cout << maxprob << '\n';
 /*   for(auto c: comb) cout << P[c] << " ";
    cout << endl;*/
  }
  return 0;
}

