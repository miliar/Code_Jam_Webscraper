#include <bits/stdc++.h>

using namespace std;

void print_impossible(int case_id) {
  printf("Case #%d: IMPOSSIBLE\n", case_id);
}

void print_answer(int case_id, const string &answer) {
  printf("Case #%d: %s\n", case_id, answer.c_str());
}

string rec(int n, int r, int p, int s, int flag) {
  if (n == 0) {
    if (r == 1) {
      return "R";
    } else if (p == 1) {
      return "P";
    } else {
      return "S";
    }
  }

  int dx = r + p - s;
  if (dx < 0 || dx % 2 == 1) {
    return "";
  }

  int x = dx / 2;

  int nr = r - x;
  int np = x;
  int ns = p - x;

  if (nr < 0 || ns < 0) {
    return "";
  }

  string st = rec(n - 1, nr, np, ns, flag ^ 1);
  if (st.size() == 0) {
    return "";
  }

  string t = "";
  for (char c : st) {
    if (c == 'R') {
      if (flag) {
        t += "RS";
      } else {
        t += "SR";
      }
    } else if (c == 'P') {
      if (flag) {
        t += "PR";
      } else {
        t += "PR";
      }
    } else if (c == 'S') {
      if (flag) {
        t += "PS";
      } else {
        t += "PS";
      }
    }
  }

  // cerr << n << " " << t << "\n";

  return t;
}

string rec_better_answer(const string &s) {
  if (s.size() == 1) {
    return s;
  }

  string a, b;
  for (int i = 0; i < s.size() / 2; i++) {
    a += s[i];
    b += s[s.size() / 2 + i];
  }

  a = rec_better_answer(a);
  b = rec_better_answer(b);

  return min(a + b, b + a);
}

void solve(int case_id) {
  int n, r, p, s; cin >> n >> r >> p >> s;

  string answer = rec(n, r, p, s, 1);

  if (answer.size() == 0) {
    print_impossible(case_id);
  } else {
    answer = rec_better_answer(answer);
    print_answer(case_id, answer);
  }
}

int main() {
  int cases; cin >> cases;

  for (int i = 1; i <= cases; i++) {
    solve(i);
  }

  return 0;
}