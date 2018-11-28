#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()
#define mp make_pair

using namespace std;
typedef long long ll;

void testCase()
{
  int h, w;
  cin >> h >> w;
  vector<vector<int> > f(h, vector<int>(w));
  vector<vector<int> > u(h, vector<int>(w, 0));
  for (int y = 0; y < h; y++)
    for (int x = 0; x < w; x++)
      cin >> f[y][x];
  for (int y = 0; y < h; y++)
  {
    int mx = f[y][0];
    for (int x = 0; x < w; x++)
      mx = max(mx, f[y][x]);
    for (int x = 0; x < w; x++)
      if (mx == f[y][x])
        u[y][x] = true;
  }
  for (int x = 0; x < w; x++)
  {
    int mx = f[0][x];
    for (int y = 0; y < h; y++)
      mx = max(mx, f[y][x]);
    for (int y = 0; y < h; y++)
      if (mx == f[y][x])
        u[y][x] = true;
  }
  for (int y = 0; y < h; y++)
    for (int x = 0; x < w; x++)
      if (!u[y][x])
      {
        printf("NO\n");
        return;
      }
  printf("YES\n");
}

int main() {
//  freopen("sample.in", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int n;
  cin >> n;
  string s;
  getline(cin, s);
  for (int ti = 0; ti < n; ++ti) {
    printf("Case #%i: ", ti + 1);
    testCase();
    getline(cin, s);
  }
  return 0;
}
