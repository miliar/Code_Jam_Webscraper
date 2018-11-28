#include <iostream>
#include <bitset>

using namespace std;

void getDigits(bitset<10>* ds, int n) {
  (*ds)[n%10] = 1;
  while (n /= 10) {
    (*ds)[n%10] = 1;
  }
}

int main() {
  ios::sync_with_stdio(false);

  int k;
  cin >> k;
  int m = k;

  while (k--) {
    bool fini = false;
    bitset<10> ds;
    int n;
    cin >> n;
    if (n == 0) {
      cout << "Case #" << m - k << ": INSOMNIA" << endl;
      fini = true;
    }
    int i = 0;

    while (!fini) {
      i++;
      int a = n * i;
      getDigits(&ds, a);
      if (ds.all()) {
        cout << "Case #" << m - k << ": " << a << endl;
        fini = true;
      }
    }
  }
}
