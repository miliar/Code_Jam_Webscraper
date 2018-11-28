#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii; 

#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)

int main() {
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL);
  int t;
  string s, ans;

  cin >> t;

  REP(tc, 1, t) {
    cin >> s;
    ans = "";
    
    REP(i, 0, s.size() - 1) {
      if (s[i] + ans > ans + s[i]) ans = s[i] + ans;
      else ans += s[i];
    }
    cout << "Case #" << tc << ": " << ans << endl;
  }
   
  return 0;
}

