#include <bits/stdc++.h>

#define F first
#define S second
#define llong long long
#define ullong unsigned long long
#define mp make_pair
#define pb push_back
#define pii pair <int, int>
#define sz(v) (int)v.size()

using namespace std;

const int MXN = (int)1e6 + 10;
const int INF = (int)1e9 + 7;
const llong LINF = (llong)1e18 + 10;
const double EPS = (double)1e-9;
const double PI = (double)acos(-1.0);

inline bool bit(int id, int mask){
  return ((mask >> id) & 1);
}

int n;
llong a[MXN];
llong ans[MXN];
vector <int> v;

inline string toString(llong mask){
  string ret = "";
  for(int i = n - 1; i >= 0; --i){
    ret += char('0' + bit(i, mask));
  }
  return ret;
}

inline llong tobase(llong mask, int base){
  llong ret = 0;
  llong cur = 1;
  for(int i = 0; i < n; ++i){
    ret += cur * bit(i, mask);
    cur *= base;
  }
  return ret;
}

inline bool isprime(int x){
  for(int i = 2; i * i <= x; ++i){
    if(x % i == 0)
      return false;
  }
  return true;
}

inline llong SD(llong x){
  for(int i = 0; i < sz(v); ++i){
    if(x == 1LL * v[i])
      return -1LL;
    if(x % v[i] == 0)
      return 1LL * v[i];
  }
  return -1LL;
}

int main(){
  #ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif // LOCAL
  for(int i = 2; i <= 1000; ++i){
    if(isprime(i)){
      v.pb(i);
    }
  }
  n = 16;
  int cnt = 50;
  cout << "Case #1:\n";
  for(llong mask = 0; mask < (1LL << n); ++mask){
    if(!bit(0, mask) || !bit(n - 1, mask))
      continue;
    bool boo = true;
    for(int i = 2; i <= 10; ++i){
      a[i] = tobase(mask, i);
      ans[i] = SD(a[i]);//Smallest divisor
      boo &= (ans[i] > 0);
    }
    if(boo){
      cout << toString(mask) << " ";
      //for(int i = 2; i <= 10; ++i){
      //  cout << a[i] << " ";
      //}
      //cout << "\n";
      for(int i = 2; i <= 10; ++i){
        cout << ans[i] << " ";
      }
      cout << "\n";
      --cnt;
    }
    if(!cnt){
      break;
    }
  }
  assert(cnt == 0);
  return 0;
}
