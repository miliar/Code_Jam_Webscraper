#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
using namespace std;
using ll = long long;

class range {private: struct I{int x;int operator*(){return x;}bool operator!=(I& lhs){return x<lhs.x;}void operator++(){++x;}};I i,n;
public:range(int n):i({0}),n({n}){}range(int i,int n):i({i}),n({n}){}I& begin(){return i;}I& end(){return n;}};

void solve();

int main() {
  int T; cin >> T;
  for (int test : range(1, T+1)) {
    cout << "Case #" << test << ": ";
    solve();
  }
}

////////////////////////////////////////////////////////////////////////////////

const int MOD = 1000*1000*1000+9;
int add(int a, int b) { return ((ll)a+b)%MOD; }
int mul(int a, int b) { return ((ll)a*b)%MOD; }
void chadd(int& a, int b) { a = ((ll)a+b)%MOD; }

ll gcd(ll a,ll b) { return b?gcd(b,a%b):a; }
ll lcm(ll a,ll b) { return a/gcd(a,b)*b; }

ll inv(ll a, ll p) {
  return ( a == 1 ? 1 : (1 - p*inv(p%a, a)) / a + p );
}

int H, W;
int f[8][8];

int get(int y, int x) {
  x = (x + W) % W;
  if (y < 0 || x < 0 || y >= H || x >= W) return -2;
  return f[y][x];
}

bool check(int y, int x) {
  x = (x + W) % W;
  int now = get(y, x);
  if (now < 0) return true;
  int undecided = 0;
  int count = 0;

  undecided += get(y - 1, x) == -1;
  undecided += get(y + 1, x) == -1;
  undecided += get(y, x - 1) == -1;
  undecided += get(y, x + 1) == -1;

  count += get(y - 1, x) == now;
  count += get(y + 1, x) == now;
  count += get(y, x - 1) == now;
  count += get(y, x + 1) == now;

  return count <= now && now <= count + undecided;
}

int ret;
void brute(int y, int x) {
  if (y == H) {
    /*
    for (int i : range(H)) {
      for (int j : range(W)) cout << f[i][j];
      cout << endl;
    }
    cout << endl;
    */
    ret++;
    return;
  }

  if (x == W) {
    brute(y + 1, 0);
    return;
  }

  for (int c : range(1, 3 + 1)) {
    f[y][x] = c;

    if (!check(y - 1, x)) goto SKIP;
    if (!check(y, x - 1)) goto SKIP;
    if (!check(y, x)) goto SKIP;

    brute(y, x + 1);
SKIP:
    f[y][x] = -1;
  }
}

void solve() {
  cin >> H >> W;

  /*
  memset(f, -1, sizeof(f));
  ret = 0;
  brute(0, 0);
  cout << ret << endl;
  */

  vector<int> Y{1}, Z{1};
  if (W % 3 == 0) { Y.push_back(2); Z.push_back(3); }
  if (W % 6 == 0) { Y.push_back(2); Z.push_back(6); }
  if (W % 4 == 0) { Y.push_back(3); Z.push_back(4); }

  int dp[H + 10][20][2];
  memset(dp, 0, sizeof(dp));
  dp[0][1][0] = 1;
  dp[0][1][1] = 1;

  for (int y : range(H))
  for (int period : range(1, 12 + 1))
  for (int prev : range(2)) {
    if (prev == 0) {
      // put 33333
      chadd(dp[y + 2][period][1 - prev], dp[y][period][prev]);
    } else {
      // put 22222
      for (int i : range(Y.size())) {
        int np = lcm(period, Z[i]);
        chadd(dp[y + Y[i]][np][1 - prev], mul(dp[y][period][prev], Z[i]));
      }
    }
  }

  int res = 0;
  for (int period : range(1, 12 + 1)) {
    int t = add(dp[H][period][0], dp[H][period][1]);
    //cout << period << "=> " << t << endl;
    chadd(res, mul(t, inv(period, MOD)));
  }
  cout << res << endl;
}
