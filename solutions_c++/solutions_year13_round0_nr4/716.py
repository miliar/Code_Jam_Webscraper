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
int have[222];
int type[22];
vector<int> keys[22];
bool seen[1<<22];
int next[1<<22];
bool GREAT = false;
    int K, N;
bool doit(int mask) {
  if (seen[mask]) return false;
  seen[mask] = true;
  if (!mask) {
    GREAT = true;
    return true;
  }
  int have2[222];
  memcpy(have2, have, sizeof(have));
  for (int i = 0; i < N; ++i) {
    if (mask & (1<<i)) continue;
    for (int j = 0; j < keys[i].size(); ++j)
      have2[keys[i][j]]++;
    have2[type[i]]--;
  }

  for (int i = 0; i < N; ++i) {
    if (!(mask&(1<<i))) continue;
    if (!have2[type[i]]) continue;
    next[mask] = i;
    if (doit(mask ^ (1<<i))) {
//      cout << mask << "  " << next[mask] << endl;
      return true; 
    }
  }
  return false;
}

int main() {
  int i,j , k;
  int casos; cin >> casos;
  for (int h = 0; h < casos; ++h) {
    cin >> K >> N;
    GREAT = false;
    memset(seen, false, sizeof(seen));
    memset(have, 0, sizeof(have));
    REP(ii, K) { cin >> k; have[k]++; }
    REP(ii, N) {
      keys[ii].clear();
      cin >> type[ii] >> k;
      REP(jj, k) { cin >> i; keys[ii].PB(i); }
    }
    doit((1<<N)-1);
    cout << "Case #" << h+1 << ":";
    if (!GREAT) {
      cout << " IMPOSSIBLE";
    } else {
      vector<int> res;
      int mask = (1<<N)-1;
      REP(ii, N) {
        res.PB(next[mask]);
        mask ^= (1<<next[mask]);
      }
      REP(ii, res.size())
        cout << " " << res[ii] + 1;
    }
    cout << endl;
  }return 0;
}
