#include <bits/stdc++.h>
#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define FOR(i,n,m) for (int i=n; i<(int)(m); ++i)
#define ALL(x) x.begin(), x.end()
#define chmax(a, b) a = max(a, b)
#define chmin(a, b) a = min(a, b)
#define in(i, n) (0 <= (i) && (i) < (n))
#define on(bit, i) (((bit >> i) & 1) == 1)

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;
const int INF = 1e9+7;

int T, CASE = 1;
string str;

int main(void) {
  cin >> T;
  while(T--) {
    cin >> str;
    int res = 0;
    REP(i, str.size() - 1) if (str[i] != str[i + 1]) res++;
    if (str[str.size() - 1] == '-') res++;
    cout << "Case #" << CASE++ << ": " << res << endl;
  }
  return 0;
}
