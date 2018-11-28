#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define pb push_back
#define MP make_pair
#define For(a,b,c) for(typeof(b)a=(b); a<(c); ++a)
#define ALL(a) (a).begin(),(a).end()
#define DBG(a) cout << #a << ": " << a << endl
#define FORE(i, v) for(typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

template <typename S, typename T>
S convert(const T& x) {
	S ret;
	stringstream s;
	s << x; s >> ret;
	return ret;
}

int main()
{
  int T; cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    ll P, N; cin >> N >> P;
    
    ll low = 0, high = (1LL<<N)-1;
    while (low < high) {
      ll mid = (low + high + 1) / 2;
      // what is the worst place i can get
      ll better = mid, worse = (1LL<<N) - mid - 1;
      ll place = 0;
      for (int round = 0; round < N; round++) {
        // worst case: i play against someone better, I lose.
        // the better players knock some of each other down, so i still have to play them
        if (better == 0) {
        } else {
          place += (1LL<<(N-1-round));
          better = (better-1) / 2;
        }
      }
      if (place >= P) {
        high = mid-1;
      } else {
        low = mid;
      }
    }
    ll a = low;
    
    low = 0, high = (1LL<<N)-1;
    while (low < high) {
      ll mid = (low + high + 1) / 2;
      ll better = mid, worse = (1LL<<N) - mid - 1;
      ll place = 0;
      for (int round = 0; round < N; round++) {
        // in the best case, you play someone worse than you
        // but this consumes 2^round people worse than you
        if (worse == 0) {
          place += (1LL<<(N-1-round));
        } else {
          worse = (worse-1) / 2;
        }
      }
      if (place < P) {
        low = mid;
      } else {
        high = mid-1;
      }
    }
    ll b = low;
    
    printf("Case #%d: %lld %lld\n", tt, a, b);
  }
}