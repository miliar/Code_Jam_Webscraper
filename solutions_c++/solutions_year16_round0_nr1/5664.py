#ifndef INCLUDES

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
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

#endif

#ifndef MACROS

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define NL '\n'
#define SZ(c) ((int)(c).size())
#define CLR(c,v) memset(c, v, sizeof(c))
#define REP(i,e) for(int i = 0; i < (signed)(e); ++i)
#define REPD(i,e) for(int i = e-1; i >= 0; --i)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(__typeof(b) i = (b); i != (e); ++i)
#define FORD(i,b,e) for(__typeof(b) i = (b); i != (e); --i)
#define FORC(i,c) FORU(i,c.begin(),c.end())
#define MAPI(m,e,v) if(m.find(e)!=m.end()){m[e]+=v;}else{m.insert(make_pair(e,v));}
#define SQR(x) ((x)*(x))
typedef vector<int> vi; 
typedef long long Int;
typedef long double LD;
typedef pair<int,int> pii;

#endif

#ifndef TOOLS

template<class T> ostream& operator << (ostream& os, vector<T> vec) {
	for(int i=0; i<vec.size(); ++i) {
		os << vec[i] << " ";
	}
	return os;
}

template <class T> T s2t(string s) {istringstream i(s); T x; i>>x; return x;}
template <class T> string t2s(T x) {ostringstream o; o << x; return o.str();}

vector<string> split (string s, string del = " ") { vector<string> res;
  int ss = s.size(), sdel = del.size();
  for (int p = 0, q; p < ss; p = q+sdel) {
    if ((q = s.find(del, p)) == (signed)string::npos) q = ss;
    if (q-p>0) res.push_back(s.substr(p,q-p));
  } return res;
}

vector<int> splitInts (string s, string del = " ") { vector<int> res;
  vector<string> t = split(s,del);
  for (int i = 0; i < (signed)t.size(); ++i) {
    if (t[i].size() > 10 || (t[i].size()==10 && t[i][0]>='2')) {
      res.push_back(2000000000);
    } else { res.push_back(atoi(t[i].c_str())); }
  } return res;
}

#endif

#define _DEBUG
#define EPS 1e-9
#define INF 0x3FFFFFFF
#define INFLL 0x3FFFFFFFFFFFFFFF
#define MAXN 333
#define MOD 1000000007

int T;
Int N;
bool D[10];

void digits(Int x) {
  while (x > 0) {
    D[x % 10] = true;
    x /= 10;    
  }
}

Int solve() {
  Int at = N;
  REP(i,10) { D[i] = false; }
  
  while (true) {
    bool allseen = true;
    digits(at);
    REP(i,10) { allseen &= D[i]; }
    if (allseen) { break; }
    at += N;
  }
  
  return at;
}

void readInput() {
  cin >> N;
}

string ms2time(clock_t t) {
  char s[12]; int seconds = (t / CLOCKS_PER_SEC);
  sprintf(s, "%02d:%02d:%02d.%03d", seconds / 3600, (seconds % 3600) / 60, seconds % 60, t - (seconds * CLOCKS_PER_SEC));
  return string(s);
}

int main(int argc, char *argv[]) {
  ios_base::sync_with_stdio(false);
  ios_base::fmtflags ff = cout.flags();
  ff |= cout.fixed;
  cout.flags(ff);
  cerr.precision(9);
  cout.precision(9);
  clock_t totalTime = clock();

  cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
    clock_t caseTime = clock();
    readInput();
    if (N != 0) {
      cout << "Case #" << tc << ": " << solve() << endl;
    } else {
      cout << "Case #" << tc << ": INSOMNIA" << endl;
    }
    cerr << " [INFO] Case #" << tc << ": done in " << ms2time(clock() - caseTime) << endl;
  } 
  
  cerr << endl << " [INFO] Input done in " << ms2time(clock() - totalTime) << endl;
  return 0;
}