#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  cout.setf(ios::fixed);
  cout.precision(7);
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    cout << "Case #" << cas << ": ";
    int N;
    cin >> N;
    vector<double> nao(N), ken(N);
    for (int i = 0; i < N; ++i) cin >> nao[i];
    for (int i = 0; i < N; ++i) cin >> ken[i];
    sort(nao.begin(), nao.end());
    sort(ken.begin(), ken.end());
    int nl, nt, kl, kt;
    nl = kl = 0; nt = kt = N - 1;
    int points = 0;
    for (int i = 0; i < N; ++i) {
      if (nao[nl] > ken[kl]) {
	++points;
	++nl;
	++kl;
      }
      else {
	++nl;
	--kt;
      }
    }
    cout << points << ' ';
    nl = kl = 0; nt = kt = N - 1;
    points = 0;
    for (int i = 0; i < N; ++i) {
      if (nao[nt] > ken[kt]) {
	++points;
	--nt;
	++kl;
      }
      else {
	--nt;
	--kt;
      }
    }
    cout << points << endl;
  }
}