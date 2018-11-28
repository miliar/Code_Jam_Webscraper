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

int n, m;

bool isPal(string s) {
  string rev = s;
  reverse(all(rev));
  if (rev == s) {
    return true;
  } else {
    return false;
  }
}

int main (int argc, char *argv[]) {

  int i, j, k, t, tt;
  unsigned long long int start, end;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> n;

  fi(n) {
    unsigned int total = 0;
    cin >> start >> end;

    string sroot, ssquare;
    unsigned long long int startroot = ceil(sqrt(start));
    unsigned long long int endroot = floor(sqrt(end));

    for (j = startroot; j <= endroot; ++j)
      {
        stringstream ss;
        ss << j << " " << j*j;
        ss >> sroot;
        ss >> ssquare;

        if (isPal(sroot) && isPal(ssquare))
          {
            ++total;
          }
      }

    cout << "Case #" << i+1 << ": ";

    cout << total << endl;
  }
  return 0;
}
