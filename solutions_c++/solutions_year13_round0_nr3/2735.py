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

bool is_palind(ll x) {
  char buf[111];
  sprintf(buf, "%lld", x);
  int i = 0, j = strlen(buf)-1;

  while(i < j) {
    if(buf[i] != buf[j]) return false;
    else { i++; j--; }
  }
  return true;
}

int main()
{
  int T;
  cin >> T;
  REP(turn, T) {
    ll A, B;
    cin >> A >> B;

    ll lb = ceil(sqrt(A));
    ll ub = floor(sqrt(B));

    ll res = 0;
    FORE(x, lb, ub) {
      if(is_palind(x)) {
        if(is_palind(x*x)) res++;
      }
    }
    
    printf("Case #%d: %lld\n", turn+1, res);
  }
  
  return 0;
}
