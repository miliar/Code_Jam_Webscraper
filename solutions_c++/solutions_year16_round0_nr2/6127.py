#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

const int inf = 1e9;

int solve(string s) {
  int n = s.length();
  vi a(n);
  forn(i, n) a[i] = (s[i] == '+');
  int r = 0;
  while (!a.empty()) {
    // forn(i, a.size()) cout << (a[i] ? '+' : '-'); cout << '\n';
    while(!a.empty() && a.back() == 1) a.pop_back();
    if (!a.empty()) {
      r += 1;
      for(int& x: a) x = 1 - x;
      // reverse(a.begin(), a.end());
    }
  }
  return r;
} 

int main() {
  int T;
  cin >> T;
  forn(t, T) {
    string s;
    cin >> s;
    cout << "Case #" << t + 1 << ": ";
    int r = solve(s);
    cout << r << '\n';
  }
  return 0;
}
