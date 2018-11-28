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
    string S;
    cin >> S;
    reverse(ALL(S));
    vb cake(S.length());
    REP(i, S.length()) cake[i] = S[i] == '+' ? true : false;
    bool state = false;
    int cnt = 0;
    for(bool b : cake) {
      if (state == b) {
        cnt++;
        state = !state;
      }
    }
    printf("Case #%d: %d\n", i + 1, cnt);
  }
}
