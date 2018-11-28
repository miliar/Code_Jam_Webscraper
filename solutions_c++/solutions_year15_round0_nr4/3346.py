// Not okay

// Zhiqiang Ma (http://www.ericzma.com)
#include <iostream>
#include <iterator>
#include <iomanip>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

template<typename T>
void print_vec(std::vector<T> &v)
{
    if (v.empty()) {
        std::cout << std::endl;
    } else {
        // use std::copy
        std::copy(v.begin(), v.end() - 1, std::ostream_iterator<T>(std::cout, ", "));
        std::cout << *(v.end() - 1) << std::endl;
    }
}

using namespace std;

// const bool debug = false;
const bool debug = true;

bool run() {
  int x, r, c;
  cin >> x >> r >> c;

  if (x >= 7) return true;

  if (x > max(r, c)) return true;

  if ((r * c) % x != 0) return true;

  if ((x + 1) / 2 > min(r, c)) return true;

  if (x == 1 || x == 2 || x == 3) return false;

  if (x == 4 && min(r, c) == 2) return true;

  return false;
}

int main() {
    std::ios::sync_with_stdio(false);

    int T;
    std::cin >> T;
    for (int t = 0; t < T; t++) {
        cout << "Case #" << t + 1 << ": ";
        if (run()) {
          cout << "RICHARD" << endl;
        } else {
          cout << "GABRIEL" << endl;
        }
    }

    return 0;
}
