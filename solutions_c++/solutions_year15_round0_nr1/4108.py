#include <bits/stdc++.h>
#define pb push_back
#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define ALL(x) x.begin(), x.end()
#define chmax(a, b) a = max(a, b)
#define chmin(a, b) a = min(a, b)

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
const int INF = 1 << 29;

int main(void) {
  int TestCase, TC = 0;
  cin >> TestCase;
  while(TestCase != TC) {
    int S;
    string nums;
    cin >> S >> nums;
    int res = 0;
    REP(i, S + 1) {
      if (i > res) res = i;
      res += nums[i] - '0';
    }
    REP(i, S + 1) res -= nums[i] - '0';
    cout << "Case #" << ++TC << ": ";
    cout << res << endl;
  }
  return 0;
}
