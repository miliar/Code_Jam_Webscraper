#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <bitset>
#include <queue>
using namespace std;

//conversion
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//typedef
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long ll;

//container util
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

//constant
const double EPS = 1e-10;
const int MAXI = 1234567890;

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;



void printList(vector<int>& v) {
  for (size_t i = 0; i < v.size(); i++) {
	cout << v[i] << " ";
  }
  cout << endl;
}

void printMatrix(vector< vector<int> >& v) {
  for (size_t i = 0; i < v.size(); i++) {
	printList(v[i]);
  }
  cout << endl;
}


int maxl(int dx, int dy, int x, int y, int N, VVI& tiles) {
  int r = 0;
  for (int i = 0; i < N; i++) {
    r = max(r, tiles[x + dx * i][y + dy * i]);
  }
  return r;
}

bool checkl(int t, int dx, int dy, int x, int y, int N, VVI& tiles) {
  for (int i = 0; i < N; i++) {
    if (tiles[x + dx * i][y + dy * i] > t) return false;
  }
  return true;
}

bool solve(int N, int M, VVI& tiles) {
  for (int i = 0; i < N; i++) {
    int m = maxl(0, 1, i, 0, M, tiles);
    for (int j = 0; j < M; j++) {
      if (tiles[i][j] == m) continue;
      if (!checkl(tiles[i][j], 1, 0, 0, j, N, tiles)) return false;
    }
  }

  for (int i = 0; i < M; i++) {
    int m = maxl(1, 0, 0, i, N, tiles);
    for (int j = 0; j < N; j++) {
      if (tiles[j][i] == m) continue;
      if (!checkl(tiles[j][i], 0, 1, j, 0, M, tiles)) return false;
    }
  }

  return true;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int N, M;
    cin >> N >> M;
    VVI tiles(N, VI(M, 0));
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < M; k++) {
	int t;
	cin >> t;
	tiles[j][k] = t;
      }
    }
    bool ans = solve(N, M, tiles);
    cout << "Case #" << i + 1 << ": ";
    if (ans) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
