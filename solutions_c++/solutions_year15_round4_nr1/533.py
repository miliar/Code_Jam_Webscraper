#include <iostream>
#include <algorithm>
#include <cstdio>
#include <memory.h>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <vector>
using namespace std;
const double PI = 3.14159265358979323846;
const int inf = 1 << 29;
const int maxn = 102;
const int maxm = 102;
const int mod = 1000000007;

void inc (char& c){
  c = getchar ();
  while (c == ' '||c == '\n')     c = getchar ();
}

void in(int &x) {
  char ch=getchar();
  bool flag=false;
  while ((ch<'0'||ch>'9')&&ch!='-') ch=getchar();
  if (ch=='-') {
    flag=true;
    ch=getchar();
  }
  x=0;
  while (ch>='0'&&ch<='9') {
    x=x*10+ch-'0';
    ch=getchar();
  }
  if (flag) x=-x;
}

/*
struct Node {
  int v;//,w;
  int next;
}edge[maxn << 1];
int head[maxn << 1];
int m,n,idx;

void init() {
  memset(head,-1,sizeof(head));
  idx = 0;
  return;
}

void addedge(int u, int v) {//(int u, int v, int w) {
  edge[idx].v = v;
  //edge[idx].w = w;
  edge[idx].next = head[u];
  head[u] = idx++;

  edge[idx].v = u;
  //edge[idx].w = w;
  edge[idx].next = head[v];
  head[v] = idx++;
  return;
}
/*
int find(int x) {
  return fa[x] == x ? x : (fa[x] = find(fa[x]));
}

bool flag[maxn];
int phi[maxn];
vector<int> prime;

void get_prime_phi() {
  memset(flag, false, false);
  prime.clear();

  phi[1] = 1;
  for (int i=2;i<maxn;i++) {
    if (!flag[i]) {
      printf("%d ",i);
      prime.push_back(i);
      phi[i] = i-1;
    }
    for (int j=0;j<prime.size() && i*prime[j]<maxn; j++) {
      flag[i * prime[j]] = true;
      if (i % prime[j]) {
        phi[i * prime[j]] = phi[i] * (prime[j] - 1);
      } else {
        phi[i * prime[j]] = phi[i] * prime[j];
        break;
      }
    }
  }
  return;
}

long long extend_gcd(long long a,long long b,long long &x,long long &y) {
  if(a == 0 && b == 0) return -1;
  if(b == 0){x = 1; y = 0; return a;}
  long long d = extend_gcd(b, a % b, y, x);
  y -= a / b * x;
  return d;
}

long long mod_reverse(long long a, long long n) {
  long long x,y;
  long long d = extend_gcd(a, n, x, y);
  if(d == 1) return (x % n + n) % n;
  else return -1;
}

int c[maxn << 1];
int lowbit(int x) {
  return x & (-x);
}

void update(int x, int num) {
  while(x < maxn) {
    c[x] += num;
    x += lowbit(x);
  }
  return;
}

int getSum(int x) {
  int cnt = 0;
  while(x > 0) {
    cnt += c[x];
    x -= lowbit(x);
  }
  return cnt;
}

long long multi(long long m, long long n, long long k) {
  long long res = 0;
  while(n) {
    if (n & 1) {
      res += m;
      res %= k;
    }
    m = (m + m) % k;
    n >>= 1;
  }
  return res;
}

// m^n % k
long long quickpow(long long m, long long n, long long k) {
  long long res = 1LL;
  while (n) {
    if (n & 1) {
      res = multi(res, m, k);
    }
    m = multi(m, m, k);
    n >>= 1;
  }
  return res;
}
*/

int m,n;

char grid[maxn][maxn];

int record[maxn][maxn][5];

void read() {
  in(n), in(m);
  for (int i=1;i<=n;i++) {
    for (int j=1;j<=m;j++) {
       inc(grid[i][j]);
    }
  }
  return;
}

void solve() {
  int res = 0;

  memset(record, 0, sizeof(record));
  for (int i=1;i<=n;i++) {
    for (int j=1;j<=m;j++) {
      if (grid[i][j] != '.') {
        record[i][j][0] = 1;
        break;
      }
    }
  }
  for (int i=1;i<=n;i++) {
    for (int j=m;j>=1;j--) {
      if (grid[i][j] != '.') {
        record[i][j][1] = 1;
        break;
      }
    }
  }
  for (int j=1;j<=m;j++) {
    for (int i=1;i<=n;i++) {
      if (grid[i][j] != '.') {
        record[i][j][2] = 1;
        break;
      }
    }
  }
  for (int j=1;j<=m;j++) {
    for (int i=n;i>=1;i--) {
      if (grid[i][j] != '.') {
        record[i][j][3] = 1;
        break;
      }
    }
  }

  bool flag = true;
  for (int i=1;i<=n;i++) {
    for (int j=1;j<=m;j++) {/*
      bool fuck = false;
      for (int k=0;k<4;k++) {
        if (!record[i][j][k]) {
          fuck = true;
          break;
        }
      }
      if (!fuck) {
        flag = false;
        break;
      }*/
      if (record[i][j][0] && record[i][j][1] && record[i][j][2] && record[i][j][3]) {
        flag = false;
        break;
      }
      if (record[i][j][0] && grid[i][j] == '<') res++;
      if (record[i][j][1] && grid[i][j] == '>') res++;
      if (record[i][j][2] && grid[i][j] == '^') res++;
      if (record[i][j][3] && grid[i][j] == 'v') res++;
    }
    if (!flag) break;
  }

  if (!flag) puts("IMPOSSIBLE");
  else cout << res << endl;
  return;
}

int main() {
  //freopen("data.in", "r", stdin);
  //freopen("A-small-attempt0.in", "r", stdin);
  //freopen("A-large-practice.in", "r", stdin);
  //freopen("A-large.in", "r", stdin);
  //freopen("data.out", "w", stdout);
  int cas;
  scanf("%d", &cas);
  for (int i=1;i<=cas;i++) {
    printf("Case #%d: ",i);
    read();
    solve();
  }
  return 0;
}

