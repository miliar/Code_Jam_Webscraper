#include <iostream>
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <complex>
#include <iterator>
#include <memory>
#include <utility>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) make_pair((a), (b))
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;

ll gcd(ll a, ll b) {
  return a == 0 ? b : gcd(b % a, a);
}

bool is_ok( int m, const vector<int>& Ps ) {
  int special = 0;
  int max_eat = 0;
  for ( int i = 0; i < Ps.size(); ++i ) {
    int p = Ps[ i ];
    if ( p >= m ) {
      int div = int( ceil( double( p ) / m ) );
      special += ( div - 1 );
      int eat = int( ceil( double( p ) / div ) );
      max_eat = ( eat > max_eat ) ? eat : max_eat;
    }
  }
  int minutes = special + max_eat;
  return minutes <= m;
}

int min_minutes = 0;

void DFS( const vector<int>& Ps, vector<int>& Ds ) {
  if ( Ds.size() == Ps.size() ) {
    int max_eat = 0;
    int special = 0;
    for ( int i = 0; i < Ps.size(); ++i ) {
      int p = Ps[ i ];
      int d = Ds[ i ];
      special += d - 1;
      int eat = int( ceil( double( p ) / d ) );
      max_eat = ( eat > max_eat ) ? eat : max_eat;
    }

    int minutes = special + max_eat;
    min_minutes = ( minutes < min_minutes ) ? minutes : min_minutes;
    return;
  }

  int i = Ds.size();
  for ( int d = 1; d <= Ps[ i ]; ++d ) {
    Ds.push_back( d );
    DFS( Ps, Ds );
    Ds.pop_back();
  }
}

int main() {
  int T;
  cin >> T;

  for ( int t = 0; t < T; ++t ) {
    int D;
    cin >> D;

    vector<int> Ps;
    for ( int d = 0; d < D; ++d ) {
      int p;
      cin >> p;
      Ps.push_back( p );
    }

    vector<int> Ds;
    min_minutes = 10000;
    DFS( Ps, Ds );

    cout << "Case #" << t + 1 << ": " << min_minutes << endl;
  }
}
