// Author: Harhro94 [Harutyunyan Hrayr]
#pragma comment(linker, "/STACK:66777216")
#define _CRT_SECURE_NO_WARNINGS
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <iomanip>
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
#include <vector>
using namespace std;

typedef long long LL;
typedef long double LD;
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()

const int N = 100007;

void testGen()
{
   FILE *f = fopen("input.txt", "w");

   fclose(f);
};

int main()
{
#ifdef harhro94
   //testGen();
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
#else
#define task "angle"
   //freopen(task".in", "r", stdin);
   //freopen(task".out", "w", stdout);
#endif

   int T;
   scanf("%d", &T);
   for (int test = 1; test <= T; ++test)
   {
      printf("Case #%d: ", test);

      int n, x;
      scanf("%d%d", &n, &x);
      vector<int> a(n);
      for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
      multiset<int> S(all(a));
      int ans = 0;
      while (!S.empty())
      {
         int cur = *S.begin();
         S.erase(S.begin());
         ++ans;
         if (S.empty()) break;
         auto it = S.lower_bound(x - cur);
         if (it == S.end())
         {
            --it;
            S.erase(it);
         }
         else if (*it == x - cur) S.erase(it);
         else if (it != S.begin()) S.erase(--it);
      }
      printf("%d\n", ans);
   }

#ifdef harhro94
   cerr << fixed << setprecision(3) << "\nExecution time = " << clock() / 1000.0 << "s\n";
#endif
   return 0;
}