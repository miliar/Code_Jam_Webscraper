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

int T, N;
string S;
int D[50];
int C[10];

bool has(char c, int x) {
	return (D[c - 'A'] >= x);
}

int solve() {
  int result = INF;

  #ifdef DEBUG
    REP(i,26) {
      cout << (char)(i + 'A') << ": " << D[i] << endl;
    }
  #endif

  // "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"

  while (has('S',1) && has('I',1) && has('X',1)) {
	  D['S'-'A'] -= 1; D['I'-'A'] -= 1;  D['X'-'A'] -= 1;
	  C[6] += 1;
  }  
  while (has('Z',1) && has('E',1) && has('R',1) && has('O',1)) {
	  D['Z'-'A'] -= 1; D['E'-'A'] -= 1;  D['R'-'A'] -= 1; D['O'-'A'] -= 1;
	  C[0] += 1;
  }  
  while (has('E',1) && has('I',1) && has('G',1) && has('H',1) && has('T',1)) {
	  D['E'-'A'] -= 1; D['I'-'A'] -= 1;  D['G'-'A'] -= 1; D['H'-'A'] -= 1; D['T'-'A'] -= 1;
	  C[8] += 1;
  }   
  while (has('F',1) && has('O',1) && has('U',1) && has('R',1)) {
	  D['F'-'A'] -= 1; D['O'-'A'] -= 1;  D['U'-'A'] -= 1; D['R'-'A'] -= 1;
	  C[4] += 1;
  }   
  while (has('S',1) && has('E',2) && has('V',1) && has('N',1)) {
	  D['S'-'A'] -= 1; D['E'-'A'] -= 2;  D['V'-'A'] -= 1; D['N'-'A'] -= 1;
	  C[7] += 1;
  }  
  while (has('T',1) && has('W',1) && has('O',1)) {
	  D['T'-'A'] -= 1; D['W'-'A'] -= 1;  D['O'-'A'] -= 1;
	  C[2] += 1;
  }  
  while (has('O',1) && has('N',1) && has('E',1)) {
	  D['O'-'A'] -= 1; D['N'-'A'] -= 1;  D['E'-'A'] -= 1;
	  C[1] += 1;
  }
  while (has('T',1) && has('H',1) && has('R',1) && has('E',2)) {
	  D['T'-'A'] -= 1; D['H'-'A'] -= 1;  D['R'-'A'] -= 1; D['E'-'A'] -= 2;
	  C[3] += 1;
  }
  while (has('F',1) && has('I',1) && has('V',1) && has('E',1)) {
	  D['F'-'A'] -= 1; D['I'-'A'] -= 1;  D['V'-'A'] -= 1; D['E'-'A'] -= 1;
	  C[5] += 1;
  }      
  while (has('N',2) && has('I',1) && has('E',1)) {
	  D['N'-'A'] -= 2; D['I'-'A'] -= 1;  D['E'-'A'] -= 1;
	  C[9] += 1;
  }  
  
  REP(i,10) {
    REP(j,C[i]) cout << i;
  }  
  
  return result;
}

void readInput() {
  cin >> S;
  N = SZ(S);
  REP(i,10) { C[i] = 0; }
  REP(i,50) { D[i] = 0; }
  REP(i,N) {
    D[S[i] - 'A'] += 1;
  }
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
  int tc = 0;
  for (int tc = 1; tc <= T; ++tc) {
    clock_t caseTime = clock();
    readInput();
    cout << "Case #" << tc << ": ";
	solve();
	cout << endl;
    cerr << " [INFO] Case #" << tc << ": done in " << ms2time(clock() - caseTime) << endl;
  } 
  
  cerr << endl << " [INFO] Input done in " << ms2time(clock() - totalTime) << endl;
  return 0;
}