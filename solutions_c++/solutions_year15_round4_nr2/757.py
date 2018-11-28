#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en)  for(int i=(st); i<=(int)(en); i++)
#define Forn(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

// Types
typedef long double ld;
typedef signed   long long i64;
typedef signed   long long ll;
typedef unsigned long long u64;
typedef unsigned long long ull;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

//#define debug(...)
#define debug printf

int N;
ld targetVolumn, targetTemp;

struct Source {
  Source(ld r, ld t): rate(r), temp(t) {}
  ld rate;
  ld temp;

  bool operator< (const Source& s) const {
    if (temp == s.temp) return rate < s.rate;
    return temp < s.temp;
  }
};

vector<Source> source;

void prepare() {
  sort(source.begin(), source.end());
  vector<Source> result;

  if (N > 1) {
    int dest = 0;
    int src = 1;

    result.push_back(source[0]);

    while (src < N) {
      if (source[src].temp == result[dest].temp) {
        result[dest].rate += source[src].rate;
      } else {
        result.push_back(source[src]);
        dest++;
      }
      src++;
    }

    source = result;
    N = dest + 1;
  }
}

ld count() {
  prepare();

  if (N == 1) {
    if (source[0].temp != targetTemp) return -1;
    return targetVolumn / source[0].rate;
  } else if (N == 2) {
    if (source[1].temp < targetTemp || source[0].temp > targetTemp) {
      return -1;
    }

    if (source[0].temp == targetTemp) {
      return targetVolumn / source[0].rate;
    }
    if (source[1].temp == targetTemp) {
      return targetVolumn / source[1].rate;
    }

    ld diff1 = targetTemp - source[0].temp;
    ld diff2 = source[1].temp - targetTemp;

    ld volumn1 = targetVolumn * diff2 / (diff1 + diff2);
    ld volumn2 = targetVolumn * diff1 / (diff1 + diff2);

    return max(volumn1 / source[0].rate, volumn2 / source[1].rate);
  }
}

int main() {
    int caseN;
    scanf("%d", &caseN);

    for (int cc = 1; cc <= caseN; ++cc) {
        printf("Case #%d: ", cc);

        cin >> N >> targetVolumn >> targetTemp;
        source.clear();

        ld rate, temp;
        for (int i = 0; i < N; ++i) {
          cin >> rate >> temp;
          source.push_back(Source(rate, temp));
        }

        if (N > 2) {
          printf("\n");
          continue;
        }

        ld time = count();
        if (time < 0) {
          cout << "IMPOSSIBLE";
        } else {
          printf("%.9Lf", time);
        }

        printf("\n");
    }

    return 0;
}
