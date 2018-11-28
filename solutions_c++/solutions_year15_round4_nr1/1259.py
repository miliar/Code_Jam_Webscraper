#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

string problemName = "A";
string smallFileName = problemName + "-small-attempt0";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
//string fileName = smallFileName;
string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

vector<string> a;

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};
string g = "^v<>";
int n, m;

bool walkoff(int y, int x, int dir) {
  while (1) {
    y += dy[dir];
    x += dx[dir];
    if (y < 0 || x < 0 || y >= n || x >= m) return true;
    if (a[y][x] != '.') return false;
  }
}

int solve() {
  int changed = 0;
  REP (i, n) {
    REP (j, m) if (a[i][j] != '.') {
      int dir = g.find(a[i][j]);
      if (!walkoff(i, j, dir)) continue;
      bool ok = false;
      REP (change, 4) if (change != dir && !walkoff(i, j, change)) {
	ok = true;
	break;
      }
      if (!ok) {
	return -1;
      }
      changed++;
    }
  }
  return changed;
}

int main () {
    freopen(inputFileName.data(), "r", stdin);
    if (fileName == smallFileName || fileName == largeFileName)
    {
	freopen(outputFileName.data(), "w", stdout);
    }
    int T;
    cin >> T;
    REP (test, T) {
	cout << "Case #" << (test + 1) << ": ";
	cin >> n >> m;
	a.clear();
	a.resize(n);
	REP (i, n) {
	  cin >> a[i];
	}
	int res = solve();
	if (res < 0) cout << "IMPOSSIBLE\n"; else cout << res << endl;
    }
    return 0;
}
