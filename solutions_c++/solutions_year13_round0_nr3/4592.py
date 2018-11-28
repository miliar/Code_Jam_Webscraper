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

int np = 1000;
bool P[1001];

bool isPal(int n) {
  int a = n, b = 0;

  while(n > 0) {
    b *= 10;
    b += n%10;
    n /= 10;
  }

  return (a == b);
}

void genPal() {
  memset(P, false, sizeof(P));
  
  for(int i=1; i*i<=np; i++) {
    if(isPal(i) && isPal(i*i)) {
      P[i*i] = true;
    }
  }

  // for(int i=1; i<=np; i++) {
  //   if(P[i])
  //     cout << ">> " << i << endl;
  // }
}

int main() {
  int t, tc = 0;
  scanf("%d", &t);
  genPal();

  while(t--) {
    tc++;

    int a, b, c = 0;
    scanf("%d %d", &a, &b);

    for(int i=a; i<=b; i++) {
      if(P[i])
	c++;
    }

    printf("Case #%d: %d\n", tc, c);
  }

  return 0;
}
