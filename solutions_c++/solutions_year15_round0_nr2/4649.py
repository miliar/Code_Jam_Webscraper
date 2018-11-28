#include <iostream>
#include <vector>
using namespace std;

int best;
void bt(int& best, int act, vector<int>& v) {
  if (act >= best) return;
  int n = 9;
  while (!v[n] && n > 0) --n;
  best = min(best, act + n);
  --v[n];
  for (int i = 1; i*2 <= n; ++i) {
    vector<int> aux = v;
    aux[i]++;
    aux[n-i]++;
    bt(best, act+1, aux);
  }
}

int main() {
  int T; cin >> T;
  int ncase = 0;
  while (T--) {
    best = 9;
    vector<int> v(10);
    int n; cin >> n;
    for (int i = 0; i < n; ++i) {
      int x; cin >> x;
      v[x]++;
    }
    bt(best, 0, v);
    cout << "Case #" << ++ncase << ": " << best << endl;
  }
}
