#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

vector<float> yes;
vector<int> take;
//1 = P, 2= R, 3 = S
//1 beats 2 beats 3 beats 1
int N,K;
float res,ans;


float calc(int idx,int y, int n) {
  if (idx < K) {
    float sum = 0;
    if (y > 0) {
      sum += yes[take[idx]] * calc(idx+1,y-1,n);
    }
    if (n > 0) {
      sum += (1-yes[take[idx]]) * calc(idx+1,y,n-1);
    }
    return sum;
  } else {
    return 1.0;
  }

}

void solve(int idx,int k,int nk) {
  if (k > 0) {
    take[K-k] = idx;
    solve(idx+1,k-1,nk);
    if (nk > 0)
      solve(idx+1,k,nk-1);
  } else {
    float res = calc(0,K/2,K/2);
    if (res > ans) {
      ans = res;

    }
  }
}


int main() {
  int T;
  cin >> T;
  for (int t = 1;t <= T;t++) {
    ans = -1;
    cin >> N >> K;
    yes.resize(N);
    take.resize(K);
    for (int i = 0;i < N;i++) {
      cin >> yes[i];
    }
    solve(0,K,N-K);
    printf("Case #%d: ",t);
    cout << ans << endl;
  }
}
