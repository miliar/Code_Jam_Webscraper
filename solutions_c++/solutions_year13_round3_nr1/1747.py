#define nPROFILE

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
using namespace std;

#ifdef PROFILE
#include <windows.h>
#define START_PROF   {LARGE_INTEGER t0, t1; ::QueryPerformanceCounter(&t0);}
#define STOP_PROF(a) {::QueryPerformanceCounter(&t1); (a) += (t1.QuadPart - t0.QuadPart);}
#endif

typedef vector<int>          vint;
typedef vector<unsigned int> vuint;
typedef vector<string>       vstr;
typedef long long            ll;
typedef unsigned long long   ull;
typedef unsigned char        uc;
typedef pair<int, int>       pii;

#define FORN(i,n) for (int (i) = 0; (i) < (n); (i)++)
#define FE  (i,x) for (typeof((x).begin()) (i) = (x).begin(); (i) != (x).end(); (i)++)

#define PB push_back
#define MP make_pair
#define A  first
#define B  second

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
      printf("%d ", table[i][j]);
    printf("\n");
  }
  printf("\n");
}

#define MAXSTR 100

const uc vowel[] = { 1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0 };
#define VOWEL(i) (vowel[name[i]-'a'])

uc name[MAXSTR+1];
uc good[MAXSTR][MAXSTR];
int n;

int mark_good(int start, ull len) {
  for (int i = 0; i <= start; i++) {
    for (int j = start + n - 1; j < len; j++) {
      good[i][j] = 1;
    }
  }
  return 0;
}

ull count_good(ull len) {
  ull found = 0;
  FORN(i, len)
    FORN(j, len)
      found += good[i][j];
  return found;
}

int main() {
  int T, num=1;

  #ifdef PROFILE
  LARGE_INTEGER start, end, freq;
  ::QueryPerformanceFrequency(&freq);
  ::QueryPerformanceCounter(&start);
  #endif

  for (cin >> T; T--;) {
    unsigned long long found = 0;
    cin >> name >> n;
    ull len = strlen((char*)name);
    memset(good, 0, sizeof(good));

    FORN(i, len+1-n) {
      if (VOWEL(i)) continue;
      FORN(j, n-1)
        if (VOWEL(i+j+1)) goto next;
      // Found a series of n consonants !
      mark_good(i, len);
      //cout << i << endl;
      //FORN(j,n) cout << name[i+j];
      //cout << endl;
next:
      ;
    }

    found = count_good(len);

    printf("Case #%d: %llu\n", num++, found);
  }

  #ifdef PROFILE
  ::QueryPerformanceCounter(&end);
  cout << (end.QuadPart - start.QuadPart) / static_cast<float>(freq.QuadPart) << endl;
  //cout << t_check / static_cast<float>(freq.QuadPart) << endl;
  #endif

}
