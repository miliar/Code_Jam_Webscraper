#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>

using namespace std;

#define FOR(k,a,b) for(typeof(a) k=(a); k < (b); k++)
#define FORE(k,a,b) for(typeof(a) k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define SZ(x) ((int)((x).size()))
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define EXIST(s,e) ((s).find(e)!=(s).end())

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1e+9;
const double EPS = 1e-10;
const double PI = acos(-1.0);

int lawn[100][100];

bool check(int r, int c, int N, int M) {
  bool ok_r = true;
  REP(nr, N) {
    if(nr == r) continue;
    if(lawn[r][c] < lawn[nr][c]) { ok_r = false; break; }
  }

  bool ok_c = true;
  REP(nc, M) {
    if(nc == c) continue;
    if(lawn[r][c] < lawn[r][nc]) { ok_c = false; break; }
  }
  
  return ok_r || ok_c;
}

int main()
{
  int T;
  cin >> T;
  REP(turn, T) {
    int N, M;
    cin >> N >> M;
    REP(i, N) REP(j, M) { cin >> lawn[i][j]; }

    bool ok = true;
    REP(r, N) REP(c, M) {
      if(!check(r, c, N, M)) {
        ok = false; break;
      }
    }

    if(ok) {
      printf("Case #%d: YES\n", turn+1);
    }
    else {
      printf("Case #%d: NO\n", turn+1);
    }
  }
  
  return 0;
}
