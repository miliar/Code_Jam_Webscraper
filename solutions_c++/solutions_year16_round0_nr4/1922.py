#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <map>
#include <sstream>
#include <string>
// www.boost.org
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/utility/binary.hpp>
using namespace std;

void cleanSet(int k, int c, int s) {
  for (int i = 1; i <= s; i++) {
    cout << i;

    if (i < s) {
      cout << " ";
    }
  }
  // cout << "IMPOSSIBLE";
}

int main() {
  int t;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; i++) {
    int k, c, s;
    cin >> k >> c >> s;

    cout << "Case #" << i << ": ";
    cleanSet(k, c, s);

    cout << endl;
  }
}
