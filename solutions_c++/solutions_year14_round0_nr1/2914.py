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

void solve(int tc) {
  set<int> s;
  int t, r; cin >> r;
  FORI(i,4)FORI(j,4){
    cin >> t;
    if(i + 1 == r) s.insert(t);
  }
  cin >> r;
  FORI(i,4)FORI(j,4){
    cin >> t;
    if(i + 1  != r) s.erase(t);
  }
  cout << "Case #" << tc + 1 << ": ";
  if(s.size() == 1) {
    cout << *s.begin() << endl;
  } else if(s.size() == 0) {
    cout << "Volunteer cheated!" << endl;
  } else {
    cout << "Bad magician!" << endl;
  }
}

int main() {
  int T;
  cin >> T;
  FORI(t,T){
    solve(t);
  }
}
