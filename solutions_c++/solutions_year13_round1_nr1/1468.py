#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for( int i = 1; i <= T; ++i ) {
    long long r, t;
    cin >> r >> t;
    long long N = 0;
    while( t >= (2*r+1) ) {
      ++N;
      t -= (2*r+1);
      r+=2;
    }
    cout << "Case #" << i << ": " << N << endl;
  }
  return 0;
}
