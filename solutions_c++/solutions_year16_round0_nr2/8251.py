#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii; 

#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)
#define TRmsi(c, it) for (msi::iterator it = (c).begin(); it != (c).end(); it++)

int t;
string s, clean;

int main() {
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL);
  cin >> t;

  REP(tt, 1, t) {
    cin >> s;

    clean = "";
    REP(i, 0, s.size() - 1)
      if (!i || s[i] != clean[clean.size() - 1])
        clean += s[i];

    int ans = 0;
    REP(j, 0, clean.size() - 1) {
      if (clean[j] == '-' && !j) ans += 1;
      else if (clean[j] == '-') ans += 2;
    }

    cout << "Case #" << tt << ": ";
    cout << ans << endl;
  }
  return 0;
}

