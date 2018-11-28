#include <iostream>
#include <bitset>

using namespace std;

bitset<10> bs;

int counting_sheep(int n) {
  if (n == 0) return 0;

  int i = n;
  while (n > 0) {
    int m = n;
    while (m) {
      bs.set(m % 10);
      m /= 10;
      if (bs.count() == 10)
        return n;
    }
    n += i;
  }

  return n;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    int n;
    cin >> n;
    bs.reset();
    n = counting_sheep(n);
    if (n <= 0)
      cout << "Case #" << i << ": INSOMNIA" << endl;
    else
      cout << "Case #" << i << ": " << n << endl;
  }
}
