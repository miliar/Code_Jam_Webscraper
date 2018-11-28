#include <iostream>
#include <bitset>

typedef long long llong;

using namespace std;

int main () {
  int testc;
  cin >> testc; /* garbage */
  cout << "Case #1:" << endl;

  int length, cnt;
  cin >> length >> cnt;

  llong cur = (1LL << (length / 2 - 1)) + 1;
  for (int i = 0; i < cnt; i++) {
    for (int j = length / 2 - 1; j >= 0; j--) {
      cout << (cur & 1LL << j ? "1" : "0") << (cur & 1LL << j ? "1" : "0");
    }
    
    for (int j = 3; j <= 11; j++) {
      cout << " " << j;
    }
    cout << endl;

    cur += 2;
  }
}
