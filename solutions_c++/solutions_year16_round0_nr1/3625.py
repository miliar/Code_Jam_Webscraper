#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void checkDigits(vector<int> &v, ll N) {
  while(N) {
    v[N%10] = 1;
    N /= 10;
  }
}
int main() {
  //freopen("A-small-attempt0.in", "r" , stdin);
  freopen("A-large.in", "r" , stdin);
  freopen("out2.out", "w" , stdout);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    ll N;
    cin >> N;
    if(N == 0) {
      cout << "Case #" << t << ": " << "INSOMNIA" << "\n";
      continue;
    }
    vector<int> v(10, 0);
    bool exit = false;
    ll i = 1;
    while(!exit) {
      ll n = i * N;
      checkDigits(v, n);
      if(find(v.begin(), v.end(), 0) == v.end()) {
        exit = true;
      } else {
        i++;
      }
    }

    cout << "Case #" << t << ": " << i * N << "\n";
  }
}
