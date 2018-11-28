#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

typedef vector<int> vi; 
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
 
#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; --i)
 
#define fs first
#define sc second
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair


#define fill0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
 
int main() {
  int T;
  cin >> T;
  for (int nt = 1; nt <= T; ++nt) {
    int res = 0;
    int S;
    string s;
    cin >> S >> s;
    int cur_tot = 0;
    forn(i, S + 1) {
      if (s[i] == '0') {
        continue;
      }
      if (cur_tot >= i) {
        cur_tot += s[i] - '0';
      } else {
        res += (i - cur_tot);
        cur_tot += (i - cur_tot) + (int)(s[i] - '0');
      }
    }
    cout << "Case #" << nt << ": " << res << endl;
  }
  return 0;
}
