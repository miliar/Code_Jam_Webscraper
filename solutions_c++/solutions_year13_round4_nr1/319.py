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


LL mod = 1000002013;
LL N;

LL cost(LL nb) {
  LL ret = (nb*N) % mod;
  ret = (ret + mod - ((nb*(nb-1))/2) % mod) % mod;
  return ret;
}


int main() {
  cout.precision(16);
  int T;
  cin >> T;
  for(int a = 1; a <= T; a++) {
    int M;
    cin >> N >> M;
    vector<LL> O(M), E(M), P(M);
    for(int i = 0; i < M; i++) cin >> O[i] >> E[i] >> P[i];

    map<LL, LL> T;
    LL normal_price = 0;
    for(int i = 0; i < M; i++) {
      T[O[i]] += P[i];
      T[E[i]] -= P[i];
      normal_price = (normal_price + P[i] * cost(E[i] - O[i]))%mod;
    }

    LL price = 0;
    vector<pair<LL, LL> > ticket;
    for(auto it : T) {


      if(it.second >= 0) ticket.push_back(make_pair(it.first, it.second));
      else {
        LL nb = -it.second;
        while(nb > 0) {
          auto &last = ticket.back();
          if(last.second > nb) {
            last.second -= nb;
            price = (price + nb*cost(it.first - last.first)) % mod;
            nb = 0;
          }
          else {
            nb -= last.second;
            price = (price + last.second*cost(it.first - last.first)) % mod;
            ticket.pop_back();
          }
        }
      }

  //    cerr << it.first << " " << ticket.back().first << " " << price << endl;

    }

    LL loss = (mod + normal_price - price) % mod;
    cout << "Case #" << a << ": " << loss << endl;
  }
}
