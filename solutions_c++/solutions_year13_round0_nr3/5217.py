/** 
 *
 * rais.fathin38
 */

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cctype>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <utility>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <bitset>

using namespace std;

#define REP(a, b) for(int a = 0; a < b; a++)
#define FOR(a, b, c) for(int a = b; a <= c; a++)
#define FOREACH(a, b) for(typeof(b.end()) a = b.begin(); a != b.end(); a++)
#define RESET(a, b) memset(a, b, sizeof a)
#define MAX(a, b) a = max(a, b)
#define MIN(a, b) a = min(a, b)

#ifdef F
#define OPEN freopen("tc", "r", stdin)
#define DEBUG(x) cout << #x << " : " << x << endl
#define TIME cout << fixed << setprecision(3) << clock() / (double)CLOCKS_PER_SEC << endl
#else
#define OPEN {}
#define DEBUG(x) {}
#define TIME {}
#endif

#define INF 0x7FFFFFFF
#define INFLL 0x7FFFFFFFFFFFFFFF

#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef long long int64;
typedef pair<int, int> pii;

template<class T> ostream& operator<<(ostream &S, const vector<T> &v) {S<<"(";REP(i,v.size()){if(i)S<<", ";S<<v[i];}S<<")";return S;}
template<class T1, class T2> ostream& operator<<(ostream &S, const pair<T1, T2> &p) {S<<"("<<p.fi<<", "<<p.se<<")";return S;}
template<class T> T abs(T num) { return num > 0 ? num : -num; }
template<class T> T sqr(T num) { return num*num; }

int a, b;
int64 ten[12];
vector<int> candidate;
vector<int64> sqrCandidate;

bool pal(int64 number) {
  stringstream ss; ss << number;
  string ln; ss >> ln;
  int len = ln.length();
  REP(i, len/2) if (ln[i] != ln[len-i-1]) return false;
  return true;
}

void generate(int number, int pos, int len) {
  if ((len & 1) && pos == len/2) {
    int tmp = number;
    FOR(i, 0, 9) {
      if (pos == 0 && i == 0) continue;
      int tmp2 = number;
      tmp2 = tmp2*10 + i;
      tmp2 = tmp2*ten[len/2] + tmp;
      if (pal(sqr((int64)tmp2))) candidate.pb(tmp2);
    }
  } else if (!(len & 1) && pos == len/2) {
    int tmp = number;
    number = number*ten[len/2] + tmp;
    if (pal(sqr((int64)number))) candidate.pb(number);
  } else {
    FOR(i, 0, 9) {
      if (pos == 0 && i == 0) continue;
      generate(number*10+i, pos+1, len);
    }
  }
}

void preCalc() {
  ten[0] = 1LL;
  FOR(i, 1, 11) ten[i] = ten[i-1]*10LL;
  FOR(i, 1, 8) generate(0, 0, i);
}

int main() {
  // freopen("tc", "r", stdin);
  // freopen("out", "w", stdout);
  preCalc();
  FOREACH(it, candidate) sqrCandidate.pb(sqr((int64)*it));
  int tc; cin >> tc;
  FOR(t, 1, tc) {
    cin >> a >> b;
    int ii = lower_bound(sqrCandidate.begin(), sqrCandidate.end(), a)-sqrCandidate.begin();
    int jj = lower_bound(sqrCandidate.begin(), sqrCandidate.end(), b)-sqrCandidate.begin();
    while (jj >= sqrCandidate.size() || sqrCandidate[jj] > b) jj--;
    printf("Case #%d: %d\n", t, max(0, jj-ii+1));
  }
  return 0;
}
