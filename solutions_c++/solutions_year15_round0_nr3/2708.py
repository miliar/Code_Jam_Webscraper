#include <iostream>

#include <cstdio>

using namespace std;

char tbl[4][4] = {{'O', 'I', 'J', 'K'},
                  {'I', 'o', 'K', 'j'},
                  {'J', 'k', 'o', 'I'},
                  {'K', 'J', 'i', 'o'}};

bool sign(char c) {
  return c >= 'A' && c <= 'Z';
}

int code(char c) {
  switch (c) {
    case 'o': return 0;
    case 'O': return 0;
    case 'i': return 1;
    case 'I': return 1;
    case 'j': return 2;
    case 'J': return 2;
    default:  return 3;
  }
}

char syms[4] = {'o', 'i', 'j', 'k'};
char sym(char a, bool sign1) {
  if (!sign1) {
    if (!sign(a)) return a - 'a' + 'A'; 
    return a - 'A' + 'a';
  }
  return a;
}

char mul(char a, char b) {
  return sym(tbl[code(a)][code(b)], sign(a) == sign(b));  
}

char c[10000];

void main2() {
  int l = 3, x = 1;
  cin >> l >> x;
  string s = "ijk";
  cin >> s;
  for (int i = 0; i < l; ++i)
    for (int j = 0; j < x; ++j)
     c[j * l + i] = s[i] - 'a' + 'A';

  char cur = c[0];
  int ok = c[0] == 'I' ? 1 : 0;
  //cout << cur << '\n';
  for (int i = 1; i < l * x - 1; ++i) {
    cur = mul(cur, c[i]);
    //cout << cur << '\n';
    if (ok == 0) { if (cur == 'I') ++ok; }
    else if (ok == 1) { if (cur == 'K') ++ok; }
  }
  //cout << mul(cur, c[l * x - 1]) << '\n';
  if (ok == 2 && mul(cur, c[l * x - 1]) == 'o') {
    cout << "YES\n";
  } else {
    cout << "NO\n";
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  freopen("C-small-0.in", "r", stdin);
  freopen("C-small-0.out", "w", stdout);

  int T = 1; 
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ": ";
    main2();
  }
}
