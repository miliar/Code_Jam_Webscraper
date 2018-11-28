#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <cmath>

int INF = 2147483647;
double INFD = 2147483647;

double PI = 3.14159265359;

using namespace std;

void Digits(unsigned long long n, set<char>& digits) {
  stringstream str;
  str << n;
  int i = 0;
  while (i < str.str().size()) {
    digits.insert(str.str()[i]);
    i++;
  }
}

int main() {
  int i = 0, t = 0;
  cin >> t;
  while (i < t) {
    unsigned long long n = 0;
    cin >> n;
    cout << "Case #" << ++i << ": ";
    if (n == 0) {
      cout << "INSOMNIA";
    } else {
      unsigned long long total = n;
      set<char> digits;
      Digits(n, digits);
      while (digits.size() < 10) {
        total += n;
        Digits(total, digits);
      }
      cout << total;
    }
    cout << endl;
  }

  return 0;
}
