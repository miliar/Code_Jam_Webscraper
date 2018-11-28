#include <iostream>
#include <cassert>
#include <string>
#include <map>
#include <vector>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

void solve(int test) {
  string a, b;
  cin >> a >> b;
  string ra, rb;
  string ca, cb;
  long long res = 1LL << 62;
  for (int i = 0; i < (int)a.size(); i++) {
    for (int ac = 0; ac < 10; ac++) {
      for (int bc = 0; bc < 10; bc++) {
        if (a[i] != '?' && (a[i] - '0') != ac) continue;
        if (b[i] != '?' && (b[i] - '0') != bc) continue;
        ca = a;
        cb = b;
        long long av = 0;
        long long bv = 0;
        int fail = 0;
        for (int j = 0; j < i; j++) {
          av *= 10;
          bv *= 10;
          if (a[j] == '?' && b[j] == '?') {
            ca[j] = cb[j] = '0';
            continue;
          }
          if (a[j] == '?') {
            av += b[j] - '0';
            bv += b[j] - '0';
            ca[j] = b[j];
            cb[j] = b[j];
            continue;
          }
          if (b[j] == '?') {
            av += a[j] - '0';
            bv += a[j] - '0';
            ca[j] = a[j];
            cb[j] = a[j];
            continue;
          }
          if (a[j] != b[j]) {
            fail = 1;
            break;
          }
          ca[j] = a[j];
          cb[j] = b[j];
        }
        if (fail) continue;
        av *= 10;
        bv *= 10;
        av += ac;
        bv += bc;
        ca[i] = ac + '0';
        cb[i] = bc + '0';
        for (int j = i + 1; j < (int)a.size(); j++) {
          av *= 10;
          bv *= 10;
          if (av <= bv) {
            if (a[j] != '?') {
              av += a[j] - '0';
              ca[j] = a[j];
            } else {
              av += 9;
              ca[j] = '9';
            }
            if (b[j] != '?') {
              bv += b[j] - '0';
              cb[j] = b[j];
            } else {
              cb[j] = '0';
            }
          } else {
            if (a[j] != '?') {
              av += a[j] - '0';
              ca[j] = a[j];
            } else {
              ca[j] = '0';
            }
            if (b[j] != '?') {
              bv += b[j] - '0';
              cb[j] = b[j];
            } else {
              bv += 9;
              cb[j] = '9';
            }
          }
        }
        long long cur = abs(av - bv);
        if (cur < res) {
          res = cur;
          ra = ca;
          rb = cb;
        }
        if (cur == res && (ca < ra || (ca == ra && cb < rb))) {
          ra = ca;
          rb = cb;
        }
      }
    }
  }
  printf("Case #%d: %s %s\n", test, ra.c_str(), rb.c_str());
  eprintf("res = %lld\n", res);
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
