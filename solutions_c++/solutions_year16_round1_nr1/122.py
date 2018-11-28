// Author: Chi-Kit (George) LAM
#include <cstdio>
#include <cinttypes>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
void solve(int T) {
  string S, ans;
  cin >> S;
  int n = S.length();
  for (int i=0; i<n; ++i) {
    ans = max(ans + S[i], S[i] + ans);
  }
  cout << "Case #" << T << ": " << ans << endl;
  return;
}
int main(){
  int T;
  cin >> T;
  for (int i=0; i<T; ++i) {
    solve(i+1);
  }
  return 0;
}
