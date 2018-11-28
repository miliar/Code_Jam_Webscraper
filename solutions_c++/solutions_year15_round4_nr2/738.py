
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
int N;
ld V, X;
ld R[111];
ld C[111];
int init()
{
  clr(R);
  clr(C);
}
inline int eq(ld a, ld b)
{
  return abs(a-b) < 1e-15;
}
int main()
{
  ios_base::sync_with_stdio(0); cout.precision(15); cout << fixed; cout.tie(0); cin.tie(0);
  cin >> T;
  rep1(testcase,T)
  {
    init();
    cin >> N >> V >> X;
    // rate and temperature of water source
    rep1(i,N) cin >> R[i] >> C[i];
    ld ans = -10;
    if (N == 1)
    {
      if (eq(C[1],X))
      {
        ans = V / R[1];
      }
    }
    else
    {
      // N == 2
      if (C[1] > C[2])
      {
        swap(C[1], C[2]);
        swap(R[1], R[2]);
      }
      // now C[1] <= C[2]
      if (eq(C[1],C[2]))
      {
        if (eq(X,C[1]))
        {
          ans = V / (R[1] + R[2]);
        }
        else
        {
          // impossible
        }
      }
      else
      {
        // C[1] < C[2]
        if ((eq(X,C[1]) == 0) && X < C[1])
        {
          // impossible
          // X < C[1] < C[2]
        }
        else if (eq(X,C[1]))
        {
          ans = V / R[1];
          // X = C[1] < C[2]
        }
        else if ((eq(X,C[2]) == 0) && X < C[2]) 
        {
          // C[1] < X < C[2]
          // binary search
          ld lo = 0;
          ld hi = V;
          while (lo + 1e-15 < hi)
          {
            ld v1 = (lo + hi) / 2;
            ld v2 = V - v1;
            ld currenttemp = (v1*C[1]+v2*C[2])/(v1+v2);
            if (currenttemp > X)
            {
              // we need to put more cold water
              // which is 1st source
              lo = v1;
            }
            else
            {
              hi = v1;
            }
          }
          ld v1 = (lo + hi) / 2;
          ld v2 = V - v1;
          ans = max(v1/R[1],v2/R[2]);
        }
        else if (eq(X,C[2]))
        {
          ans = V / R[2];
        }
        else
        {
          // impossible
        }
      }
    }
    cout << "Case #" << testcase << ": ";
    if (ans < -1)
    {
      cout << "IMPOSSIBLE" << endl;
    }
    else
    {
      cout << ans << endl;
    }
  }
}
