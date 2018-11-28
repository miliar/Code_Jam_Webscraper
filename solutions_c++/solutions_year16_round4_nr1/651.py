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

int N;
int win[3][2] = {{0,1}, {1,2}, {0,2}};
string seq[13][3];
string PRT = "PRS";
int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(i,0,3) seq[0][i] = '0' + i;
  REP(k,1,13) {
    REP(g,0,3) {
      int a = win[g][0], b = win[g][1];
      string s1 = seq[k-1][a] + seq[k-1][b];
      string s2 = seq[k-1][b] + seq[k-1][a];
      seq[k][g] = s1 < s2 ? s1 : s2;
    }
  }
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    //cerr << csn << endl;
    int need[3];
    cin >> N;
    cin >> need[1] >> need[0] >> need[2];
    string ans;
    REP(g,0,3) {
      int cnt[3] = {};
      REP(i,0,1<<N) cnt[seq[N][g][i] - '0']++;
      bool ok = 1;
      REP(i,0,3) if (cnt[i] != need[i]) { ok = 0; break; }
      if (ok) {
        if (ans.length() == 0) ans = seq[N][g];
        else ans = min(seq[N][g], ans);
      }
    }
    if(!ans.length()) puts("IMPOSSIBLE");
    else {
      REP(i,0,1<<N) printf("%c", PRT[ans[i] - '0']);
      puts("");
    }
  }
  return 0;
}
