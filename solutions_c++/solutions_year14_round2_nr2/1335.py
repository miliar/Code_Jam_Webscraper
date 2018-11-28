#include <iostream>

using namespace std;

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int A, B, K;
    cin >> A;
    cin >> B;
    cin >> K;
    int total_cnt = 0;
    for (int j = 0; j < A; ++j) {
      for (int k = 0; k < B; ++k) {
        int candidate = j & k;
        if (candidate < K) {
          total_cnt++;
        }
      }
    }
    cout << "Case #" << i << ": " << total_cnt << endl;
  }
  return 0;
}
