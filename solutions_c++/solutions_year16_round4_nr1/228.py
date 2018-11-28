#include <bits/stdc++.h>

using namespace std;

int A, B, C;
map<string, string> from;

string S(int A, int B, int C) {
  return string(A, 'P') + string(B, 'R') + string(C, 'S');
}

void pre() {
  from["R"] = "RS";
  from["S"] = "SP";
  from["P"] = "PR";
}

void read() {
  int n;
  cin >> n;
  cin >> B >> A >> C;
}

bool good(int A, int B, int C) {
  int sum = (A + B + C);
  if (sum == 1)
    return true;
  sum /= 2;
  int bc = sum - A;
  int ca = sum - B;
  int ab = sum - C;
  if (bc < 0 || ca < 0 || ab < 0)
    return false;
  return good(ab, bc, ca);
}

string get(int A, int B, int C) {
  int sum = (A + B + C);
  if (sum == 1) {
    return S(A, B, C);
  }
  sum /= 2;
  int bc = sum - A;
  int ca = sum - B;
  int ab = sum - C;
  string p = get(ab, bc, ca);
  string s = "";
  for (int i = 0; i < (int) p.length(); ++i)
    s += from[p.substr(i, 1)];
  return s;
}

string norm(string s) {
  if (s.length() == 1)
    return s;
  int m = s.length() / 2;
  string A = s.substr(0, m);
  string B = s.substr(m, m);
  A = norm(A);
  B = norm(B);
  return min(A + B, B + A);
}

void kill() {
  if (!good(A, B, C)) {
    cout << "IMPOSSIBLE\n";
    return ;
  }


  string s = get(A, B, C);
  s = norm(s);
  cout << s << endl;
}

int main() {
  pre();
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}
