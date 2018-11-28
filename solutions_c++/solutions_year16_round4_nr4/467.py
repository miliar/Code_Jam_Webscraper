#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 100005

int N, g[25][25], ng[25][25];
bool check() {
  int order[4];
  REP(i,0,N) order[i] = i;
  do {
    int mac[4];
    REP(j,0,N) mac[j] = j;
    do {
      bool v[4] = {};
      REP(i,0,N) {
        int w = order[i], m = mac[i];
        int pos = 0;
        REP(j,0,N) {
          if (!v[j] && ng[w][j]) pos++;
        }
        if (pos == 0) return 0;
        if (!ng[w][m]) break;
        v[m] = 1;
      }
    } while(next_permutation(mac, mac+N));
  } while(next_permutation(order,order+N));
  return 1;
}
int main() {
  freopen("input", "r", stdin);
  //freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    //cerr << csn << endl;
    cin >> N;
    REP(i,0,N) {
      char s[30];
      scanf("%s", s);
      REP(j,0,N) g[i][j] = s[j] - '0';
    }
    int ans = INF;
    REP(m,0,1<<(N*N)){
      int sol = 0;
      REP(i,0,N) {
        REP(j,0,N) {
          ng[i][j] = g[i][j] | ((m & (1<<(N*i+j)))>0);
          if (!g[i][j] && ng[i][j]) sol++;
        }
      }
      /*
      REP(i,0,N) {
        REP(j,0,N) {
          cerr << ng[i][j];
        }
        cerr << endl;
      }
      cerr << endl;
       */
      if (check()) ans = min(ans, sol);
    }
    printf("%d\n", ans);
  }
  return 0;
}
