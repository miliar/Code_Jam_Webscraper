
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <climits>
#include <limits.h>
#include <string>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <assert.h>
#include <cstring>
using namespace std;
#define rep(i, n) for (int (i) = 0, j123 = n; (i) < j123; (i) ++)
#define rep1(i, n) for (int (i) = 1, j123 = n; (i) <= j123; (i) ++)
#define db(x) {cout << #x << " = " << (x) << endl;}
#define dba(a, x, y) {cout << #a << " :";for(int i123=(x);i123<=(y);i123++) cout<<setw(4)<<(a)[i123];cout<<endl;}
#define clr(x) memset(x,0,sizeof(x));
#define mp make_pair
#define pb push_back
#define sz(x) int(x.size())
#define endl '\n'
typedef long long ll;
typedef long double ld;
const int INF = INT_MAX;
const ll INFL = LLONG_MAX;
const ld pi = acos(-1);
// const int MOD = ;

int T;
int R, C;
char A[111][111];
char dir[4] = {'^','>','<','v'};
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, 1, -1, 0};
int rowcnt[111];
int colcnt[111];
int init()
{
  clr(A);
  clr(rowcnt);
  clr(colcnt);
}
int main()
{
  ios_base::sync_with_stdio(0); cout.precision(15); cout << fixed; cout.tie(0); cin.tie(0);
  cin >> T;
  for (int testcase = 1; testcase <= T; testcase++)
  {
    init();
    cin >> R >> C;
    rep1(r,R) rep1(c,C)
    {
      cin >> A[r][c];
      if (A[r][c] != '.')
      {
        rowcnt[r]++;
        colcnt[c]++;
      }
    }
    int cnt = 0;
    rep1(r,R) rep1(c,C)
    {
      if (A[r][c] == '.') continue;
      // if it's an arrow, 
      // it needs to be pointing to other arrow
      if (rowcnt[r] == 1 && colcnt[c] == 1)
      {
        cnt = -1e9;
      }
      rep(i,4)
      {
        if (A[r][c] == dir[i])
        {
          int rr = r + dx[i];
          int cc = c + dy[i];
          int any = 0;
          while (true)
          {
            if (1 <= rr && rr <= R && 1 <= cc && cc <= C)
            {
              if (A[rr][cc] != '.')
              {
                any = 1;
                break;
              }
              rr += dx[i];
              cc += dy[i];
            }
            else
            {
              break;
            }
          }
          if (!any) cnt++;
          break;
        }
      }
    }
    cout << "Case #" << testcase << ": "; 
    
    if (cnt >= 0)
    {
      cout << cnt << endl;
    }
    else
    {
      cout << "IMPOSSIBLE" << endl;
    }
  }
}
