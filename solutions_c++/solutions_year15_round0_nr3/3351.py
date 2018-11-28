#define DBG 0

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <iterator>
#include <utility>
#include <string.h>
using namespace std;

typedef vector<int>          vint;
typedef vector<unsigned int> vuint;
typedef vector<string>       vstr;
typedef long long            ll;
typedef unsigned long long   ull;
typedef pair<int, int>       pii;

#define FORN(i,n) for (unsigned long long (i) = 0; (i) < (n); (i)++)
#define FE  (i,x) for (typeof((x).begin()) (i) = (x).begin(); (i) != (x).end(); (i)++)

#define PB push_back
#define MP make_pair
#define A  first
#define B  second

#if DBG
#define db(x) { cout << __FUNCTION__ << "(" << __LINE__ << "): " << #x << " = " << x << endl; }
#define dbgp(...) fprintf(stderr, __VA_ARGS__);
#define dmp(table,n) { for (int __i = 0; __i < n; __i++) cerr << (__i==0 ? "" : ",") << table[__i]; cout << endl;}
ostream& operator<<(ostream& os, const vector<int> keys) {
  vector<int>::size_type sz = keys.size();
  for (unsigned int i = 0; i < sz; i++)
    os << keys[i] << " ";
  os << endl;
  return os;
}
void disp_table(int table[101][101], int N, int M) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++)
      dbgp("%d ", table[i][j]);
    dbgp("\n");
  }
  dbgp("\n");
}
#else
#define db(x)
#define dbgp(...)
#define dmp(t,n)
#define disp_table(t,n,m)
#endif

unsigned char ijk[10001];
string        ijk_line;
unsigned long long L, X;
unsigned long long S;

char mtab[5][5] = {
  0,  0,  0,  0,  0,
  0,  1,  2,  3,  4,
  0,  2, -1,  4, -3,
  0,  3, -4, -1,  2,
  0,  4,  3, -2, -1,
};

char reduce(unsigned long long start, unsigned long long end) {
  char result = 1;
  char sign   = 1;
  char in;
  unsigned long long i, n, i_end, n_end, i_lim;
  n = start / L;
  i = start % L;
  n_end = end / L;
  i_end = end % L;
  i_lim = L - 1;
  dbgp(">>>> i=%llu n=%llu i_end=%llu n_end=%llu\n",i,n,i_end,n_end);

  for ( ; n <= n_end; n++) {
    if (n == n_end)
      i_lim = i_end;

    for ( ; i <= i_lim; i++) {
      in = ijk[i];
      if (in == 0 || in > 4) {
        dbgp("ACCESS ERROR start=%llu end=%llu i=%llu n=%llu\n", start, end, i, n);
        exit(-1);
      }
      dbgp(">>>> i=%llu n=%llu in=%d sign=%d pre=%d ",i,n,in,sign,result);
      result = mtab[result][in];
      dbgp("post=%d\n",result);
      if (result < 0) {
        sign   *= -1;
        result *= -1;
      }
    }
    i = 0;
  }

  dbgp(">> reduce (%llu,%llu) = %d\n", start, end, sign*result);
  return (sign * result);
}

unsigned long long find_i(int *found) {
  char result = 1;
  char sign   = 1;
  char in;
  unsigned long long i, n;
  n = 0;
  i = 0;

  for ( ; n < X; n++) {
    for ( ; i < L; i++) {
      in = ijk[i];
      if (in == 0 || in > 4) {
        dbgp("ACCESS ERROR find_i i=%llu n=%llu\n", i, n);
        exit(-1);
      }
      result = mtab[result][in];
      if (result < 0) {
        sign   *= -1;
        result *= -1;
      }
      dbgp(">>>> i=%llu n=%llu in=%d sign*res=%d\n",i,n,in,sign*result);
      if (sign * result == 2) { // found i !
        *found = 1;
        return i+L*n;
      }
    }
    i = 0;
  }
  *found = 0;
  return 0;
}


unsigned long long find_k(unsigned long long start_k, int *found) {
  char result = 1;
  char sign   = 1;
  char in;
  long long i, n;
  long long i_min, n_min, i_lim;
  n_min = start_k / L;
  i_min = start_k % L;
  i_lim = 0;

  for (n = X-1 ; n >= n_min; n--) {
    if (n == n_min)
      i_lim = i_min;

    for (i = L-1 ; i >= i_lim; i--) {
      in = ijk[i];
      if (in == 0 || in > 4) {
        dbgp("ACCESS ERROR find_k start_k=%llu i=%llu n=%llu\n", start_k, i, n);
        exit(-1);
      }
      result = mtab[in][result];
      if (result < 0) {
        sign   *= -1;
        result *= -1;
      }
      dbgp(">>>> i=%llu n=%llu in=%d sign*res=%d\n",i,n,in,sign*result);
      if (sign * result == 4) { // found k !
        *found = 1;
        return i+L*n;
      }
    }
  }
  *found = 0;
  return 0;
}



int main() {
  int T, num=1;

  for (cin >> T; T--;) {
    int possible = 0;
    unsigned long long found_i, found_k;
    unsigned char c;
    int found;
    cin >> L >> X;
    ijk_line.reserve(L);
    cin >> ijk_line;

    S = L * X;
    dbgp("%llu %llu %llu\n", L, X, S);

    memset(ijk,0,sizeof(ijk));
    FORN(i,L) {
      c = ijk_line[i];
      if (c == '1')
        ijk[i] = 1;
      else
        ijk[i] = 2 + c - 'i';
    }
    
    char total = reduce(0, S-1);
    if (total != -1) {
      dbgp("Rejected because reduce is not -1\n");
      goto impossible;
    }

    // Find prefix resolving to "i"
    found_i = find_i(&found);
    dbgp("found_i = %llu\n", found_i);
    // Not feasible or leaves less than 2 characters -> impossible
    if (found == 0) {
      dbgp("%llu %llu %llu\n", L, X, S);
      dbgp("Rejected because could not create i\n");
      goto impossible;
    }
    if (found_i >= S-2) {
      dbgp("%llu %llu %llu\n", L, X, S);
      dbgp("Rejected because could not create i leaving 2 characters found_i=%llu\n",found_i);
      goto impossible;
    }

    // Find suffix resolving to "k"
    found_k = find_k(found_i+2, &found);
    dbgp("found_k = %llu\n", found_k);
    if (found == 0) {
      dbgp("%llu %llu %llu\n", L, X, S);
      dbgp("Rejected because could not create k found_i=%llu\n",found_i);
      goto impossible;
    }

    // Because i.x.k = R = -1
    // x = i^-1.R.k^-1 = j
    // so we're done
#if DBG
    total = reduce(found_i+1,found_k-1);
    printf("%llu %llu %llu\n", L, X, S);
    cout << ijk_line << endl;
    printf("Mid = %d\n",total);
    if (total != 3) printf("WTF!!\n");
#endif

    possible = 1;

impossible:
    printf("Case #%d: %s\n", num++, possible ? "YES" : "NO");
  }
}

