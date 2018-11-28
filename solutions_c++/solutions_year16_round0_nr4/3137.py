
#include <iostream>
#include <vector>
using namespace std;

#define LL unsigned long long int
int main() {
  int T; cin >> T;
  for (int j = 1; j <= T; j++) {
    int K, C, S; cin >> K >> C >> S;
    vector<LL> num(K, 0);
    for (int i = 1; i <= K; i++) {
      num[i-1] = i;
    }

    for (int l = 2; l <= C; l++) {
      for (int i = 0; i < K; i++) {
        num[i] = (num[i] - 1) * K + (i + 1);
      }
    }

    cout << "Case #" << j << ":";
    for (int i = 0; i < K; i++) {
      cout << " " <<  num[i];
    }
    cout << endl;
  }
  return 0;

}

