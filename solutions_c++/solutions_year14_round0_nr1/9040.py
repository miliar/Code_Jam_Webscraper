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
    int i; cin >> i;
    set<int> nums;
    
    REP(k, 4) {
      if(k + 1 == i) {
        REP(l, 4) {
          int t; cin >> t;
          nums.insert(t);
        }
      }
      else REP(l, 4) { int t; cin >> t; }
    }
    
    int j; cin >> j;
    int hit = -1;
    REP(k, 4) {
      if(k + 1 == j) {
        REP(l, 4) {
          int t; cin >> t;
          if(EXIST(nums, t)) {
            if(hit == -1) {
              hit = t;
            }
            else {
              hit = -2;
            }
          }
        }
      }
      else REP(l, 4) { int t; cin >> t; }
    }

  END:
    printf("Case #%d: ", tcase + 1);
    if(hit > 0) printf("%d\n", hit);
    else if(hit == -1) printf("Volunteer cheated!\n");
    else if(hit == -2) printf("Bad magician!\n");
  }
  
  return 0;
}
