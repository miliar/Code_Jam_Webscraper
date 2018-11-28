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

int CASE = 1;
ll T, N;

int main(void) {
  cin >> T;
  while(T--) {
    cin >> N;
    if (N == 0) {
      cout << "Case #" << CASE++ << ": INSOMNIA" << endl;
      continue;
    }
    set<int> st;
    for (int i = 1; i <= 10000000; i++) {
      stringstream ss;
      ss << (N * i);
      string str = ss.str();
      REP(i, str.size()) st.insert(str[i]);
      if (st.size() == 10) {
	cout << "Case #" << CASE++ << ": " << (N * i) << endl;
	break;
      }
    }
  }
  return 0;
}
