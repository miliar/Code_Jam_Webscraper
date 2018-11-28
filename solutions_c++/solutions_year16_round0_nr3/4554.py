#define ONLINE_JUDGE
#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
using namespace std;
#else
#include "header.h"
#include "debug.h"
#endif
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
const int N = 200000;

string getBin (LL num, LL len) {
  string s = "";
  while (num) {
    if(num % 2 == 0) {
      s = s + '0';
    } else {
      s = s + '1';
    }
    num /= 2;
  }
  if(sz(s) < len) {
    s[0] = '0';
  }
  return s;
}

LL POW (LL base, LL pow) {
  LL ret = 1;
  while (pow--) {
    ret *= base;
  }
  return ret;
}

LL getDivisor (LL num) {
  for (LL i = 2; i*i <= num; ++i) {
    if (num % i == 0LL) {
      //show3(num,i,num%i);
      return i;
    }
  }
  return 1;
}

bool check (string s) {
  vector <LL> ans;
  for (LL base = 2; base <= 10; ++base) {
    LL num = 1;
    for (LL pos = 1; pos < sz(s); ++pos) {
      if (s[pos] == '1') {
        num += POW (base, pos);
      }
    }
    //show3(s,base,num);
    LL divisor = getDivisor (num);
    if (divisor == 1) {
      return false;
    }
    //show3 (s, num, divisor);
    ans.pb (divisor);
  }
  for (int i = sz(s) - 1; i >= 0; --i) {
    cout << s[i];
  }
  cout << ' ';
  for (LL i = 0; i < sz(ans); ++i) {
    cout << ans [i] << ' ';
  }
  cout << '\n';
  return true;
}

void solve (LL n, LL j) {
  if (j == 0) return;
  for (LL i = 1; i < (1 << n); ++i) {
    string s = getBin (i, n);
    if (s[0] == '0' || s[n - 1] == '0') {
      continue;
    }
    if (check (s)) {
      --j;
      if (j == 0) {
        return;
      }
    }
  }
}

int main () {
  #ifndef ONLINE_JUDGE
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
  #endif
  cin.sync_with_stdio (0); cin.tie (0);
  LL tt;
  cin >> tt;
  for (LL tc = 1; tc <= tt; ++tc) {
    cout << "Case #" << tc << ":\n";
    LL n, j;
    cin >> n >> j;
    solve (n, j);
  }
}
