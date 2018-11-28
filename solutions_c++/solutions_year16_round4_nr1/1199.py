#pragma comment (linker, "/STACK:268435456")
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <cmath>
#include <cctype>
#include <sstream>
#include <ctime>
#include <tuple>
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;
template <typename T> using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
template <typename T> T sqr(T r) { return r * r; }

string young(string s)
{
  if (s == "R")
    return "S";
  if (s == "P")
    return "R";
  return "P";
}

string find(int n, string top)
{
  if (n == 0)
    return top;
  string a1 = find(n - 1, top);
  string a2 = find(n - 1, young(top));
  return a1 < a2 ? a1 + a2 : a2 + a1;
}

string solve(int n, int r, int p, int s, string top)
{
  string res = find(n, top);
  //cout << top << " " << res << endl;
  for (auto c : res)
    if (c == 'R')
      r--;
    else if (c == 'P')
      p--;
    else
      s--;
  if (!r && !p && !s)
    return res;
  else
    return "U";
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn;
  cin >> tn;
  for (int tc = 0; tc < tn; tc++)
  {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    string best = "U";
    best = min(best, solve(n, r, p, s, "R"));
    best = min(best, solve(n, r, p, s, "P"));
    best = min(best, solve(n, r, p, s, "S"));
    if (best == "U")
      best = "IMPOSSIBLE";
    cout << "Case #" << tc + 1 << ": " << best << endl;
  }
  return 0;
}
