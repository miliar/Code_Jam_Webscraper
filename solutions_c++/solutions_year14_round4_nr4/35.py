#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <climits>
#include <cassert>

#define INF (INT_MAX/2)
#define MAXNSERVER 100
#define MAXS 1000
#define MAXB (MAXS + MAXNSERVER + 10)

typedef long long lint;

const lint mod = 1000000007LL;

using namespace std;

int nserver;

lint bin[MAXB+1][MAXB+1];

lint binom(lint a, lint b) {
  assert(0 <= b && b <= a && a <= MAXB);
  return bin[a][b];
}

struct node {
  int many, manysum;
  map <char, node> child;
  
  lint exact[MAXNSERVER+1];
  lint atmost[MAXNSERVER+1];

  node() {
    many = manysum = 0;
    child.clear();
  }
  void add(char *s) {
    manysum++;
    if (*s) child[*s].add(s+1);
    else many++;
  }
  int result() {
    int ret = 0;
    for (map<char, node>::iterator it = child.begin(); it != child.end(); it++)
      ret += (it -> second).result();
    ret += min(manysum, nserver);
    return ret;
  }

  lint thisatmost(int div) {
    if (div == 0) {
      if (many == 0) return 1;
      else return 0;
    }
    return binom(many + div-1, div-1);
  }

  void dp() {
    for (map<char, node>::iterator it = child.begin(); it != child.end(); it++) {
      node &son = it -> second;
      son.dp();
    }

    for (int div = 0; div <= nserver; div++) {
      lint &amd = atmost[div];

      amd = 1;
      amd = (amd * thisatmost(div)) % mod;
      for (map<char, node>::iterator it = child.begin(); it != child.end(); it++) {
	node &son = it -> second;
	amd = (amd * (son.atmost[div]) ) % mod;
      }

      exact[div] = atmost[div];
      for (int sub = 0; sub < div; sub++) {
	exact[div] = (exact[div] - exact[sub] * binom(div, sub) % mod + mod) % mod;
	exact[div] = (exact[div]%mod + mod) % mod;
      }
    }

    const int need = min(nserver, manysum);
    for (int div = 0; div < need; div++) exact[div] = 0;

    for (int div = 0; div <= nserver; div++) {
      lint &amd = atmost[div];
      amd = 0;

      for (int sub = 0; sub <= div; sub++) {
	amd = (amd + exact[sub] * binom(div, sub) % mod) % mod;
      }
    }
  }
};

void precalc() {
  const int maxb = MAXB;

  for (int i = 0; i <= maxb; i++) bin[i][0] = bin[i][i] = 1;
  for (int i = 0; i <= maxb; i++)
    for (int j = 1; j < maxb; j++)
      bin[i][j] = (bin[i-1][j] + bin[i-1][j-1]) % mod;
}

int main() {
  precalc();

  int ntest;

  scanf("%d", &ntest);

  for (int t = 0; t < ntest; t++) {
    int ns;
    node root;

    scanf("%d %d", &ns, &nserver);

    for (int i = 0; i < ns; i++) {
      static char str[128];
      scanf(" %s", str);
      root.add(str);
    }

    int result = root.result();

    root.dp();

    printf("Case #%d: %d %d\n", t+1, result, (int)((root.exact[nserver]%mod + mod)%mod));
  }

  return 0;
}
