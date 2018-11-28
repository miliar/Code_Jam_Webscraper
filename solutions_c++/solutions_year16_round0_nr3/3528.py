#include <bits/stdc++.h>
using namespace std;
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
typedef unsigned long long ull;

int T;

ull f(string s, int base) {
  ull num = 0;
  for (int i = 0; i < (int) s.size(); i++) {
    num = num * base + s[i] - '0';
  }
  return num;
}

string toBinary(ull num, int sz) {
  string s = "";
  while (num != (ull) 0) {
    s += num % 2 + '0';
    num /= 2;
  }
  int rest = sz - (int) s.size();
  for (int i = 0; i < rest; i++) {
    s += "0";
  }
  reverse(s.begin(), s.end());
  return s;
}

bool isPrime(ull num) {
  if (num < 2) return false;
  if (num == 2) return true;
  if (num % 2 == 0) return false;
  for (ull i = 3; i * i <= num; i += 2) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

int main() {
#ifdef msci
  //freopen("input.txt", "r", stdin);
#endif
  cin >> T;
  for (int t = 1; t <= T; t++) {
    printf("Case #%d:\n", t);
    fflush(stdout);
    // begin solution
    int N, J; 
    cin >> N >> J;
    vector<ull> divisors;
    for (ull j = 0; j < (ull) ((ull) 1 << (ull) (N - 2)); j++) {
      if (J <= 0) {
        break;
      }
      divisors.clear();
      string current = "1" + toBinary(j, N - 2) + "1";
      bool flag = false;
      for (int base = 2; base <= 10; base++) {
        ull num = f(current, base);
        if (isPrime(num)) {
          flag = true;
          break;
        } else {
          for (ull k = 2; k < num; k++) {
            if (num % k == 0) {
              divisors.push_back(k);
              break;
            }
          }
        }
      }
      if (!flag) {
        J--;
        cout << current;
        // print the divisors
        for (int i = 0; i < (int) divisors.size(); i++) {
          cout << " " << divisors[i];
        }
        cout << endl;
      }
    }
  }
  return 0;
}
