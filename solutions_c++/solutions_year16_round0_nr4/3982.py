#include <iostream>
#include <map>
#include <cstring>
#include <climits>

using namespace std;

int main(int argc, char **argv) {
  int T, K, C, S;

  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> K >> C >> S;
    cout << "Case #" << i+1 << ": ";
    for (int j = 1; j <= K; ++j) {
      cout << j;
      if (j != K) {
        cout << " ";
      }
    }
    cout << endl;
  }
  return 0;
}

