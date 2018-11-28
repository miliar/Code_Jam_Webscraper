/*
 *
 *
 */

#include <bits/stdc++.h>

using namespace std;

#define LOG(...) fprintf(stderr, __VA_ARGS__)
//#define LOG(...)
#define FOR(i, a, b) for(ll i = (int)(a); i < (int)(b); ++i)
#define REP(i, n) for(int i = 0; i < (int)(n); ++i)
#define ALL(a) (a).begin(), (a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define EXIST(s, e) ((s).find(e) != (s).end())
#define SORT(c) sort(ALL(c))
#define RSORT(c) sort(RALL(c))
#define SQ(n) (n) * (n)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<pll> vpl;
typedef vector<ll> vll;
typedef vector<vb> vvb;
typedef vector<vi> vvi;
typedef vector<vll> vvll;

class Radix {
private:
  const char* s;
  int a[128];
public:
  Radix(const char* s = "0123456789ABCDEF") : s(s) {
    int i;
    for(i = 0; s[i]; ++i)
      a[(int)s[i]] = i;
  }
  std::string to(long long p, int q) {
    int i;
    if(!p)
      return "0";
    char t[64] = { };
    for(i = 62; p; --i) {
      t[i] = s[p % q];
      p /= q;
    }
    return std::string(t + i + 1);
  }
  std::string to(const std::string& t, int p, int q) {
    return to(to(t, p), q);
  }
  long long to(const std::string& t, int p) {
    int i;
    long long sm = a[(int)t[0]];
    for(i = 1; i < (int)t.length(); ++i)
      sm = sm * p + a[(int)t[i]];
    return sm;
  }
};


int main() {
  map<ll, ll> factor; //factor[n]==0のとき素数
  Radix r;
  int T;
  cin >> T;
  REP(i, T) {
    int cnt = 0;
    int N, J;
    cin >> N >> J;
    ll start = (1 << (N - 1) ) + 1;
    ll goal = (1 << N) - 1;

    printf("Case #%d:\n", i + 1);
    for(ll n = start; n <= goal; n += 2) {
      bool flag = true;
      string num = r.to(n, 2);
      vll numbers(9, -2);
      FOR(base, 2, 10 + 1){
        ll rn = r.to(num, base);
        if (!EXIST(factor, rn)) {
          factor[rn] = 0;
          if (~rn & 1) factor[rn] = 2;
          else{
            ll rtrn = sqrt(rn);
            for(int j = 3; j < rtrn; j += 2) {
              if (rn % j == 0) {
                factor[rn] = j;
                break;
              }
            }
          }

        }
        if(factor[rn] == 0) {
          flag = false;
          break;
        }
        else{
          numbers[base - 2] = factor[rn];
        }
      }
      if(flag) {
        cout << num;
        cnt++;
        REP(i, 9){
          cout << ' ' << numbers[i];
        }
        cout << endl;
        if(cnt >= J) break;
      }
    }
  }
}
