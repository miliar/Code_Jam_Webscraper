#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>

#define DEBUGLEVEL
#ifdef DEBUGLEVEL
#define dbg(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define dbg(fmt, args...)
#endif
#define REPS(i, s, n) for(int (i) = (s); (i) < (int)(n); ++(i))
#define REP(i, n) REPS(i, 0, n)
#define pb push_back
#define pii pair<int, int>
#define pll pair<ll, ll>
#define mp make_pair
#define x first
#define y second
#define INFI 1234567890
#define INFL 1234567890123456789LL
typedef long long ll;

using namespace std;

string world[200];
char dchi[] = {'<', '^', '>', 'v'};
int dy[] = {0, -1, 0, 1};
int dx[] = {-1, 0, 1, 0};

inline int get_di(char c) {
  REP(i, 4) {
    if (dchi[i] == c) {
      return i;
    }
  }
  return -1;
}

int main() {
#ifdef DEBUG
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
#endif
    int _test_count;
    cin >> _test_count;
    REP(_test_i, _test_count) {
        dbg("Processing test %d\n", _test_i + 1);
        int r, c;
        cin >> r >> c;
        REP(i, r) {
          cin >> world[i];
        }
        int possible = 1;
        int ans = 0;
        REP(i, r) {
          if (!possible) {
            break;
          }
          REP(j, c) {
            int di = get_di(world[i][j]);
            if (di == -1) {
              continue;
            }
            int mask_ok = 0;
            REP(d, 4) {
              int ni = i + dy[d];
              int nj = j + dx[d];
              while (0 <= ni && ni < r &&
                     0 <= nj && nj < c &&
                     world[ni][nj] == '.') {
                ni += dy[d];
                nj += dx[d];
              }
              if (0 <= ni && ni < r && 0 <= nj && nj < c) {
                mask_ok |= (1 << d);
              }
            }
            if (mask_ok == 0) {
              possible = 0;
            } else {
              ans += ((mask_ok & (1 << di)) == 0);
            }
          }
        }
        printf("Case #%d: ", _test_i + 1);
        if (possible) {
          printf("%d\n", ans);
        } else {
          printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}