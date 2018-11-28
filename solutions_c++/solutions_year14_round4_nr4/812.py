#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;

const int maxn = 4, maxm = 8;
int n, m;
vector<string> s;

int maxAns = 0, maxCnt = 0;
int index[maxm];

void Solve()
{
  set<string> ss[maxn];
  for (int i = 0; i < m; i++)
  {
    for (int j = 0; j <= sz(s[i]); j++)
      ss[index[i]].insert(s[i].substr(0, j));
  }
  int ans = 0;
  for (int i = 0; i < n; i++)
    ans += sz(ss[i]);
  if (ans == maxAns)
    maxCnt++;
  else if (ans > maxAns)
    maxCnt = 1, maxAns = ans;
}

void Go(int p)
{
  if (p == m)
  {
//    for (int i = 0; i < m; i++)
//      cerr << index[i] << " ";
//    cerr << endl;
    Solve();
    return;
  }
  for (int i = 0; i < n; i++)
  {
    index[p] = i;
    Go(p + 1);
  }
}

void testCase()
{
  cin >> m >> n;
  s.resize(m);
  for (int i = 0; i < m; i++)
    cin >> s[i];

  maxAns = 0;
  maxCnt = 0;
  Go(0);
  printf("%d %d\n", maxAns, maxCnt);
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T;
  cin >> T;
//  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    cerr << "Case #" << t << ": " << endl;
    printf("Case #%d: ", t);
    testCase();
  }
  return 0;
}
