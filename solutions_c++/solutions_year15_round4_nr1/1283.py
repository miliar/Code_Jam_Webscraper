#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <math.h>
#include <cmath>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <climits>
#include <assert.h>

using namespace std;


typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> int2;
typedef pair<float, float> float2;
typedef pair<ull, ull> ull2;

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(s,i) for ( __typeof((s).begin()) i = ((s).begin())   ; i != (s).end(); ++i)  
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp(a,b) make_pair(a,b)
#define del(s,x) do {__typeof((s).begin()) abcde=(s).find(x); if(abcde !=(s).end()) s.erase(abcde); } while(0);
#define del2(s,x) do {__typeof((s).begin()) abcde=find(all(s),x); if(abcde !=(s).end()) s.erase(abcde); } while(0);

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)

int R = 0, C = 0;

bool montest (vector<vector<char> > &tab, int i, int j, int dx, int dy) {
  int x = j + dx;
  int y = i + dy;
  bool ok = false;
  FOR(k,0,max(R,C)) {
    if ((x >= 0) && (y >= 0) && (x < C) && (y < R)) {
      if (tab[y][x] != '.') {
	return true;
      }
      x += dx;
      y += dy;
    }
  }
  return false;
}

int main() {
  int T;
  cin >> T;
  cout.precision(12);
  FOR (test, 1, T+1) {
    cin >> R >> C;
    vector<vector<char> > tab(R, vector<char>(C,' '));
    FOR(i,0,R) FOR(j,0,C) cin >> tab[i][j];
    int cpt = 0;
    FOR(i,0,R) FOR(j,0,C) {
      if (tab[i][j] != '.') {
	int dx = 0, dy = 0;
	if (tab[i][j] == '>') {
	  dx = 1;
	}
	else if (tab[i][j] == '<') {
	  dx = -1;
	}
	else if (tab[i][j] == '^') 
	  dy = -1;
	else {
	  assert (tab[i][j] == 'v');
	  dy = 1;
	}
	bool ok1 = montest (tab, i, j, dx, dy);

	if (!ok1) {
	  ok1 |= montest (tab, i, j, 1, 0);
	  ok1 |= montest (tab, i, j, -1, 0);
	  ok1 |= montest (tab, i, j, 0, 1);
	  ok1 |= montest (tab, i, j, 0, -1);
	  cpt ++;
	}
	if (!ok1) {
	  goto imp;
	}
      }
    }
    cout << "Case #" << test << ": " << cpt << endl;
    continue;
  imp:
    cout << "Case #" << test << ": IMPOSSIBLE" << endl;
  }
  return 0;
}
