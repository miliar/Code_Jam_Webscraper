#include <iostream>

using namespace std;

int
main() {
  int T;

  cin >> T;

  for(int i = 1; i <= T; i++) {
    int A, B, K;
    int n = 0;

    cin >> A >> B >> K;

    for(int a = 0; a < A; a++) {
      for(int b = 0; b < B; b++) {
	if((a&b) < K) {
	  n++;
	}
      }
    }

    cout << "Case #" << i << ": " << n << endl;
  }

  return 0;
}

