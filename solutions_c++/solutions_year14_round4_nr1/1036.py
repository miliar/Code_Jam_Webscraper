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

int a[15000];
char was[15000];

int main() {
  //freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int q=0;q<t;q++) {
    cout << "Case #" << q+1 << ": ";
    int ans = 0;
    int n,m;
    cin >> n >> m;
    for (int i=0;i<n;i++) cin >> a[i];
    sort(a, a+n);
    m0(was);
    for (int cur = n-1; cur>=0;cur--) {
      if (was[cur]) continue;
      int pos = cur-1;
      while (pos>=0 && (was[pos] || a[pos] > m-a[cur])) pos--;
      if (pos>=0) {
        was[pos] = 1;
      }
      ans++;
    }
    cout << ans << "\n";
  }
  return 0;
}
