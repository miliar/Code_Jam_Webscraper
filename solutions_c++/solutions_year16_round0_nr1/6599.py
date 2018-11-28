#include <bits/stdc++.h>

#define pii pair<int, int>

#define pb push_back

#define mp make_pair

#define f first
#define s second

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

const int N = 1e2 + 10;
const int TMXN = 2e6 + 10;
const int INF = 1e9 + 7;
const ll INFL = 1e18;
const ld EPS = 0.000000000001;

int t;
int add;
int x;
int used[N];
int cnt;
int ans;
int y;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    int tt = 0;
    while (t--) {
      cout << "Case #" << ++tt << ": ";
      cin >> x;
      add = x;
      cnt = 0;
      if (x == 0) {
        cout << "INSOMNIA" << '\n';
        continue;
      }
      for (int i = x; ; i += add) {
        y = i;
        while (y != 0) {
          if (!used[y % 10]) {
            cnt++;
          }
          used[y % 10] = 1;
          y /= 10;
        }
        if (cnt == 10) {
          ans = i;
          break;
        }
      }
      cout << ans << '\n';
      for (int i = 0; i <= 9; i++) {
        used[i] = 0;
      }
    }
    return 0;
}
