#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

enum {
  ONE = 1,
  I = 2,
  J = 3,
  K = 4
};

int mt[4][4] = {
  {ONE, I, J, K},
  {I, -ONE, K, -J},
  {J, -K, -ONE, I},
  {K, J, -I, -ONE}
};

int signum(int x) {
  return x < 0 ? -1 : x > 0;
}

int multiply(int a, int b) {
  return signum(a) * signum(b) * mt[abs(a)-1][abs(b)-1];
}

int solve(int a, int b, int c) {
  for (int x = -K; x <= K; x++) {
    if (x == 0) continue;
    int ta = (a == 0) ? x : a;
    int tb = (b == 0) ? x : b;
    int tc = (c == 0) ? x : c;
    if (multiply(ta, tb) == tc)
      return x;
  }
  return 0;
}

int divide(int a, int b) {
  return solve(0, b, a);
}

bool separable(const vector<int>& s) {
  bool found_k = false;
  bool found_jk = false;
  int curr = ONE;
  for (int i = s.size() - 1; i > 0; i--) {
    curr = multiply(s[i], curr);

    if (curr == K)
      found_k = true;
    if (curr == multiply(J, K) && found_k)
      found_jk = true;
  }

  return multiply(s[0], curr) == multiply(multiply(I, J), K) && found_jk;
}

int parse(char c) {
  switch (c) {
    case 'i': return I;
    case 'j': return J;
    case 'k': return K;
  }
  return 0;
}

vector<int> generate(const string& s, int x) {
  vector<int> v(s.size() * x);
  for (int i = 0; i < v.size(); i++)
    v[i] = parse(s[i % s.size()]);
  return v;
}

int main() {
  ios::sync_with_stdio(false);

  int t;
  cin >> t;

  for (int tc = 1; tc <= t; tc++) {
    int x, l;
    cin >> l >> x;
    string s;
    cin >> s;

    string res;

    bool possible = false;

    for (int a = 0; a <= 3; a++) {
      // Case 1: 'j' is formed using a substring of s.
      {
        int c = x - 1 - a;

        if (c >= 0) {
          auto v = generate(s, a + 1 + (c % 4));
          if (separable(v))
            possible = true;
        }
      }

      // Case 2: 'j' breaks the boundaries of s.
      for (int b = 0; b <= 3; b++) {
        int c = x - 2 - a - b;

        if (c >= 0) {
          auto v = generate(s, a + b + 2 + (c % 4));

          if (separable(v))
            possible = true;
        }
      }
    }

    cout << "Case #" << tc << ": " << (possible ? "YES" : "NO") << '\n';
  }

  return 0;
}
