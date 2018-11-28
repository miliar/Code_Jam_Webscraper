#include <cstring>
typedef long long ll;

#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int A[32];
int B[32];
int K[32];

void parse(ll n, int *dst){
  REP(i,32) dst[i] = (n & (1ll << i)) != 0;
}

ll memo[2][2][2][32];

ll solve(int a, int b, int c, int pos){
  if(pos == -1) return a == 1 && b == 1 && c == 1;
  if(memo[a][b][c][pos] != -1) return memo[a][b][c][pos];

  ll ret = 0;

  REP(aa,2) REP(bb,2){
    const int kk = aa & bb;

    if(!a && aa > A[pos]) continue;
    if(!b && bb > B[pos]) continue;
    if(!c && kk > K[pos]) continue;

    const int na = a || (aa < A[pos]);
    const int nb = b || (bb < B[pos]);
    const int nc = c || (kk < K[pos]);

    ret += solve(na, nb, nc, pos - 1);
  }

  // printf("%d %d %d %d: %lld\n", a, b, c, pos, ret);

  return memo[a][b][c][pos] = ret;
}

void solve(int cs){
  parse(getInt(), A);
  parse(getInt(), B);
  parse(getInt(), K);

  memset(memo, -1, sizeof(memo));
  const ll ans = solve(0, 0, 0, 31);
  printf("Case #%d: %lld\n", cs, ans);
}

int main(){
  const int n = getInt();
  REP(i,n) solve(i + 1);
  return 0;
}
