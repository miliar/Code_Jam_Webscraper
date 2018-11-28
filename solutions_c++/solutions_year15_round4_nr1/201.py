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

const int N = 107;
char st[N][N];
int n, m, row[N], col[N];

void solve() {
   int T;
   scanf("%d", &T);
   for (int test = 1; test <= T; ++test) {
      scanf("%d%d", &n, &m);
      FOR(i, n) scanf("%s", st[i]);

      memset(row, 0, sizeof row);
      memset(col, 0, sizeof col);

      FOR(i, n) FOR(j, m) if (st[i][j] != '.') {
         ++row[i];
         ++col[j];
      }

      bool flag = false;

      FOR(i, n) FOR(j, m) if (st[i][j] != '.') {
         if (row[i] == 1 && col[j] == 1) {
            flag = true;
         }
      }

      int ans = 0;
      FOR(x, n) FOR(y, m) if (st[x][y] != '.') {
         int dx = 0, dy = 0;
         if (st[x][y] == '^') dx = -1;
         if (st[x][y] == 'v') dx = 1;
         if (st[x][y] == '>') dy = 1;
         if (st[x][y] == '<') dy = -1;
         int tx = x + dx;
         int ty = y + dy;
         while (tx >= 0 && ty >= 0 && tx < n && ty < m && st[tx][ty] == '.') {
            tx += dx;
            ty += dy;
         }
         if (tx < 0 || ty < 0 || tx >= n || ty >= m) ++ans;
      }


      printf("Case #%d: ", test);
      if (flag) printf("IMPOSSIBLE\n");
      else printf("%d\n", ans);
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