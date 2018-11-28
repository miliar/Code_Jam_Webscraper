#include <iostream>
#include <cmath>

using namespace std;

void doit() {

    long long K, C, S;
    cin >> K >> C >> S;

    if (S < K) {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
    
    for (long long kk = 1; kk <= K; ++kk) {
      long long blocks_to_skip = (kk-1)*powl(K, C-1);
      long long pos_in_block = ((kk-1)*powl(K, C-2))+1;
      cout << blocks_to_skip + pos_in_block << " ";
    }

    cout << endl;
}

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #"<<t<<": ";
    doit();
  }
}
