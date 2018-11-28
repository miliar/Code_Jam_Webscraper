#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>

using namespace std;

double dp[216][216];
double dpp[216][216];
double p[216];

double calc(vector<double> x){
  int n = x.size();
  for(int i = 0;i < n + 5;i++){
    for(int j = 0;j < n + 5;j++){
      dpp[i][j] = 0;
    }
  }
  dpp[0][0] = 1;
  for(int i = 1;i <= n;i++){
    double pp = x[i-1];
    for(int j = 0;j <= i;j++){
      dpp[i][j] = dpp[i-1][j] * (1-pp);
      if(j > 0)dpp[i][j] += dpp[i-1][j-1] * pp;
    }
  }
  return dpp[n][n/2];
}

void solve(){
  int n, k;
  cin >> n >> k;
  for(int i = 0;i < n;i++){
    cin >> p[i];
  }
  double res = 0;
  sort(p, p + n);
  for(int i = 0;i < n;i++){
    vector<double> x;
    for(int j = 0;j < i;j++){
      x.push_back(p[j]);
    }
    for(int j = 0;j < (k - i);j++){
      x.push_back(p[n-1-j]);
    }
    res = max(res, calc(x));
  }
  printf("%.10lf\n", res);
  return;
}

int main(){
  int t;
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
