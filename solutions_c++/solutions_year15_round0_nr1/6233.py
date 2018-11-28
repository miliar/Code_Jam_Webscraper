#include <iostream>
#include <algorithm>
#include <memory.h>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
using namespace std;
#define sz(s) int((s).size())
#define clr(a) memset(a,0,sizeof(a))
#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int(i)=0; (i)<(n);++(i))
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
typedef pair <int,int> pii;
typedef long long LL;
template <class T> inline T gcd(T a,T b){return (!b? a : gcd(b,a%b));}
template <class T> inline T ABS(T x){return ((x)>0?(x):(-(x)));}
const int N = 1010;

int arr [N];

int main () {
  freopen ("in.txt", "r", stdin);
  freopen ("out.txt", "w", stdout);
  cin.sync_with_stdio (0); cin.tie (0);
  int tt;
  cin >> tt;
  for (int tc = 1; tc <= tt; ++tc) {
    cout << "Case #" << tc << ": ";
    int n;
    string s;
    cin >> n >> s;
    int prev = 0;
    int ans = 0;
    for (int i = 0; s [i]; ++i) {
      if (i > prev && s [i] > '0') {
        ans += i - prev;
        prev += i - prev;
      }
      prev += (s [i] - 48);
    }
    cout << ans << '\n';
  }
}
