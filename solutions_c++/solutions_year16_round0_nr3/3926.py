#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

bool isprime(long long x) {
  long long sq = (long long)(sqrt(x + 0.0));
  for(long long i = 2; i <= sq; i++) {
    if (x % i == 0) return false;
  }
  return true;
}

long long getvalue(string str, int k) {
  long long base = 1;
  long long value = 0;
  for(int i = 0; i < str.size(); i++) {
    value += base * (str[i] - '0');
    base *= k;
  }
  return value;
}

long long getdivisor(long long value) {
  long long sq = (long long)sqrt(value + 0.0);
  for(long long d = 2; d <= sq; d++) {
    if (value % d == 0) return d;
  }
}

int main() {
  int T;
  cin >> T;
  int n, J;
  while(T--) {
    scanf("%d %d", &n, &J);
    printf("Case #1:\n");
    for(int i = 0; i < (1 << n); i++) {
      string s = "";
      int v = i;
      while(v) {
        s += (v % 2) + '0';
        v >>= 1;
      }
      if (s[0] == '1' && (s.size() == n) && s[s.size() - 1] == '1') {
        bool satisfy = true;
        for(int k = 2; k <= 10; k++) {
          long long value = getvalue(s, k);
          if (isprime(value)) {
            satisfy = false;
            break;
          }
        }
        if (satisfy) {
          string rev = s;
          //cout << s ;
          reverse(rev.begin(), rev.end());
          cout << rev ;
          for(int k = 2; k <= 10; k++) {
            long long value = getvalue(s, k);
            // cout << "\n" << value << endl;
            cout << " " << getdivisor(value);
          }
          cout << endl;
          J --;
          if (!J) break;
        }
      }
    }
  }
  return 0;
}