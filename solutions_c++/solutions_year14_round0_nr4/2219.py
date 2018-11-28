/** 
 *
 * rais.fathin38
 */

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cctype>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <utility>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <bitset>
#include <complex>

using namespace std;

#define ALL(a) a.begin(), a.end()
#define SZ(a) ((int)a.size())

#define MIN(a, b) a = min(a, b)
#define MAX(a, b) a = max(a, b)

#define SHOW(x) { cerr << ">>> " << #x << " : " << x << endl; }

#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef long long LL;
typedef pair<int, int> pii;

const int N = 1001;

int n;
int a[N];
int b[N];
int owner[N];
bool visit[N];
vector<int> adj[N];

int match(int u) {
  if (visit[u]) return 0;
  visit[u] = true;
  for (int &v : adj[u]) {
    if (owner[v] == -1 || match(owner[v])) {
      owner[v] = u;
      return 1;
    }
  }
  return 0;
}

int main() {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      double t; scanf("%lf", &t);
      a[i] = (int)(t * 100000);
    }
    for (int i = 0; i < n; i++) { 
      double t; scanf("%lf", &t);
      b[i] = (int)(t * 100000);
    }
    sort(a, a + n);
    sort(b, b + n);
    int d = 0, w = 0;
    for (int i = 0, j = 0; i < n; i++) {
      while (j < n && b[j] <= a[i]) j++;
      if (j == n) w++;
      else j++;
    }
    for (int i = 0; i < n; i++) adj[i].clear();
    for (int i = 0; i < n; i++) {
      owner[i] = -1;
      for (int j = 0; j < n; j++) if (a[i] > b[j]) adj[i].pb(j);
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) visit[j] = false;
      d += match(i);
    }
    printf("Case #%d: %d %d\n", t, d, w);
  }
  return 0;
}

