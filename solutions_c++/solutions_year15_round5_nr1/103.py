#include <cassert>
#include <cstring>

#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAXN = 2e6 + 123;

int n, d;
int dad[MAXN];
vector<int> E[MAXN];

int isok[MAXN];
int insol[MAXN];
llint S[MAXN];

int cnt_intree = 0;

void dfs_on(int x) {
  if (!isok[x]) return ;
  insol[x] = true;
  ++cnt_intree;
  for (int y : E[x]) {
    dfs_on(y);
  }
}

void dfs_off(int x) {
  if (!insol[x]) return;
  insol[x] = false; --cnt_intree;
  for (int y : E[x]) {
    dfs_off(y);
  }
}

int main(void) {
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    printf("Case #%d: ", tc+1); fflush(stdout);

    cin >> n >> d;
    llint s0, as, cs, rs; cin >> s0 >> as >> cs >> rs;
    llint m0, am, cm, rm; cin >> m0 >> am >> cm >> rm;

    static llint M[MAXN];
    S[0] = s0; M[0] = m0;
    for (int i = 0; i < n; ++i) {
      S[i+1] = (S[i]*as + cs) % rs;
      M[i+1] = (M[i]*am + cm) % rm;
    }

    REP(i, n) {
      E[i].clear();
      isok[i] = 0;
      insol[i] = 0;
    }
    cnt_intree = 0;

    dad[0] = -1;
    for (int i = 1; i < n; ++i) {
      dad[i] = M[i] % i;
      E[dad[i]].push_back(i);
    }    

    vector<int> idxs; REP(i, n) idxs.push_back(i);
    sort(idxs.begin(), idxs.end(), [](int a, int b) { return S[a] < S[b]; });

    int ans = 0;
    int a = 0;
    REP(b, n) {
      // turn ok idxs[b]
      isok[idxs[b]] = true;
      if (dad[idxs[b]] == -1 || insol[dad[idxs[b]]]) {
        dfs_on(idxs[b]);
      }

      while (S[idxs[b]] - S[idxs[a]] > d) {
        // turn off idxs[a]
        if (insol[idxs[a]]) {
          dfs_off(idxs[a]);
        }
        isok[idxs[a]] = false;
        ++a;
      }

      ans = max(ans, cnt_intree);
    }

    printf("%d\n", ans); fflush(stdout);
  }

  return 0;
}   
