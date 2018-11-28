#include <string>
#include <iostream>
#include <vector>

using namespace std;

void out(int x) {
  if (x < 0) {
    cout << "-";
    x = -x;
  }
  if (x == 1) {
    x = 49;
  }
  cout << (char)x;
}

int abx (int a, int b) {
  int sign = (a < 0 ? -1 : 1) * (b < 0 ? -1 : 1);
  a = (a < 0 ? -a : a);
  b = (b < 0 ? -b : b);
  if (a == 1)
    return b * sign;
  if (b == 1)
    return a * sign;

  if (a == b)
    return -1 * sign;

  switch (a) {
    case 'i':
      switch (b) {
        case 'j':
          return 'k' * sign;
        case 'k':
          return -1 * 'j' * sign;
      }
    case 'j':
      switch (b) {
        case 'i':
          return -1 * 'k' * sign;
        case 'k':
          return 'i' * sign;
      }
    case 'k':
      switch (b) {
        case 'i':
          return 'j' * sign;
        case 'j':
          return -1 * 'i' * sign;
      }
  }

  cerr << "FAIL" << endl;
  exit(0);
}

int axb (int a, int b) {
  for (int i = 0; i < 2; i++) {
    int sign = (i ? 1 : -1);
    for (int j = 0; j < 4; j++) {
      int v[] = {1, 'i', 'j', 'k'};
      int x = sign * v[j];
      if (abx(a, x) == b)
        return x;
    }
  }

  cerr << "FAIL" << endl;
  exit(0);
}

int main () {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    long long L, X;
    string s;
    cin >> L >> X >> s;
    string ss(s);

    for (int i = 0; i < X; i++)
      s += ss;

    int pro = 1;
    vector<int> prefix;
    for (int i = 0; i < L * X; i++) {
      pro = abx(pro, s[i]);
      prefix.push_back(pro);
    }

    int good = false;
    for (int i = 0; i < L * X - 2; i++) {
      if (prefix[i] != 'i') continue;
      for (int j = i + 1; j < L * X - 1; j++) {
        int middle = axb(prefix[i], prefix[j]);
        int end = axb(prefix[j], pro);
        if (middle == 'j' && end == 'k') {
          good = true;
        }
      }
    }

    cout << "Case #" << tt << ": " << (good ? "YES" : "NO") << endl;
  }
}


