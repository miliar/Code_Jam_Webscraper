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


LL guar(LL N, LL P) {
  if(P == 0) return 0;
  if(P == 1LL << (N)) return 1LL << (N);
  if(P <= (1LL << (N-1))) return 1;
  return 2*guar(N-1, P - (1LL << (N-1)))  + 1;
}



int main() {

  LL T, N, P;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> N >> P;


    cout << "Case #" << i << ": " << guar(N, P) - 1 << " " << ((1LL << N) - 1 - guar(N, ((1LL << N) - P))) << endl;
  }
}




