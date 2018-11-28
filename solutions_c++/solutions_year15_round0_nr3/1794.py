#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <cctype>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < n; ++i)
#define rrep(i,n) for(int i = 1; i <= n; ++i)
#define drep(i,n) for(int i = n-1; i >= 0; --i)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcount
#define snuke srand((unsigned)clock()+(unsigned)time(NULL));
using namespace std;
typedef long long int ll;
typedef pair<int,int> P;
typedef vector<int> vi;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi& a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}

const int MX = 100005, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-10;
const int di[] = {-1,0,1,0}, dj[] = {0,-1,0,1}; //^<v>

const int g[4][4] {
{0,1,2,3},
{1,4,3,6},
{2,7,4,1},
{3,2,5,4}};

inline int nxt(int i, char c) {
  c = c-'i'+1;
  return g[i%4][c]^(i&4);
}

int dp[MX][3][8];

int main(){
  int ts;
  cin >> ts;
  rrep(ti,ts) {
    int l, x; string s, is;
    cin >> l >> x >> is;
    int n = l*x;
    string ans = "NO";
    s = ""; rep(i,x) s += is;
    rep(i,n+1)rep(j,3)rep(k,8) dp[i][j][k] = 0;
    dp[0][0][0] = 1;
    rep(i,n) {
      rep(j,3)rep(k,8) {
        if (!dp[i][j][k]) continue;
        dp[i+1][j][nxt(k,s[i])] = 1;
      }
      rrep(j,2) dp[i+1][j][0] |= dp[i+1][j-1][j];
     // if(n<13){rep(j,3)rep(k,8) printf("%d",dp[i+1][j][k]); puts("");}
    }
    if (dp[n][2][3]) ans = "YES";
    printf("Case #%d: %s\n",ti,ans.c_str());
  }
  return 0;
}





