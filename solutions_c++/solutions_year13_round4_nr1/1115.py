#include<cassert>
#include<complex>
#include<cstdlib>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<valarray>
#include<cstring>
#include<iomanip>

using namespace std;

#define rep(i, n) for (long long i = 0; i < (long long)(n); ++i)

typedef long long Int;
const Int B = 10000;      // base (power of 10)
const int BW = 4;         // log B
const int MAXDIGIT = 10; // it can represent 4*MAXDIGIT digits (in base 10)
struct BigNum {
  Int digit[MAXDIGIT];
  int size;
  BigNum(int size = 1, Int a = 0) : size(size) {
    memset(digit, 0, sizeof(digit));
    digit[0] = a;
  }
};
const BigNum ZERO(1, 0), ONE(1, 1);

// Comparators
bool operator<(BigNum x, BigNum y) {
  if (x.size != y.size) return x.size < y.size;
  for (int i = x.size-1; i >= 0; --i)
    if (x.digit[i] != y.digit[i]) return x.digit[i] < y.digit[i];
  return false;
}
bool operator >(BigNum x, BigNum y) { return y < x; }
bool operator<=(BigNum x, BigNum y) { return !(y < x); }
bool operator>=(BigNum x, BigNum y) { return !(x < y); }
bool operator!=(BigNum x, BigNum y) { return x < y || y < x; }
bool operator==(BigNum x, BigNum y) { return !(x < y) && !(y < x); }

// Utilities
BigNum normal(BigNum x) {
  Int c = 0;
  for (int i = 0; i < x.size; ++i) {
    while (x.digit[i] < 0)
      x.digit[i+1] -= 1, x.digit[i] += B;
    Int a = x.digit[i] + c;
    x.digit[i] = a % B;
    c          = a / B;
  }
  for (; c > 0; c /= B) x.digit[x.size++] = c % B;
  while (x.size > 1 && x.digit[x.size-1] == 0) --x.size;
  return x;
}
BigNum convert(Int a) {
  return normal(BigNum(1, a));
}
BigNum convert(const string &s) {
  BigNum x;
  int i = s.size() % BW;
  if (i > 0) i -= BW;
  for (; i < (int)s.size(); i += BW) {
    Int a = 0;
    for (int j = 0; j < BW; ++j)
      a = 10 * a + (i + j >= 0 ? s[i+j] - '0' : 0);
    x.digit[x.size++] = a;
  }
  reverse(x.digit, x.digit+x.size);
  return normal(x);
}
// Input/Output
ostream &operator<<(ostream &os, BigNum x) {
  os << x.digit[x.size-1];
  for (int i = x.size-2; i >= 0; --i)
    os << setw(BW) << setfill('0') << x.digit[i];
  return os;
}
istream &operator>>(istream &is, BigNum &x) {
  string s; is >> s;
  x = convert(s);
  return is;
}

// Basic Operations 
BigNum operator+(BigNum x, BigNum y) {
  if (x.size < y.size) x.size = y.size;
  for (int i = 0; i < y.size; ++i)
    x.digit[i] += y.digit[i];
  return normal(x);
}
BigNum operator-(BigNum x, BigNum y) {
  assert(x >= y);
  for (int i = 0; i < y.size; ++i)
    x.digit[i] -= y.digit[i];
  return normal(x);
}
BigNum operator*(BigNum x, BigNum y) {
  BigNum z(x.size + y.size);
  for (int i = 0; i < x.size; ++i)
    for (int j = 0; j < y.size; ++j)
      z.digit[i+j] += x.digit[i] * y.digit[j];
  return normal(z);
}
BigNum operator*(BigNum x, Int a) {
  for (int i = 0; i < x.size; ++i)
    x.digit[i] *= a;
  return normal(x);
}
pair<BigNum, Int> divmod(BigNum x, Int a) {
  Int c = 0, t;
  for (int i = x.size-1; i >= 0; --i) {
    t          = B * c + x.digit[i];
    x.digit[i] = t / a;
    c          = t % a;
  }
  return pair<BigNum, Int>(normal(x), c);
}
BigNum operator/(BigNum x, Int a) {
  return divmod(x, a).first;
}
Int operator%(BigNum x, Int a) {
  return divmod(x, a).second;
}
pair<BigNum, BigNum> divmod(BigNum x, BigNum y) {
  if (x.size < y.size) return pair<BigNum, BigNum>(ZERO, x);
  int F = B / (y.digit[y.size-1] + 1); // multiplying good-factor
  x = x * F; y = y * F;
  BigNum z(x.size - y.size + 1);
  for (int k = z.size-1, i = x.size-1; k >= 0; --k, --i) {
    z.digit[k]  = (i+1 < x.size ? x.digit[i+1] : 0) * B + x.digit[i];
    z.digit[k] /= y.digit[y.size-1];
    BigNum t(k + y.size);
    for (int m = 0; m < y.size; ++m)
      t.digit[k+m] = z.digit[k] * y.digit[m];
    t = normal(t);
    while (x < t) {
      z.digit[k] -= 1;
      for (int m = 0; m < y.size; ++m)
        t.digit[k+m] -= y.digit[m];
      t = normal(t);
    }
    x = x - t;
  }
  return pair<BigNum, BigNum>(normal(z), x / F);
}
BigNum operator/(BigNum x, BigNum y) {
  return divmod(x, y).first;
}
BigNum operator%(BigNum x, BigNum y) {
  return divmod(x, y).second;
}

typedef pair<long long, long long> P;

struct edge{long long to, cap, cost, rev;};

const int MAX_V = 2013;
const long long INF = 1e18;

int V;
vector<edge> G[MAX_V];
long long h[MAX_V];
long long dist[MAX_V];
long long prevv[MAX_V], preve[MAX_V];

void add_edge(int from, int to, long long cap, long long cost) {
  G[from].push_back((edge){to, cap, cost, (int)G[to].size()});
  G[to].push_back((edge){from, 0, -cost, (int)G[from].size() - 1});
}

BigNum min_cost_flow(long long s, long long t, long long f) {
  BigNum res = 0;
  fill(h, h + V , 0);
  while (f > 0) {
    priority_queue<P, vector<P>, greater<P> > que;
    fill(dist, dist + V, INF);
    dist[s] = 0;
    que.push(P(0, s));
    while (!que.empty()) {
      P p = que.top(); que.pop();
      long long v = p.second;
      if (dist[v] < p.first) continue;
      for (int i = 0; i < (int)G[v].size(); i++) {
	edge &e = G[v][i];
	if (e.cap > 0 && dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]) {
	  dist[e.to] = dist[v] + e.cost + h[v] - h[e.to];
	  prevv[e.to] = v;
	  preve[e.to] = i;
	  que.push(P(dist[e.to], e.to));
	}
      }
    }
    if (dist[t] == INF) {
      return -1;
    }
    for (int v = 0; v < V; v++) h[v] = h[v] + dist[v];
    long long d = f;
    for (int v = t; v != s; v = prevv[v]) {
      d = min(d, G[prevv[v]][preve[v]].cap);
    }
    f = f - d;
    res = res + convert(d) * convert(h[t]);
    for (int v = t; v != s; v = prevv[v]) {
      edge &e = G[prevv[v]][preve[v]];
      e.cap -= d;
      G[v][e.rev].cap += d;
    }
  }
  return res;
}

int uf[2013];
int root(int x) { return (uf[x] < 0) ? x : (uf[x] = root(uf[x])); }
bool conn(int x, int y) {
  x = root(x); y = root(y);
  if (x == y) return 0;
  if (uf[x] > uf[y]) swap(x, y);
  uf[x] += uf[y]; uf[y] = x;
  return 1;
}

int main() {
  int t;
  cin >> t;
  rep (iii, t) {
    cout << "Case #" << iii + 1 << ": ";
    rep (i, MAX_V) G[i].clear();
    int n, m;
    cin >> n >> m;
    long long sum = 0;
    BigNum pre = 0;
    vector<pair<int, int> > ft;
    rep (i, m) {
      int from, to, pi;
      cin >> from >> to >> pi;
      --from; --to;
      add_edge(2 * n, from, pi, 0);
      add_edge(to + n, 2 * n + 1, pi, 0);
      sum += pi;
      pre = pre + convert((long long)(2 * n + 1 - (to - from)) * (to - from) / 2) * convert(pi);
      ft.push_back(make_pair(from, to));
    }
    sort(ft.begin(), ft.end());
    rep (i, m) uf[i] = -1;
    rep (i, m) rep (j, i) if (ft[i].first <= ft[j].second) conn(i, j);
    rep (i, m) rep (j, m) {
      if (ft[i].second < ft[j].first) continue;
      if (root(i) != root(j)) continue;
      add_edge(ft[j].first, ft[i].second + n, 1e12, (long long)(2 * n + 1 - (ft[i].second - ft[j].first)) *  (ft[i].second - ft[j].first) / 2);
    }
    V = 2 * n + 2;
    /*
    rep (i, 2 * n + 2) {
      rep (j, G[i].size()) cout << i << " " << G[i][j].to << " " << G[i][j].cost << endl;
    }
    */
    cout << ((pre - min_cost_flow(2 * n, 2 * n + 1, sum)) % convert(1000002013)) << endl;;
  }
  return 0;
}
