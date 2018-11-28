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

long long n, A, m;

int main (int argc, char *argv[]) {

  long long i, j, k, t, tt, total;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> n;

  fi(n) {
    total = 0;
    cin >> A >> m;

    long long motes[m];

    fj(m)  {
      cin >> motes[j];
    }

    sort(motes, motes+m);

    fj(m)  {
      if (motes[j] < A)
        {
          A += motes[j];
          continue;
        }

      if (motes[j] < (2*A)-1)
        {
          ++total;
          A = 2 * A - 1 + motes[j];
          continue;
        }

      if (A <= 1)
        {
          total += m - j;
          break;
        }

      long long A_t = A;
      tt = 0;
      while (A_t <= motes[j]) {
        ++tt;
        A_t += A_t -1;
      }

      if (tt < (m-j)) {
          total += tt;
          A = A_t + motes[j];
      }
      else
        {
          total += m - j;
          break;
        }

    }

    cout << "Case #" << i+1 << ": " << total << endl;
  }

  return 0;
}
