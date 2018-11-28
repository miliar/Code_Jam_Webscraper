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

const int N = 1000007;
char st[N];
bool mark1[N], mark2[N], c1[N], c2[N];

vector<string> parse() {
   vector<string> ans;
   int len = strlen(st);
   for (int i = 0; i < len;) {
      while (i < len && st[i] == ' ') ++i;
      if (i == len) break;
      int j = i;
      string cur = "";
      while (j < len && (st[j] >= 'a' && st[j] <= 'z')) {
         cur += st[j++];
      }
      ans.pb(cur);
      i = j;
   }
   return ans;
}

int add(string &x, map<string, int> &ID, int &curid) {
   if (ID.count(x)) return ID[x];
   ID[x] = curid++;
   return curid - 1;
}

void solve() {
   int tcnt;
   scanf("%d\n", &tcnt);
   for (int test = 1; test <= tcnt; ++test) {
      cerr << "test = " << test << endl;

      int n;
      scanf("%d\n", &n);
      gets(st);
      vector<string> one = parse();
      gets(st);
      vector<string> two = parse();

      vector<vector<string> > mas(n - 2);
      FOR(i, n - 2) {
         gets(st);
         mas[i] = parse();
      }

      map<string, int> ID;
      int curid = 0;
      for (auto x : one) {
         int id = add(x, ID, curid);
         mark1[id] = true;
      }
      for (auto x : two) {
         int id = add(x, ID, curid);
         mark2[id] = true;
      }

      vector<vector<int> > masid(n - 2);

      FOR(i, n - 2) {
         for (auto x : mas[i]) {
            masid[i].pb(add(x, ID, curid));
         }
      }

      int ans = 1 << 30;

      FOR(mask, 1 << (n - 2)) {

         FOR(i, curid) {
            c1[i] = mark1[i];
            c2[i] = mark2[i];
         }

         FOR(i, n - 2) {
            if ((mask >> i) & 1) {
               for (auto x : masid[i]) {
                  c1[x] = true;
               }
            }
            else {
               for (auto x : masid[i]) {
                  c2[x] = true;
               }
            }
         }

         int cur = 0;
         FOR(i, curid) {
            if (c1[i] && c2[i]) ++cur;
         }
         ans = min(ans, cur);
      }

      FOR(i, curid + 1) {
         mark1[i] = mark2[i] = 0;
         c1[i] = c2[i] = 0;
      }

      printf("Case #%d: %d\n", test, ans);
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