/**
 * @author neko13
 */
#include<iostream>
#include<string>
#include<cmath>
using namespace std;
// 13C
#define DBG 0
#define sz(c) ((int)(c).size())
#define   forl(i, a, b) for(int i = (a); i <  (b); ++i)
#define  forle(i, a, b) for(int i = (a); i <= (b); ++i)
#define   forg(i, a, b) for(int i = (a); i >  (b); --i)
#define  forge(i, a, b) for(int i = (a); i >= (b); --i)
#define  forlc(i, a, b) for(int i##_b = (b), i = (a); i <  i##_b; ++i)
#define forlec(i, a, b) for(int i##_b = (b), i = (a); i <= i##_b; ++i)
#define  forgc(i, a, b) for(int i##_b = (b), i = (a); i >  i##_b; --i)
#define forgec(i, a, b) for(int i##_b = (b), i = (a); i >= i##_b; --i)
#define  forls(i, n, a, b) for(int i = a; i != b; i = n[i])
#define rep(n)  for(int               repp = 0; repp <    (n); ++repp)
#define repc(n) for(int repp_b = (n), repp = 0; repp < repp_b; ++repp)
#define rst(a, v) memset(a, v, sizeof a)
#define cpy(a, b) memcpy(a, b, sizeof a)
#define rstn(a, v, n) memset(a, v, (n)*sizeof((a)[0]))
#define cpyn(a, b, n) memcpy(a, b, (n)*sizeof((a)[0]))
#define ast(b) if(DBG && !(b)) { printf("!! %d\n", __LINE__); while(1) getchar(); }
#define dout DBG && cout << ">>| "
#define pr(x) #x"=" << (x) << " | "
#define mk(x) DBG && cout << "**| "#x << endl
#define pra(arr, a, b) if(DBG) { \
    dout<<#arr"[] | "; \
    forlec(i, a, b) cout<<"["<<i<<"]="<<arr[i]<<" |"<<((i-(a)+1)%13?" ":"\n"); \
    if(((b)-(a)+1)%13) puts(""); \
  }
#define rd(type, x) type x; cin >> x
inline int     rdi() { int d; scanf("%d", &d); return d; }
inline char    rdc() { scanf(" "); return getchar(); }
inline string  rds() { rd(string, s); return s; }
inline double rddb() { double d; scanf("%lf", &d); return d; }
template<class T> inline bool updateMin(T& a, T b) { return a>b? a=b, true: false; }
template<class T> inline bool updateMax(T& a, T b) { return a<b? a=b, true: false; }

bool ispalindrom(int x) {
  static int num[128];
  int n = 0;
  while(x) num[n++] = x%10, x /= 10;
  forlc(i, 0, n>>1)
    if(num[i] != num[n-1-i])
      return false;
  return true;
}

int sqr(int x) { return x*x; }
bool is_sqr(int x) {
  int s = sqrt(x);
  return sqr(s-1)==x || sqr(s)==x || sqr(s+1)==x;
}

int main() {
  int cas = 0;
  repc(rdi()) {
    rd(int, a);
    rd(int, b);
    int ans = 0;
    forle(i, a, b)
      if(ispalindrom(i) && is_sqr(i) && ispalindrom(sqrt(i)+1e-6))
        ++ans;
    printf("Case #%d: %d\n",  ++cas, ans);
  }
  return 0;
}