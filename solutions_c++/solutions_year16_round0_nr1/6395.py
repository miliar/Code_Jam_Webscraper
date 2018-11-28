#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <unordered_map>
#include <queue>

#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))
#define MAX_N 401

using namespace std;

int res[10];

bool checkIfComplete() {
  for (int i = 0; i < 10; ++i) {
    if (res[i] == 0) {
      return false;
    }
  }
  return true;
}

void addDigit(int n) {
  while (n) {
    int d = n % 10;
    res[d] = 1;
    n = n / 10;
  }
}

int main() {
  int T;
  cin >> T;
  for (int cnt = 1; cnt <= T; ++cnt) {
    int n;
    cin >> n;
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", cnt);
      continue;
    }

    for (int i = 0; i < 10; ++i) {
      res[i] = 0;
    }
    int num = n;
    for (int i = 1; !checkIfComplete(); ++i) {
      num = n * i;
      addDigit(num);
    }
    printf("Case #%d: %d\n", cnt, num);
  }
  return 0;
}
