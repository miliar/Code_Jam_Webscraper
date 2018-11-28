#include <set>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <climits>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#define MID(x,y) ( ( x + y ) >> 1 )
#define L(x) ( x << 1 )
#define R(x) ( x << 1 | 1 )
#define REP(i,t) for(int i=0; i<(t); i++)
#define FOR(i,s,t) for(int i=(s); i<(t); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define FORL(i,s,t) for(L i=(s); i<(t); i++)
#define BUG puts("here!!!")
#define STOP system("pause")
#define file_r(x) freopen(x, "r", stdin)
#define file_w(x) freopen(x, "w", stdout)
#define EPS 1e-6
#define EQ(a, b) (fabs((a) - (b)) <= EPS)
#define POS(a) ((a) >= EPS)
#define NEG(a) ((a) <= -EPS)
#define BG(a, b) ((a) - (b) >= EPS)
#define LS(a, b) ((b) - (a) >= EPS)
#define CLR(a, x) memset( a, x, sizeof( a ) )
#define PI (atan(1.0) * 4)
#define SQ(x) ((x) * (x))
#define DIST(x1, y1, x2, y2) (sqrt(SQ((x1) - (x2)) + SQ((y1) - (y2))))
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define LOG2(x) (log(x) / log(2))
#define XX first.first
#define XY first.second
#define YX second.first
#define YY second.second

using namespace std;
typedef unsigned long long ULL;
typedef long long LL;
typedef pair<double, double> Pd;
typedef pair<int, int> Pi;
typedef pair<LL, LL> Pl;

vector<int> ch[20];
int ty[20];
int n;
vector<int> ans;
set<int> fail;
map<int, int> keys;

bool solve(int state) {
  if (state == (1 << n) - 1)
    return true;
  if (fail.find(state) != fail.end())
    return false;
  int p = 1;
  REP(i, n) {
    if (!(state & p)) {
      if (keys.find(ty[i]) != keys.end() && keys[ty[i]] > 0) {
        keys[ty[i]]--;
        REP(j, ch[i].size())
          if (keys.find(ch[i][j]) == keys.end())
            keys[ch[i][j]] = 1;
          else
            keys[ch[i][j]]++;
        ans.push_back(i + 1);
        if (solve(state | p)) {
          return true;
        }
        ans.pop_back();
        keys[ty[i]]++;
        REP(j, ch[i].size())
          keys[ch[i][j]]--;
      }
    }
    p = p << 1;
  }
  fail.insert(state);
  return false;
}

int main()
{
  int t;
  cin >> t;
  FOR(tt, 1, t + 1) {
    int k, x;
    cin >> k >> n;
    keys.clear();
    REP(i, k) {
      cin >> x;
      if (keys.find(x) == keys.end())
        keys[x] = 1;
      else
        keys[x]++;
    }
    REP(i, n) {
      ch[i].clear();
      cin >> ty[i] >> k;
      REP(j, k) {
        cin >> x;
        ch[i].push_back(x);
      }
    }
    fail.clear();
    ans.clear();
    cout << "Case #" << tt << ": ";
    if (!solve(0)) {
      cout << "IMPOSSIBLE";
    } else {
      REP(i, ans.size())
        cout << ans[i] << " ";
    }
    cout << endl;
  }
  return 0;
}

