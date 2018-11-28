#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <ctime>

#define pb push_back
#define mp make_pair
#define PI 3.1415926535897932384626433832795
#define ALL(x) x.begin(), x.end()
#define F first
#define S second
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,-1,sizeof(x))
#define pw(x) (1ull<<(x))

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

int t,n,m;
int a[15][15], b[15][15];

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for (int o=0;o<t;o++) {
    cin >> n >> m;
    for (int i=0;i<n;i++) for (int j=0;j<m;j++) cin >> a[i][j];
    bool ans = false;
    for (int mask=0;mask<pw(m+n) && !ans;mask++) {
      bool ok = true;
      for (int i=0;i<n;i++) for (int j=0;j<m;j++) b[i][j] = 2;
      for (int i=0;i<n && ok;i++) {
        if ((((mask)>>(i))&1)==0) continue;
        for (int j=0;j<m;j++) {
          if (a[i][j]==2) ok = false;
          b[i][j] = 1;
        }
      }
      for (int i=0;i<m && ok;i++) {
        if ((((mask)>>(i+n))&1)==0) continue;
        for (int j=0;j<n;j++) {
          if (a[j][i]==2) ok = false;
          b[j][i] = 1;
        }
      }
      for (int i=0;i<n && ok;i++) for (int j=0;j<m && ok;j++) if (b[i][j]!=a[i][j]) ok = false;
      if (ok) ans = true;
    }
    cout << "Case #" << o+1 << ": ";
    if (ans) cout << "YES\n"; else cout << "NO\n";
  } 
  return 0;
}
