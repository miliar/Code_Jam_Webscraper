#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

int main() {
  cin.sync_with_stdio(false);

  int t;
  cin >> t;

  for (int test = 1; test <= t; test++) {
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();

    int ans = 0;
    for (int i = 0; i < n - k + 1; i++) {
      if (s[i] == '-') {
        ans++;
        for (int j = i; j < i + k; j++) {
          if (s[j] == '-') {
            s[j] = '+';
          } else {
            s[j] = '-';
          }
        }
      }
    }

    for (int i = 0; i < n; i++) {
      if (s[i] == '-') {
        ans = -1;
        break;
      }
    }

    cout << "Case #" << test << ": ";
    if (ans == -1) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << ans << '\n';
    }
  }

  return 0;
}
