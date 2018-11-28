#include <bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define TR(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define TR(...)
#endif

typedef long long                LL;
typedef vector < int >           VI;
typedef pair < int,int >         II;
typedef vector < II >            VII;

#define MOD                      1000000007
#define EPS                      1e-12
#define N                        200100
#define PB                       push_back
#define MP                       make_pair
#define F                        first 
#define S                        second
#define ALL(v)                   v.begin(),v.end()
#define SZ(a)                    (int)a.size()
#define FILL(a,b)                memset(a,b,sizeof(a))
#define SI(n)                    scanf("%d",&n)
#define SLL(n)                   scanf("%lld",&n)
#define PLLN(n)                  printf("%lld\n",n)
#define PIN(n)                   printf("%d\n",n)
#define REP(i,j,n)               for(LL i=j;i<n;i++)
#define PER(i,j,n)               for(LL i=n-1;i>=j;i--)
#define endl                     '\n'
#define fast_io                  ios_base::sync_with_stdio(false);cin.tie(NULL)

#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
 
inline int mult(int a , int b) { LL x = a; x *= LL(b); if(x >= MOD) x %= MOD; return x; }
inline int add(int a , int b) { return a + b >= MOD ? a + b - MOD : a + b; }
inline int sub(int a , int b) { return a - b < 0 ? MOD - b + a : a - b; }
LL powmod(LL a,LL b) { if(b==0)return 1; LL x=powmod(a,b/2); LL y=(x*x)%MOD; if(b%2) return (a*y)%MOD; return y%MOD; }

char p[2] = {'+', '-'};
string s;

void flip (int i, int len) {
  int lim = i+len;
  for(int i = 0; i < lim; i ++) {
    if(s[i] == p[0])
      s[i] = p[1];
    else
      s[i] = p[0];
  }
}


int main() {
  FILEIO("AA")
  int t; cin >> t;
  REP(z,1,t+1) {
     cin >> s;
    int len; cin >> len;
    int n = SZ(s);
    int ans = 0;
    bool ok = true;
    for(int i = 0; i < n; i ++) {
      if(s[i] == '+')
        continue;
      if(s[i] == '-') {
        ans ++;
        if(i + len > n) {
          ok = false;
          break;
        }
        else
          flip(i,len);
      }
    }
    cout << "Case #" << z << ": ";
    if(ok)
      cout << ans << endl;
    else
      cout << "IMPOSSIBLE\n";
  }
  return 0;
}
