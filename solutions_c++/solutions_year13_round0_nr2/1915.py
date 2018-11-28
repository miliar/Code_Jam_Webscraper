#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cmath> 
#include <ctime> 
#include <float.h> 

using namespace std; 

#define REP(i, from, to) for (int i = (from); i < (to); ++i) 
#define FOR(i, n) REP(i, 0, (n)) 
#define ALL(x) x.begin(), x.end() 
#define SIZE(x) (int)x.size() 
#define PB push_back 
#define MP make_pair 

typedef long long i64; 
typedef vector<int> VI; 
typedef vector<VI> VVI; 
typedef vector<string> VS; 
typedef vector<VS> VVS; 
typedef pair<int, int> PII; 

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int t;
  cin >> t;

  FOR (tt, t) {
    int n, m;
    cin >> n >> m;

    VVI board(n, VI(m));
    FOR (i, n) FOR (j, m) cin >> board[i][j];
    VVI cur(n, VI(m, 100));

    while (true) {
      bool wasCut = false;

      FOR (i, n) FOR (j, m) if (cur[i][j] != board[i][j]) {
        bool hasGreaterInRow = false;
        FOR (k, m) hasGreaterInRow |= board[i][k] > board[i][j];
        if (!hasGreaterInRow) {
          FOR (k, m) cur[i][k] = board[i][j];
          wasCut = true;
        }

        bool hasGreaterInCol = false;
        FOR (k, n) hasGreaterInCol |= board[k][j] > board[i][j];
        if (!hasGreaterInCol) {
          FOR (k, n) cur[k][j] = board[i][j];
          wasCut = true;
        }
      }

      if (!wasCut) break;
    }

    bool res = cur == board;
    cout << "Case #" << tt + 1 << ": " << (res ? "YES" : "NO") << endl;
  }

  return 0;
}