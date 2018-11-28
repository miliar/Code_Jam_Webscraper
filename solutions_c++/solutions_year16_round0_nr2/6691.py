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
int mn = N;
int cnt;
int tt;
string s;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    while (t--) {
        tt++;
        cin >> s;
        int cnt = 0;
        int need = 0;
        for (int i = s.size() - 1; i >= 0; i--) {
            cnt = 0;
            for (int j = 0; j < s.size(); j++) {
              if (s[j] == '-') {
                cnt++;
              }
            }
            if (!cnt) {
              break;
            }
            if (s[0] != '-') {
              need++;
              for (int j = 0; j < s.size(); j++) {
                if (s[j] == '+') {
                  s[j] = '-';
                } else {
                  break;
                }
              }
            }
            if (s[i] == '-') {
              need++;
              for (int j = 0; j <= i; j++) {
                if (s[j] == '-') {
                  s[j] = '+';
                } else {
                  s[j] = '-';
                }
              }
              reverse(s.begin(), s.begin() + i + 1);
            }
        }
        cout << "Case #" << tt << ": " << need << '\n';
    }
    return 0;
}
