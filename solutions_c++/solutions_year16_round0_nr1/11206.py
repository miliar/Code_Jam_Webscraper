#include <iostream>

using namespace std;

bool arra[10];
int T, n;

void update_array(int x) {
  while (x > 0) {
    arra[x % 10] = true;
    x /= 10;
  }
}

bool verify_array() {
  for (int i = 0; i < 10; i++) if (!arra[i]) return false;
  return true;
}

void main2() {
  if (n == 0) {
    cout << "INSOMNIA" << endl;
    return;
  }
  for (int i = 0; i < 10; i++) arra[i] = false;
  int i;
  for (i = 1; !verify_array(); i++) {
    update_array(i * n);
  }
  cout << (i - 1) * n << endl;
}

int main() {
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cin >> n;
    cout << "Case #" << i << ": ";
    main2();
  }
  return 0;
}