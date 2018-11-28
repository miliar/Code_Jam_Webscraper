#include <bits/stdc++.h>

using namespace std;

#ifdef ACMTUYO
struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#else
struct RTC{};
#define DBG(X)
#endif

#define fast_io() ios_base::sync_with_stdio(false)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long int number;
string s;
string greedy() {
  deque<char> cad;
  cad.push_back(s[0]);
  for (int i = 1; i < sz(s); i++) {
    char c = s[i];
    if (c >= cad.front())
      cad.push_front(c);
    else
      cad.push_back(c);
  }
  return string(all(cad));
}
int main() {
  fast_io();
  int t;
  cin >> t;
  for (int caso = 1; caso <= t; caso++) {
    cin >> s;
    cout << "Case #" << caso << ": ";
    string g = greedy();
    cout << g << '\n';
  }
  return 0;
}

