#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <assert.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
const int INF = 1000000000;
const int prime = 9241;
const ld pi = acos(-1.);


string s[1005];
string last[5];
int lcp(string a, string b)
{
   for (int i = 0; i  < (int)min(a.size(), b.size()); i++)
      if (a[i] != b[i]) return i;
   return min(a.size(), b.size());
}

void solve(int test)
{
   cerr << "test=" << test << endl;
   int m, n;
   cin >> m >> n;
   for (int i = 0; i < m; i++) cin >> s[i];
   sort(s, s + m);
   pair<int,int> mx = mp(0, -1);
   for (int mask = 0; mask < (1 << (2 * m)); mask++)
   {
      for (int i = 0; i < n; i++) last[i] = "";
      int ans = n;
      bool ok = 1;
      for (int i = 0; i < m && ok; i++)
      {
         int u = (mask >> (2*i)) & 3;
         if (u >= n) ok = 0;
      }
      if (!ok) continue;
      for (int i = 0; i < m; i++)
      {
         int u = (mask >> (2*i)) & 3;
         ans += s[i].size() - lcp(last[u], s[i]);
         last[u] = s[i];
      }
      for (int i = 0; i < n; i++) if (last[i] == "") ok = 0;
      if (!ok) continue;
      if (ans == mx.first) mx.second++;
      if (ans > mx.first) mx = mp(ans, 1);
   }
   cout << "Case #" << test << ": " << mx.first << ' ' << mx.second << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}