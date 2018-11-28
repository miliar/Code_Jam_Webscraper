/*
 *
 *
 */

#include <bits/stdc++.h>

using namespace std;

#define LOG(...) fprintf(stderr, __VA_ARGS__)
//#define LOG(...)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)
#define REP(i, n) for(int i = 0; i < (int)(n); ++i)
#define ALL(a) (a).begin(), (a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define EXIST(s, e) ((s).find(e) != (s).end())
#define SORT(c) sort(ALL(c))
#define RSORT(c) sort(RALL(c))
#define SQ(n) (n) * (n)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<pll> vpl;
typedef vector<ll> vll;
typedef vector<vb> vvb;
typedef vector<vi> vvi;
typedef vector<vll> vvll;

int main() {
  int T;
  cin >> T;
  REP(i, T) {
    ll N;
    cin >> N;
    if (N == 0) {
      printf("Case #%d: INSOMNIA\n", i + 1);
      continue;
    }
    set<char> app;
    int n = 0;
    n++;
    for(; app.size() != 10; n++) {
      string s = to_string(N * n);
      for(char c : s) {
        app.insert(c);
      }
      // cout << N * n << endl;
    }
    n--;
    printf("Case #%d: %lld\n", i + 1, N * n);
  }
}
