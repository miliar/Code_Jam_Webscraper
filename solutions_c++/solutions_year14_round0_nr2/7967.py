#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <deque>
#include <map>
#include <set>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <queue>

#define FOR(a,b,c) for(long long a = (b); a < (c); a++)
#define FORE(a,b,c) for(long long a = (b); a <= (c); a++)
#define FORD(a,b,c) for(long long a = (b); a > (c); a--)
#define REP(a,b) FOR(a,0,b)
#define REPE(a,b) FORE(a,1,b)
#define SZ(c) ((int) c.size())
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<string> vs;

const double eps = 1e-7;
const double pi = 2*acos((double) 0);

int main() {
  int nt;
  double nc, nf, nx, ans, prod;

  cin >> nt;
  REP(t, nt) { 
    cin >> nc >> nf >> nx;
    if(nc > nx) {
      ans = nx/2;
    } else {
      prod = 2;
      ans = 0;

      do {
        ans += nc / prod;
        prod += nf;
      } while((nx-nc)/(prod-nf) > (nx) / (prod));

      ans += (nx-nc) / (prod-nf);
    }

    printf("Case #%lld: %.7lf\n", t+1, ans);
  }

  return 0;
}










