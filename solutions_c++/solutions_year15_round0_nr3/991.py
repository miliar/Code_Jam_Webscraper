#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

char opt[11111][11111];
char F[4][4] = {
  {1, 'i', 'j', 'k'},
  {'i', -1, 'k', -'j'},
  {'j', -'k', -1, 'i'},
  {'k', 'j', -'i', -1},
};

char mul(char x, char y) {
  bool neg = 0;
  if (x < 0) {
    x = -x;
    neg = !neg;
  }
  if (y < 0) {
    y = -y;
    neg = !neg;
  }
  if (x == 1) {
    x = 0;
  } else {
    x = x - 'i' + 1;
  }
  if (y == 1) {
    y = 0;
  } else {
    y = y - 'i' + 1;
  }
  return (neg ? -1 : 1) * F[x][y];
}

bool solve() {
  long long l, x;
  string s;
  cin >> l >> x;
  cin >> s;
  for (long long i = 0; i < l; i++) {
    for (long long j = i; j < l; j++) {
      if (i == j) {
        opt[i][j] = s[i];
      } else {
        opt[i][j] = mul(opt[i][j - 1], s[j]);
      }
    }
  }

  char pp[4];
  pp[0] = 1;
  pp[1] = opt[0][l - 1];
  pp[2] = mul(pp[1], pp[1]);
  pp[3] = mul(pp[2], pp[1]);
  assert(mul(pp[3], pp[1]) == 1);

  vector<long long> l1[4], l2[4];
  for (long long i = 0; i < l; i++) {
    for (long long j = 0; j < 4; j++) {
      if (mul(pp[j], opt[0][i]) == 'i') {
        l1[j].push_back(i);
      }
    }
  }
  for (long long i = 0; i < l; i++) {
    for (long long j = 0; j < 4; j++) {
      if (mul(opt[i][l - 1], pp[j]) == 'k') {
        l2[j].push_back(i);
      }
    }
  }
  for (long long i = 0; i < 4; i++) {
    for (long long j = 0; j < 4; j++) {
      for (auto id1 : l1[i]) {
        for (auto id2 : l2[j]) {
          if (id1 < id2 && opt[id1 + 1][id2 - 1] == 'j' && (x - 1 - i - j) >= 0 && (x - 1 - i - j) % 4 == 0) {
            return true;
          }
          for (long long k = 0; k < 4; k++) {
            if (mul(mul(id1 + 1 < l ? opt[id1 + 1][l - 1] : 1, pp[k]), id2 > 0 ? opt[0][id2 - 1] : 1) == 'j' && (x - 2 - i - j - k) >= 0 && (x - 2 - i - j - k) % 4 == 0) {
              return true;
            }
          }
        }
      }
    }
  }
  return false;
}

int main() {
  int _;
  cin >> _;
  for (int i = 1; i <= _; i++) {
    printf("Case #%d: %s\n", i, solve() ? "YES" : "NO");
  }
}
