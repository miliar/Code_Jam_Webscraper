#include <iostream>
using namespace std;

int main() {

  long long int T;

  cin >> T;

  for ( long long int i = 0; i < T; i++ ) {

    long long int A, B, K;

    cin >> A >> B >> K;

    long long int ans = 0;

    for ( long long int j = 0; j < A; j++ ) {

      for ( long long int l = 0; l < B; l++ ) {

	if ( ( j & l ) < K ) ans++;

      }

    }

    cout << "Case #" << i+1 << ": " << ans << endl;

  }

  return 0;

}
