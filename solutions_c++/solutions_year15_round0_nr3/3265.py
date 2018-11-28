#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int test_number = 0;
#define SIZE(A) (int((A).size()))
#define pb push_back
#define mp make_pair
#define gout printf("Case #%d: ", ++test_number),cout

void Update(int &x, int &s, int y) {
  if (y == '1') {

  } else if (x == '1') {
    x = y;
  } else if (x == 'i') {
    if (y == 'i') {
      x = '1';
      s = -s;
    } else if (y == 'j') {
      x = 'k';
    } else {
      x = 'j';
      s = -s;
    }
  } else if (x == 'j') {
    if (y == 'i') {
      x = 'k';
      s = -s;
    } else if (y == 'j') {
      x = '1';
      s = -s;
    } else {
      x = 'i';
    }
  } else if (x == 'k') {
    if (y == 'i') {
      x = 'j';
    } else if (y == 'j') {
      x = 'i';
      s = -s;
    } else {
      x = '1';
      s = -s;
    }
  }
}

void Main() {
  int L;
  long long X;
  string s;
  cin >> L >> X >> s;
  X = min(X, 64LL + (X%4));
  for (string add = s; --X;) {
    s += add;
  }
  string req = "ijk";
  bool noSol = 0;
  for (int id = 0, i = 0; id < 3; ++id) {
    for (int cur = '1', sgn = 1; i < SIZE(s); ++i) {
      Update(cur, sgn, s[i]);
      if (cur == req[id] && sgn == 1) {
        if (id < 2 || i == SIZE(s)-1) {
          break;
        }
      }
    }
    if (i == SIZE(s)) {
      noSol = 1;
    } else {
      ++i;
    }
  }
  gout << (noSol ? "NO" : "YES") << endl;
}

int main() {
  //std::ios_base::sync_with_stdio (false);
  int test;
  cin >> test;
  for (; test--;) {
    Main(); 
  }
  return 0;
}
