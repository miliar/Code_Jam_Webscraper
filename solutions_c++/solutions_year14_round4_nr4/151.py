#include <algorithm>
#include <array>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <forward_list>
#include <functional>
#include <initializer_list>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <regex>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;

#define FORI(i,n) for(int i=0; i<(int)(n); ++i)
#define FORIB(i,b,n) for(int i=(int)(b); i<(int)(n); ++i)
#define FORIR(i,n) for(int i=(int)((n)-1); i>=0; --i)
#define FORIBR(i,b,n) for(int i=(int)((n)-1); i>=(int)(b); --i)
#define MP(a,b) make_pair(a,b)
#define MT(a...) make_tuple(a)
#define ALL(L) (L).begin(),(L).end()
#define ALLR(L) (L).rbegin(),(L).rend()
#define SZ(L) (L).size()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SORTED_PAIR(a,b) MIN(a,b),MAX(a,b)
#define INF (1<<29)
#define EPS (1e-9)

typedef unsigned int uint;
typedef unsigned long long ull;
typedef signed long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef pair<int,int> pii;
typedef vector<pii> vii;

bool getNext(vi& a, int N) {
  for(uint i = 0; i < a.size(); ++i) {
    a[i]++;
    a[i] %= N;
    if(a[i] != 0) return true;
  }
  return false;
}

int cnt(vi& a, vector<string>& S, int N) {
  int r = 0;
  for(int i = 0; i < N; ++i) {
    set<string> pre;
    for(uint j = 0; j < S.size(); ++j) {
      if(a[j] != i) continue;
      for(uint k = 0; k <= S[j].size(); ++k) {
        pre.insert(S[j].substr(0, k));
      }
    }
    r += pre.size();
  }
  return r;
}

void calc(int T) {
  int N, M;
  cin >> M >> N;
  vector<string> S(M);
  FORI(i, M) {
    cin >> S[i];
  }

  vi a(M, 0);
  int mx = 0, mxc = 0;
  do {
    int x = cnt(a, S, N);
    if(x > mx) {
      mx = x;
      mxc = 1;
    } else if(x == mx) {
      ++mxc;
    }
  } while(getNext(a, N));
  printf("Case #%d: %d %d\n", T + 1, mx, mxc);
}

int main() {
  int T;
  cin >> T;
  FORI(t, T) calc(t);
}
