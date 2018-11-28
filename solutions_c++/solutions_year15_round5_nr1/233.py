//#pragma comment(linker, "/STACK:66777216")
#define _CRT_SECURE_NO_WARNINGS
//#include <unordered_set>
//#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <complex>
#include <cstring>
#include <cstdio>
#include <bitset>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>	
#include <complex>
using namespace std;

#define FOR(i, n) for (int i = 0; i < (n); ++i)
typedef long long LL;
typedef long double LD;
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()

const int N = 1000007;
int n, D, s[N], par[N];
vector<int> G[N];
int timer, L[N], R[N];
int upcnt[N], rev[N];
struct node {
   int maxi, cnt, add;
   node(int maxi = 0, int cnt = 0, int add = 0) : maxi(maxi), cnt(cnt), add(add) { }
} T[4 * N];

void dfs(int u, int up = 0) {
   rev[timer] = u;
   L[u] = timer++;
   upcnt[u] = up + 1;
   for (int to : G[u]) {
      dfs(to, up + 1);
   }
   R[u] = timer - 1;
}

node merge(node A, node B) {
   node ret;
   ret.maxi = max(A.maxi + A.add, B.maxi + B.add);
   if (A.maxi + A.add == ret.maxi) ret.cnt += A.cnt;
   if (B.maxi + B.add == ret.maxi) ret.cnt += B.cnt;
   return ret;
}

void build(int v, int tl, int tr) {
   if (tl == tr) {
      T[v] = node(-upcnt[rev[tl]], 1, 0);
      return;
   }
   int tm = (tl + tr) / 2;
   build(2 * v, tl, tm);
   build(2 * v + 1, tm + 1, tr);
   T[v] = merge(T[2 * v], T[2 * v + 1]);
}

void push(int v) {
   T[2 * v].add += T[v].add;
   T[2 * v + 1].add += T[v].add;
   T[v].maxi += T[v].add;
   T[v].add = 0;
}

void update(int v, int tl, int tr, int l, int r, int delta) {
   if (tl == l && tr == r) {
      T[v].add += delta;
      return;
   }
   push(v);
   int tm = (tl + tr) / 2;
   if (r <= tm) update(2 * v, tl, tm, l, r, delta);
   else if (l > tm) update(2 * v + 1, tm + 1, tr, l, r, delta);
   else {
      update(2 * v, tl, tm, l, tm, delta);
      update(2 * v + 1, tm + 1, tr, tm + 1, r, delta);
   }
   T[v] = merge(T[2 * v], T[2 * v + 1]);
}

void add(int u) {
   //cerr << "add " << u << endl;
   update(1, 0, n - 1, L[u], R[u], +1);
}

void del(int u) {
   //cerr << "del " << u << endl;
   update(1, 0, n - 1, L[u], R[u], -1);
}

int getCur() {
   if (T[1].maxi + T[1].add == 0) return T[1].cnt;
   return 0;
}

void solve() {
   int T;
   int AS, CS, RS;
   int AM, CM, RM;
   scanf("%d", &T);
   for (int test = 1; test <= T; ++test) {
      scanf("%d%d", &n, &D);
      scanf("%d%d%d%d", &s[0], &AS, &CS, &RS);
      scanf("%d%d%d%d", &par[0], &AM, &CM, &RM);
      for (int i = 1; i < n; ++i) {
         s[i] = (s[i - 1] * AS + CS) % RS;
         par[i] = (par[i - 1] * AM + CM) % RM;
      }
      par[0] = 0;
      for (int i = 1; i < n; ++i) {
         par[i] %= i;
      }
      FOR(i, n) G[i].clear();
      FOR(i, n) {
         if (i) G[par[i]].pb(i);
      }
      timer = 0;
      dfs(0);
      build(1, 0, n - 1);
      /*
      FOR(i, n) {
         cerr << i << " " << par[i] << " " << s[i] << endl;
         cerr << i << " " << L[i] << " " << R[i] << endl;
      }
      */
      vector<pair<int, int> > mas;
      FOR(i, n) {
         mas.pb(mp(s[i], i));
      }
      sort(all(mas));
      int r = 0;
      while (r < sz(mas) && mas[r].first - mas[0].first <= D) {
         add(mas[r].second);
         ++r;
      }
      
      int ans = getCur();
      
      for (int l = 1; l < n; ++l) {
         del(mas[l - 1].second);
         while(r < sz(mas) && mas[r].first - mas[l].first <= D) {
            add(mas[r].second);
            ++r;
         }
         //cerr << "now = " << getCur() << endl;
         ans = max(ans, getCur());
      }

      printf("Case #%d: %d\n", test, max(ans, 1));
   }   
}

void testGen() {
   FILE *f = fopen("input.txt", "w");
   fclose(f);
}

int main()
{
#ifdef harhro94
   //testGen();
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
#else
#define task "grid"
   //freopen(task".in", "r", stdin);
   //freopen(task".out", "w", stdout);
#endif

   cerr << fixed;
   cerr.precision(3);
   cout << fixed;
   cout.precision(9);

   solve();

#ifdef harhro94
   cerr << fixed << setprecision(3) << "\nExecution time = " 
        << clock() / (double)CLOCKS_PER_SEC << "s\n";
#endif
   return 0;
}
