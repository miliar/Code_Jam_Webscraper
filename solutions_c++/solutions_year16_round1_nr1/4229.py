#include <iostream>
#include <map>
#include <vector>

using namespace std;

string solve(string& s, int l, int r, bool recurse) {
  char m = 'A';
  int index = l;

  if (l >= r) {
    string res;
    res += s[r];
    return res;
  }

  for (int i = l; i <= r; ++i) {
    char c = s[i];
    if (c > m) {
      m = c;
      index = i;
    }
  }

  string res;
  if ((index == l) || (!recurse)) {
    for (int i = l; i <= r; ++i) {
      char c = s[i];
      if (c == m) {
        res = c + res;
      } else {
        res = res + c;
      }
    }
  } else {
    res += m;
    for (int i = index+1; i <= r; ++i) {
      char c = s[i];
      if (c == m) {
        res = c + res;
      }
    }
    res = res + solve(s, l, index - 1, true);
    for (int i = index+1; i <= r; ++i) {
      char c = s[i];
      if (c != m) {
        res = res + c;
      }
    }
  }

  return res;
}

int main(int argc, char **argv) {
  int T;

  cin >> T;
  for (int i = 0; i < T; ++i) {
    string s;
    cin >> s;
    cout << "Case #" << i+1 << ": ";
    string r = solve(s, 0, s.size() - 1, true);
    cout << r << endl;
  }
  return 0;
}

