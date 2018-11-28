#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <memory.h>
#include <cmath>

#define MAXN 40

using namespace std;

int main () {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int test, cnt = 0;

  cin >> test;

  while (test > 0) {
    cnt++;
    test--;

    int k, c, s;

    cin >> k >> c >> s;

    cout << "Case #" << cnt << ": ";

    for (int i = 1; i <= s; ++i) {
      cout << i << " ";
    }

    cout << endl;
  }

  return 0;
}
