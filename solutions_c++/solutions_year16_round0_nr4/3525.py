#include <iostream>
using namespace std;

int main() {
  int T, K, C, S;
  cin >> T;
  for (int x=1; x<=T; ++x) {
    cin >> K >> C >> S;
    cout << "Case #" << x << ":";
    for (int i=1; i<=K; ++i) {
      cout << " " << i;
    }
    cout << endl;
  }
  return 0;
}
