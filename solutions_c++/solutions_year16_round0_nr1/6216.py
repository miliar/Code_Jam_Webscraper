#include <iostream>
#include <vector>
using namespace std;

int main() {
  int t; cin >> t;
  for (int i = 1; i <= t; ++i) {
    long n; cin >> n;
    if (n == 0) {
      cout << "Case #" << i << ": INSOMNIA" << endl;
      continue;
    }
    vector<bool> seen(10, false);
    int num_seen = 0;
    long x = 0;
    while (num_seen < 10) {
      x += n;
      long x_copy = x;
      while (x_copy) {
	if (!seen[x_copy % 10]) {
	  seen[x_copy % 10] = true;
	  ++num_seen;
	}
	x_copy = x_copy / 10;
      }
    }
    cout << "Case #" << i << ": " << x << endl;
  }
}
