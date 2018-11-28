#include <iostream>
#include <string>
#include <vector>
#include <array>

using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define PATH "C:\\Users\\Valentin\\Desktop\\cpp\\"

template<typename T>
int sz(const T& t) {
  return static_cast<int>(t.size());
}
  
void solve() {
  string s;
  int k;
  cin >> s >> k;
  
  
  int ans = 0;
  for (int i = 0; i + k <= sz(s); ++i) {
    if (s[i] == '-') {
      forn (j, k) {
        s[i + j] ^= ('-' ^ '+');
      }
      ans++;
    }
  }
  
  for (char c : s) {
    if (c == '-') {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  cout << ans << endl;
}

int main() {
  freopen(PATH"in.txt", "r", stdin);
  freopen(PATH"out.txt", "w", stdout);

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;
  forn (i, t) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }  
  
  cout.flush();
  return 0;
}