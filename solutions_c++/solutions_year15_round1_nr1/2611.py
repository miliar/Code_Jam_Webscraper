#include<iostream>
#include<algorithm>

using namespace std;
const int MAXN = 1000;
int m[MAXN+1];

int main() {
  int T, n;
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    cin >> n;
    for(int i = 0; i < n; ++i) cin >> m[i];

    int y = 0, r = 0;
    for(int i = 0; i < n-1; ++i) {
      if(m[i] > m[i+1]) {
        y += (m[i]-m[i+1]);
        r = max(r, m[i]-m[i+1]);
      }
    }

    int z = 0;
    for(int i = 0; i < n-1; ++i) {
      z += min(r, m[i]);
    }

    cout << "Case #" << t << ": " << y << " " << z;
    if(t < T) cout << "\n";
  }

  return 0;
}
