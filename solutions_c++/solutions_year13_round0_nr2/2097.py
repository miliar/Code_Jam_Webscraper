#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define NDEBUG
#ifdef NDEBUG
#define DEBUG if (false)
#else
#define DEBUG if (true)
#endif

#pragma GCC diagnostic warning "-Wall"
#define WRITE(x) DEBUG { cout << x << endl; }
#define WATCH(x) DEBUG { cout << #x << " = " << x << endl; }
#define ALL(x) (x).begin(), (x).end()
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

const int inf = 0x3f3f3f3f;

bool go(vector<vector<int> > & board, 
        vector<bool> & il, 
        vector<bool> & ic)
{
  int m = board.size();
  int n = board[0].size();

  FORN(i, 0, m) WATCH(il[i]);
  WRITE("");
  FORN(j, 0, n) WATCH(ic[j]);
  WRITE("--------");

  bool is_base_case = true;
  FORN(i, 0, m) if (!il[i]) 
    FORN(j, 0, n) if (!ic[j])  
      is_base_case = false;
  if (is_base_case)
    return true;

  int im = 0, jm = 0, vm = inf;
  FORN(i, 0, m) if (!il[i]) {
    FORN(j, 0, n) if (!ic[j]) {
      if (board[i][j] < vm) im = i, jm = j, vm = board[i][j];
    }
  }
  assert(not il[im] and not ic[jm]);

  bool okc = true;
  FORN(i, 0, m) if (!il[i]) 
    okc &= board[i][jm] == board[im][jm];

  bool okl = true;
  FORN(j, 0, n) if (!ic[j])
    okl &= board[im][j] == board[im][jm];

  if (okc) {
    ic[jm] = true;
    return go(board, il, ic);
  } else if (okl) {
    il[im] = true;
    return go(board, il, ic);
  } else {
    return false;
  }
  
}

int main(){
	//Descomente para acelerar cin
	//ios::sync_with_stdio(false);
	int ntc; cin >> ntc;
	FORN(tc, 1, ntc+1) {
    int m, n; cin >> m >> n;
    vector<vector<int> > board(m, vector<int>(n));
    vector<bool> ic(n), il(m);
    FORN(i, 0, m) FORN(j, 0, n) cin >> board[i][j];

    WATCH(m); WATCH(n);
    bool ok = go(board, il, ic);
    cout << "Case #" << tc << ": " << (ok ? "YES" : "NO") << endl;
  }
	
}
