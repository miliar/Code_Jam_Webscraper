#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <assert.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
const int INF = 1000000000;
const int prime = 9241;
const ld pi = acos(-1.);

int come[20];
int guy[20];
const int IN = 2, OUT = 3;

bool dp[16][(1<<15)+5];

void solve(int test)
{
    int n;
    cin >> n;
    map<int, int> v;
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
       char a; int b;
       cin >> a >> b;
       b--;
       if (a == 'E') come[i] = IN;
       else come[i] = OUT;        
       if (b != -1 && v.count(b) == 0) v[b] = cnt++;
       if (b != -1) guy[i] = v[b];
       else guy[i] = -1;
    }
  //  for (int i = 0; i < n; i++)
  //     cout << guy[i] << "," << (come[i]==IN?"IN":"OUT") << ' ';
  //  cout << endl;
    for (int i = 0; i <= n; i++)
       for (int j = 0; j < (1<<n); j++)
          dp[i][j] = 0;
    for (int i = 0; i < (1<<n); i++)
       dp[0][i] = 1;
    for (int i = 0; i < n; i++)
       for (int mask = 0; mask < (1<<n); mask++)
          if (dp[i][mask])
          {
             if (guy[i] == -1)
             {
                 if (come[i] == IN)
                 {
                    for (int j = 0; j < n; j++)
                       if (!(mask & (1<<j))) dp[i+1][mask | (1<<j)] = 1;
                 }
                 else if (come[i] == OUT)
                 {
                    for (int j = 0; j < n; j++)
                       if (mask & (1<<j)) dp[i+1][mask ^ (1<<j)] = 1;
                 }
             }
             else
             {
                if (come[i] == IN)
                {
                    if (!(mask & (1<<guy[i]))) dp[i+1][mask | (1<<guy[i])] = 1;
                } 
                else if (come[i] == OUT)
                {
                    if (mask & (1<<guy[i])) dp[i+1][mask ^ (1<<guy[i])] = 1;
                }
             }
          } 
    int ans = (int)1e9;
    for (int i = 0; i < (1<<n); i++)
       if (dp[n][i]) ans = min(ans, __builtin_popcount(i));
    cout << "Case #" << test << ": ";
    if (ans > 100) cout << "CRIME TIME";
    else cout << ans;
    cout << endl;
}

int main()
{
   int t;
   cin >> t;
   for (int i = 1; i <= t; i++)
   {
      solve(i);
   }
}