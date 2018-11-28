#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main() {
  int nrCases;
  cin >> nrCases;
  for(int i = 1; i <= nrCases; ++i) {
    long long K, C, S;
    cin >> K >> C >> S;
    cout << "Case #" << i <<":";

    if(S*C < K) {
      cout << " IMPOSSIBLE" << endl;
    } else if(C >= K) {
      for(long long j = 1; j <= K; ++j) cout << " " << j;
      cout << endl; 
    } else {
      for(int j = 1; j*C < K + C; ++j) {
        long long p = 1 + (j - 1) * C;
        for(long long h = 1; h < C; ++h) {
          p = K*(p-1) + min((j - 1) * C + h + 1, K);
        }
        cout << " " <<  p;
      }
      cout << endl;
    }
  }
  return 0;
}