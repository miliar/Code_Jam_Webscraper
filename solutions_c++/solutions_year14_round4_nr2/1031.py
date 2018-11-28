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

int a[1500];
int b[1500];

int run(int sz) {
  int ret = 0;
  if (sz==0) return ret;
  for (int i=0;i<sz;i++) {
    for (int j=sz-2;j>=0;j--) {
      if (b[j]>b[j+1]) {
        swap(b[j], b[j+1]);
        ret++;
      }
    }
  }
  return ret;
}

int main() {
  //freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int q=0;q<t;q++) {
    int n;
    cin >> n;
    cout << "Case #" << q+1 << ": ";
    for (int i=0;i<n;i++) cin >> a[i];
    int l = 0, r = n-1;
    int ans = 0;
    for (int i=0;i<n;i++) {
      int mi = INF, mip = 0;
      for (int j=l;j<=r;j++) 
        if (a[j]<mi) {
          mi = a[j];
          mip = j;
        }
      if (mip-l < r-mip) {
        for (int i=mip-1;i>=l;i--) {
          a[i+1] = a[i];
        }
        ans += mip-l;
        l = l+1;
      }
      else {
        for (int i=mip;i<=r-1;i++) {
          a[i] = a[i+1];
        }
        ans += r-mip;
        r = r-1;
      }
    }
    cout << ans << "\n";
  }
  return 0;
}
