#include <algorithm>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define FR first
#define SC second

#define debug(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
}

const ll LINF = 1000000000000000000LL;
const int INF = 1000000000;
const ll MOD = 1000002013;

ll N;

ll sum(ll n) {
  return n*(n+1)/2;
}

ll journey_cost(ll d) {
  return sum(N)-sum(N-d);
}

ll total_cost(const vector<int>& rid, const vector<vector<ll> >& jo) {
  ll c = 0;
  for (int i = 0; i < int(jo.size()); ++i) {
    for (int j = i+1; j < int(jo[i].size()); ++j) if (jo[i][j] > 0) {
      ll jc = journey_cost(rid[j]-rid[i])%MOD;
      c += (jc*jo[i][j])%MOD;
      c %= MOD;
    }
  }
  return c;
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    int m;
    cin >> N >> m;
    vector<pair<PII, ll> > journeys(m);
    vector<int> rid;
    for (int i = 0; i < m; ++i) {
      cin >> journeys[i].FR.FR >> journeys[i].FR.SC >> journeys[i].SC;
      rid.push_back(journeys[i].FR.FR);
      rid.push_back(journeys[i].FR.SC);
    }
    
    sort(rid.begin(), rid.end());
    rid.resize(unique(rid.begin(), rid.end())-rid.begin());
    int n = int(rid.size());
    map<int, int> id;
    for (int i = 0; i < n; ++i) {
      id[rid[i]] = i;
    }
    
    vector<vector<ll> > jo(n, vector<ll>(n, 0));
    vector<PII> p;
    for (int i = 0; i < m; ++i) {
      int a = id[journeys[i].FR.FR];
      int b = id[journeys[i].FR.SC];
      jo[a][b] += journeys[i].SC;
      p.push_back(PII(a, b));
    }
    ll c0 = total_cost(rid, jo);
    sort(p.begin(), p.end());
    
    bool done = false;
    for (; !done;) {
      done = true;
      set<PII> s;
      for (int i = 0; i < int(p.size()); ++i) {
        int a = p[i].FR;
        int b = p[i].SC;
        set<PII>::iterator it = s.lower_bound(PII(a, -INF));
        vector<PII> to_remove;
        for (; it != s.end() && it->first < b && jo[a][b] > 0; ++it) {
          int y = it->first;
          int x = it->second;
          if (jo[x][y] == 0) {
            to_remove.push_back(*it);
            continue;
          }
          if (x >= a) {
            continue;
          }
          
          // swap cards
          int k = min(jo[a][b], jo[x][y]);
          done = false;
          jo[a][b] -= k;
          jo[x][y] -= k;
          jo[a][y] += k;
          jo[x][b] += k;
        }
        
        // remove empty pairs
        for (int j = 0; j < int(to_remove.size()); ++j) {
          if (jo[to_remove[j].SC][to_remove[j].FR] == 0) {
            s.erase(to_remove[j]);
          }
        }
        
        // insert current pair
        s.insert(PII(b, a));
      }
      
      vector<PII> np;
      for (int j = 0; j < n; ++j) {
        for (int k = j+1; k < n; ++k) if (jo[j][k] > 0) {
          np.push_back(PII(j, k));
        }
      }
      swap(p, np);
    }
    ll c1 = total_cost(rid, jo);
    cout << "Case #" << ca << ": " << (c0-c1+MOD)%MOD << endl;
  }
}

