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

int X, R, C;

int main(void) {
  int TestCase, TC = 0;
  cin >> TestCase;
  while(TestCase != TC) {
    cout << "Case #" << ++TC << ": ";
    cin >> X >> R >> C;
    if (X >= 7 || (R * C) % X != 0) { cout << "RICHARD" << endl; continue; }
    if (X == 1 || X == 2) { cout << "GABRIEL" << endl; continue; }
    if (X == 3) {
      if (R >= 2 && C >= 2) { cout << "GABRIEL" << endl; continue; }
      else { cout << "RICHARD" << endl; continue; }
    }
    if (X == 4) {
      if (R >= 3 && C >= 3) { cout << "GABRIEL" << endl; continue; }
      else { cout << "RICHARD" << endl; continue; }
    }
  }
  return 0;
}
