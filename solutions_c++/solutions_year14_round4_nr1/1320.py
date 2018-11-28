#include <bits/stdc++.h>
using namespace std;

int main() {
  for(int Tc, tc = (bool)(cin >> Tc); tc <= Tc; ++tc) {
    cout << "Case #" << tc << ": ";
    int N, X;
    cin >> N >> X;
    vector<int> S(N);
    for(int i = 0; i < N; ++i) cin >> S[i];
    sort(S.begin(), S.end());
    int l = 0, r = N-1;
    int res = 0;
    while(l <= r) {
      while(S[l] + S[r] > X && l < r) {
        ++res;
        --r;
      }
      ++res;
      ++l;
      --r;
    }
    cout << res << endl;
  }
  return 0;
}
