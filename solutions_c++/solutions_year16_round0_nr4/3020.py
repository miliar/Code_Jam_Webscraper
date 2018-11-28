#include <bits/stdc++.h>
using namespace std;

void solve(int K) {
  for(int i = 1; i <= K; i++) {
    cout << i << " ";
  }
  cout<<endl;
}

int main() {
  freopen("D-small-attempt0.in", "r" , stdin);
  //freopen("B-large.in", "r" , stdin);
  //freopen("in", "r" , stdin);
  freopen("D-small.out", "w" , stdout);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int K, C, S;
    cin >> K >> C >> S;

    cout << "Case #" << t << ": ";
    solve(K);
  }
}
