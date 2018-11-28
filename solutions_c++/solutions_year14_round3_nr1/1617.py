#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>

using namespace std;

#define FOR(k,a,b) for(typeof(a) k=(a); k < (b); k++)
#define FORE(k,a,b) for(typeof(a) k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define SZ(x) ((int)((x).size()))
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define EXIST(s,e) ((s).find(e)!=(s).end())

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1e+9;
const double EPS = 1e-10;
const double PI = acos(-1.0);



int main()
{
  int T; cin >> T;
  REP(tcase, T) {
    printf("Case #%d: ", tcase + 1);
    
    long p, q;
    cin >> p; cin.ignore(); cin >> q;
    
    for(long i = 2; i <= sqrt(max(p, q)); i++) {
      while(p % i == 0 && q % i == 0) {
        p /= i;
        q /= i;
      }
    }
    //dump(p); dump(q);

    if(p > q || q > (1LL << 40) || q & (q-1)) {
      printf("impossible\n");
      continue;
    }
    else {
      int c = 1;
      while(true) {
        if(p >= q / 2) {
          break;
        }
        else {
          q /= 2;
        }
        c++;
      }
      printf("%d\n", c);
    }
  }
  
  return 0;
}
