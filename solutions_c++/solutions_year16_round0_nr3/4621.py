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

#define _DEBUG
#define EPS 1e-9
#define INF 0x3FFFFFFF
#define INFLL 0x3FFFFFFFFFFFFFFF
#define MAXN 333
#define MOD 1000000007

string i2bs (unsigned long long n, long b = 32, bool zeros = false) {
  string res = "00000000000000000000000000000000";
  int c = b; --b;
  while (n) {res[b] += (n&1); --b; n >>= 1;}
  if (!zeros) return res.substr(b+1,c-b-1);
  return res.substr(0,c);
}

int T, N, J;
Int B[11]; // decimal value of jamcoin in i-th base

bool isPrime(Int n) {
  if (n == 1) return false;
  if (n == 2) return true;
  if (n % 2 == 0) return false;

  for (Int i = 3L; i*i <= n; i += 2L) {
    if (n % i == 0) {
      return false;
    }
  }

  return true;
}

Int minDivisor(Int N){
  for (Int i = 2; i*i <= N; ++i) {
    if (N%i == 0) {
      return i;
    }
  }
  return 1;
}

Int x2dec(Int x, int base) {
  Int bb = 1, res = 0;
  while (x > 0) {
    res += (x&1) * bb;
    bb *= base;
    x >>= 1;
  }
  return res;
}

void solve() {
  Int at = (1 << (N-1)) + 1;
  
  Int stop = 1 << N;
  while (J > 0 && at < stop) {
    bool isJamCoin = true;
    for (int b = 2; b <= 10; b++) {
      B[b] = x2dec(at, b);
      if (isPrime(B[b])) {
        isJamCoin = false; break;
      }
    }
    if (isJamCoin) {
      cout << i2bs(at) << " ";
      for (int b = 2; b <= 10; b++) {
        cout << minDivisor(B[b]) << " ";
      }
      cout << endl;
      --J;
    }
    at += 2;
  }

}

void readInput() {
  cin >> N >> J;
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
    cout << "Case #" << tc << ": " << endl;
    solve();
    cerr << " [INFO] Case #" << tc << ": done in " << ms2time(clock() - caseTime) << endl;
  } 
  
  cerr << endl << " [INFO] Input done in " << ms2time(clock() - totalTime) << endl;
  return 0;
}