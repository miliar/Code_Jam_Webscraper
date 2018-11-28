#include <cstdio>
#include <sstream>
#include <iostream>
#include <memory>
#include <cassert>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
#define PI 3.14159

int n, m;

int main (int argc, char *argv[]) {

  int i, j, k, total;
  long long r, t, tt;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> n;

  fi(n) {
    total = 0;
    cin >> r >> t;

    while(t > 0) {
      tt = ((r+1)*(r+1) - (r * r));
      if (tt <= t)
        {
          ++total;
        }
      t -= tt;
      r += 2;
    }

    cout << "Case #" << i+1 << ": " << total << endl;
  }

  return 0;
}
