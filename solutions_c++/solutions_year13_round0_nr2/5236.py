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
#include <cstring>

using namespace std;

typedef long long          ll;
typedef vector<int>        vi;
typedef pair<int, int>     ii;
typedef vector<ii>         vii;
typedef set<int>           si;
typedef map<string, int>   msi;

//#define for(i, a, b) \
//  for(int i = int(a); i <= int(b); i++)
//#define Rvi(c, it) \
//  for(vi::iterator it = (c).begin(); it != (c).end(); it++)
//#define Rvii(c, it) \
//  for(vii::iterator it = (c).begin(); it != (c).end(); it++)
//#define Rmsi(c, it) \
//  for(msi::iterator it = (c).begin(); it != (c).end(); it++)

int main() {
  int t, tc = 0;
  scanf("%d", &t);

  while(t--) {
    tc++;
    int n, m;
    scanf("%d %d", &n, &m);

    int A[n][m];
    int mr[n], mc[m];
    memset(mr, 0, sizeof(mr));
    memset(mc, 0, sizeof(mc));

    for(int i=0; i<n; i++) {
      for(int j=0; j<m; j++) {
	scanf("%d", &A[i][j]);
	mr[i] = max(A[i][j], mr[i]);
	mc[j] = max(A[i][j], mc[j]);
      }
    }

    bool sw = true;

    for(int i=0; i<n; i++) {
      for(int j=0; j<m; j++) {
	if(A[i][j] < mr[i] && A[i][j] < mc[j]) {
	  sw = false;
	  break;
	}
      }
    }

    if(sw)
      printf("Case #%d: YES\n", tc);
    else
      printf("Case #%d: NO\n", tc);
  }

  return 0;
}
