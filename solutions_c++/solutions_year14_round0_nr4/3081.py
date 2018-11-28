#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
// 初期化！
int t, n;
vector<double> naomi, ken, ken2;

int ken_strategy(double n_mass) {
  rep(i,n) {
    if (ken2.at(i) > n_mass) { // ken win
      ken2.at(i) = -1.0;
      return 0;
    }
  }
  // ken has no heavier blocks
  rep(i,n) { // find lightest block
    if (ken2.at(i) >= 0.0) {
      ken2.at(i) = -1.0;
      return 1;
    }
  }
}

int deceive() {
  int ret = 0;
  double n_min;
  double k_min; 
  rep(i,n) {
    n_min = naomi.at(i);
    int j = 0;
    while(ken.at(j) < 0.0) j++;
    k_min = ken.at(j);
    if (n_min > k_min) {
      ret++;
      naomi.at(i) = -1.0;
      ken.at(j) = -1.0;
    }
    else {
      naomi.at(i) = -1.0;
      j = n - 1;
      while(ken.at(j) < 0.0) j--;
      ken.at(j) = -1.0;
    }
  }
  return ret;
}

int war() {
  int ret = 0;
  ken2.clear();
  rep(i,n) {
    ken2.push_back(ken.at(i));
  }
  rep(i,n){
    ret += ken_strategy(naomi.at(i));
    //cout << ret << endl;
  }
  return ret;
}

void solve(int testnum) {
  int ans1, ans2;
  ans2 = war();
  ans1 = deceive();
  printf("Case #%d: %d %d\n", testnum, ans1, ans2);
}

int main() {
  cin >> t;
  rep(i,t) {
    naomi.clear();
    ken.clear();
    cin >> n;
    rep(j,n) {
      double p;
      cin >> p;
      naomi.push_back(p);
    }
    rep(j,n) {
      double p;
      cin >> p;
      ken.push_back(p);
    }
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    solve(i+1); // 1 origin
  }
  return 0;
}
