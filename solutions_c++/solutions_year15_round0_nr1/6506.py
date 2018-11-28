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

const bool debug = false;

int run() {
  int max;

  cin >> max;
  debug && cout << endl;
  // debug && cout << max << " ";
  int friends = 0;
  int acc = 0;
  for (int i = 0; i <= max; ++i) {
    char c;
    int cnt;

    cin >> c;
    cnt = c - '0';
    // debug && cout << cnt;

    if (i > acc) {
      debug && cout << "i: " << i << " acc: " << acc << " friends: " << friends << endl;
      friends += i - acc;
      acc += i - acc;
    }
    acc += cnt;
  }
  debug && cout << endl;
  return friends;
}

int main() {
    std::ios::sync_with_stdio(false);

    int T;
    std::cin >> T;
    for (int t = 0; t < T; t++) {
        cout << "Case #" << t + 1 << ": " << run() << endl;
    }

    return 0;
}
