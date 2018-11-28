#include "stdio.h"
#include "stdlib.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define REP(i,a) for(typeof(a) i = 0; i < (a); ++i)
#define FOR(i,a,b) for(typeof(a) i = (a); i < (b); ++i)
#define SZ(x) ((int)((x).size()))
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define GET_BITS(i,j) (i >> (j)) & 1
#define min(a,b) ((a) < (b) ? (a) : (b))
#define READI(n,a) REP(i,n) scanf("%d", &a[i]);

int main()
{
#ifdef DEBUG
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-small.out","w", stdout);
#endif
  int T;
  cin >> T;
  int v[5][5], m[5][5];
  REP(i,T)
  {
    int r1,r2;
    cin >> r1;
    REP(j,4) REP(k,4) cin >> v[j][k];
    cin >> r2;
    REP(j,4) REP(k,4) cin >> m[j][k];

    int c[17] = {0};
    REP(j,4) ++c[v[r1-1][j]];

    int rep = 0;
    int res = 0;
    int saveNo;
    REP(j,4)
    if (c[m[r2-1][j]] == 1)
    {
      ++rep;
      saveNo = m[r2-1][j];
      if (rep == 2)
      {
        res = 1;
        break;
      }
    }
    if (rep == 0) res = 2;

    cout << "Case #"<<i+1<<": ";
    switch(res)
    {
      case 0:
        cout << saveNo << endl;
        break;
      case 1:
        cout << "Bad magician!" << endl;
        break;
      case 2:
        cout << "Volunteer cheated!" << endl;
        break;
    }
  }
 

  return 0;
}

