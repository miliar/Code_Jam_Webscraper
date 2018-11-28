#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof__(V.begin()) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

vector<LL> dobre;

inline bool jestPalindrom(LL x) { 
    vector<char> reszta;
    while(x) {
      reszta.PB(x%10);
      x /= 10;
    }
    int latacz = 0;
    bool ok = true;
    while (latacz < reszta.size()) {
      if (reszta[latacz] != reszta[ reszta.size()-1-latacz ]) {
	ok = false;
	break;
      }
      ++latacz;
    }
    if (ok) return true;
    return false;
}

void preprocess() {
  FOR(i,1,10000001) {
    LL sq = (LL)i*1LL*i;
    if (jestPalindrom(sq) && jestPalindrom((LL)i))
      dobre.PB((LL)i*1LL*i);
  }
}

void testcase() {
  LL a, b;
  scanf("%lld%lld", &a, &b);
  int ile = upper_bound(dobre.begin(), dobre.end(), b) - lower_bound(dobre.begin(), dobre.end(), a);
  printf("%d\n", ile);
}

int main() {
  preprocess();
  int t;
  scanf("%d", &t);
  FOR(i,1,t) {
    printf("Case #%d: ", i);
    testcase();
  }
}
