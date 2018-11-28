//Author: Harhro94 [Harutyunyan Hrayr]
//#pragma comment(linker, "/STACK:667777216")
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <bitset>
//#include <unordered_map>
//#include <unordered_set>
using namespace std;

#define FOR(i, n) for (int i = 0; i < (n); ++i)
typedef long long LL;
typedef long double LD;
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()
int rd();

const LD eps = 1e-12;
struct pipe {
   LD r, T;
   pipe(LD r = 0, LD t = 0) : r(r), T(T) {}

   bool operator < (const pipe &o) const {
      return T < o.T;
   }
};

LD calc(vector<pipe> &a, LD t, bool &ok, LD V0) {
   LD maxv = 0.0;
   FOR(i, sz(a)) {
      maxv += a[i].r * t;
   }
   if (maxv < V0 - eps) {
      ok = false;
      return 0;
   }
   LD curv = 0;
   LD curt = 0;
   FOR(i, sz(a)) {
      LD mx = min(a[i].r * t, V0 - curv);
      curt = (curt * curv + mx * a[i].T) / (mx + curv);
      curv += mx;
   }
   return curt;
}

void solve() {
   int tcnt;
   scanf("%d", &tcnt);
   for (int test = 1; test <= tcnt; ++test) {

      int n;
      LD V0, T0;
      cin >> n >> V0 >> T0;
      vector<pipe> a(n);
      FOR(i, n) cin >> a[i].r >> a[i].T;

      LD l = 0, r = 1e16;

      sort(all(a));

      FOR(iter, 150) {
         LD t = (l + r) / 2;
         bool ok = true;

         LD tmin = calc(a, t, ok, V0);
         reverse(all(a));
         LD tmax = calc(a, t, ok, V0);
         reverse(all(a));

         if (ok && T0 > tmin - eps && T0 < tmax + eps) ok = true;
         else ok = false;

         if (ok) r = t;
         else l = t;
      }

      cout << "Case #" << test << ": ";
      if (l + 1 > 1e16) cout << "IMPOSSIBLE" << endl;
      else cout << fixed << setprecision(14) << l << endl;
   }
}

int rd() {
   return (((LL)rand() << 16) ^ rand()) % 1000000000;

}

void testGen() {
   FILE *f = fopen("input.txt", "w");
   fclose(f);
}

int main() {
#ifdef harhro94
   //testGen();
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
#else
#define task "ghosts"
   //freopen(task".in", "r", stdin);
   //freopen(task".out", "w", stdout);
#endif

   cerr << fixed;
   cerr.precision(9);

   solve();

#ifdef harhro94
   cerr << fixed << setprecision(3) << "\nExecution time = " << clock() / 1000.0 << "s\n";
#endif
   return 0;
}