#include <iostream>
#include <bitset>

using namespace std;

int main() {
  int T; 
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #"<<t<<": ";
    unsigned int A, B, K;
    cin >> A >> B >> K;

    unsigned int count = 0;

    for (unsigned int a = 0; a < A; ++a) {
      for (unsigned int b = 0; b < B; ++b) {
        if ((a&b) < K) count++;
      }
    }
    cout << count << endl;

  }
}
