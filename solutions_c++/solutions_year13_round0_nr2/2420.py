#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
typedef  long long   ll;


#define ALL(x)   (x).begin(),(x).end()
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-9;
const double PI = acos(-1.0);




template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}



int mat[111][111];

int main() {
  int casos; cin >> casos;
  for (int h = 0 ; h < casos; ++h) {
    int rows, cols; cin >> rows >> cols;
    int maxCol[111], maxRow[111];
    memset(maxCol, 0, sizeof(maxCol)); memset(maxRow, 0, sizeof(maxRow));
    REP(ii, rows) REP(jj, cols) {
      cin >> mat[ii][jj];
      maxCol[jj] = max(maxCol[jj], mat[ii][jj]);
      maxRow[ii] = max(maxRow[ii], mat[ii][jj]);
    }
    bool ok = true;
    REP(ii, rows) REP(jj, cols) {
      if (min(maxCol[jj], maxRow[ii]) > mat[ii][jj])
        ok = false; 
    }
    printf("Case #%d: %s\n", h+1, ok?"YES":"NO");
  }
  return 0;
}
