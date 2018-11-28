#include <iostream>

using ul = unsigned __int64;
using namespace std;

int T;

int main(void) {
  cin >> T;
  for (int i = 0; i < T; i++) {
    int table[10];
    int count = 10;
    int it = 0;
    for (int i = 0; i < 10; i++) table[i] = 1;
    ul N; cin >> N;

    cout << "Case #" << (i + 1) << ": ";
    if (N == 0) {
      cout << "INSOMNIA" << endl;
      continue;
    }
    do {
      it++;
      ul target = N * it;
      while (target != 0) {
        int r = target % 10;
        target /= 10;
        count -= table[r];
        table[r] = 0;
      }
    } while (count != 0);
    cout << (N * it) << endl;
  }
  return 0;
}