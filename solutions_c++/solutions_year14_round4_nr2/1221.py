#include <algorithm>
#include <iostream>
#include <vector>

int Sort(std::vector<int> a) {
  int n = a.size();
  int c = 0;
  for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
      if (a[j] == i) {
        c += j - i;
        for (int k = j; k > i; k--) {
          a[k] = a[k - 1];
        }
        a[i] = i;
        break;
      }
    }
  }
  return c;
}

int main() {
  int t;
  std::cin >> t;
  for (int x = 1; x <= t; x++) {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    std::vector<int> p(n);
    for (int i = 0; i < n; i++) {
      std::cin >> a[i];
      p[i] = i;
    }
    int y = -1;
    do {
      bool up = true;
      bool valid = true;
      for (int i = 0; i < n - 1; i++) {
        int u = a[p[i]];
        int v = a[p[i + 1]];
        if (up && u > v) {
          up = false;
        } else if (!up && u < v) {
          valid = false;
          break;
        }
      }
      if (valid) {
        int z = Sort(p);
        if (y == -1 || z < y) {
          y = z;
        }
      }
    } while (std::next_permutation(p.begin(), p.end()));
    std::cout << "Case #" << x << ": " << y << std::endl;
  }
}
