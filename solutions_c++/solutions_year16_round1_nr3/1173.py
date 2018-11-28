#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second
#define vi vector<int>
#define vii vector< pii >

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

int T;
int N;
int F[1005];
int in_deg[1005];
int len[1005];
bool del[1005];

int main() {
  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%d", &N);
    REP(i, N) in_deg[i] = 0;
    REP(i, N) len[i] = 0;
    REP(i, N) del[i] = false;
    REP(i, N) {
      scanf("%d", F + i);
      --F[i];
      ++in_deg[F[i]];
    }
    REP(i, N) {
      REP(j, N) {
        if (del[j]) continue;
        if (in_deg[j] == 0) {
          --in_deg[F[j]];
          del[j] = true;
          len[F[j]] = len[j] + 1;
        }
      }
    }
    int best1 = 0;
    int bestc = 0;
    REP(i, N) {
      if (del[i]) continue;
      if (F[F[i]] == i) {
        int now = len[i] + len[F[i]] + 2;
        best1 += now;
        del[i] = true;
        del[F[i]] = true;
      } else {
        int clen = 1;
        int j = i;
        del[i] = true;
        while (F[j] != i) { j = F[j]; ++clen; del[j] = true; }
        if (clen > bestc) bestc = clen;
      }
    }
    int best = max(best1, bestc);
    printf("Case #%d: %d\n", t, best);
  }

  return 0;
}
