#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;

#include <cstring>

#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()


#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751



double M[1 << 20];
int N;


int next_free(int m, int pos) {
 // cerr << m << " " << pos << " " << N << endl;
  int r = 0;
  for(; m & (1 << ((pos + r)%N)); r++);
  return r;
//  cerr << r << endl;;
}

double sol(int m) {
//  cerr << m << endl;
  if(m == (1 << N) - 1) return 0;
  if(M[m] > 0) return M[m];

  double r = 0;
  for(int pos = 0; pos < N; pos++) {
    int n = next_free(m, pos);
    r += N - n + sol(m | 1 << ((pos + n)%N));
  }
  r /= double(N);
  M[m] = r;
  return r;
}

double solve(string G) {
  int m = 0;
  N = G.length();
  for(int i = G.length() -1; i >= 0; i--) {
    m <<= 1;
    if(G[i] == 'X') m |= 1;
  }

  return sol(m);
}


int main() {
  cout.precision(16);
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    memset(M, 0, sizeof(M));
    string G;
    cin >> G;


    cout << "Case #" << i << ": " << solve(G) << endl;

  }
}
