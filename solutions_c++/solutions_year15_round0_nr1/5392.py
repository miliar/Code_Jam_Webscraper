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

int main() {
  int T;
  cin >> T;

  for ( int t = 0; t < T; ++t ) {
    int SMax;
    cin >> SMax;

    string D;
    cin >> D;

    int add = 0;
    int sum = 0;
    for ( int d = 0; d <= SMax; ++d ) {
      if ( d > sum ) {
	add += ( d - sum );
	sum += ( d - sum );
      }
      sum += ( D[ d ] - '0' );
    }

    cout << "Case #" << t + 1 << ": " << add << endl;
  }
}
