#include <string>
#include <iostream>
#include <vector>

using namespace std;

int nextInt() {
  int x;
  scanf("%d", &x);
  return x;
}

string nextstring() {
  char buf[11111];
  scanf("%s", buf);
  return buf;
}


void rec(string& s, int at, string cur, string& best) {
  if (at == s.length()) {
    best = max(best, cur);
    return;
  }
  rec(s, at + 1, cur + s[at], best);
  rec(s, at + 1, s[at] + cur, best);
}

string slow(string s) {
  string best = "";
  rec(s, 0, "", best);
  return best;
}

string fast(string s) {
  string best = "";
  for (int i = 0; i < s.size(); ++i) {
    string a = best;
    a += s[i];
    string b = "";
    b += s[i];
    b += best;
    best = max(a, b);
  }
  return best;
}

string randString(int n) {
  string res;
  for (int i = 0; i < n; ++i) {
    res += rand() % 26 + 'A';
  }
  return res;
}

int main() {
  // for (int i = 0; i < 10000; ++i) {
  //   string s = randString(10);
  //   string r1 = slow(s);
  //   string r2 = fast(s);
  //   if (r1 == r2) cerr << "."; else cerr << "!";
  // }

  int T = nextInt();
  for (int test_number = 1; test_number <= T; ++test_number) {
    cerr << test_number << endl;
    string s = nextstring();
    string res = fast(s);
    printf("Case #%d: %s\n", test_number, res.c_str());
  }
  return 0;
}
