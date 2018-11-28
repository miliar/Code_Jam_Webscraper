#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
using namespace std;

typedef pair<int,int> pairii;
typedef long long llong;

#define pb push_back
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

const int MAXN = 1005;
int n,k,ar[MAXN],buf[MAXN*MAXN],tm[MAXN];

llong gcd(llong x, llong y) {
  if(y != 0) return gcd(y, x%y);
  return x;
}

llong lcm(llong x, llong y) {
  return y * (x / gcd(x, y));
}

void solve() {
  cin>>n>>k;
  FORZ(i,n)scanf("%d",ar+i);
  llong rnd = 1;
  FORZ(i,n) rnd *= ar[i] / gcd(rnd, ar[i]);
  int c=0;
  FORZ(i,n) tm[i]=0;
  FORZ(i,rnd) {
    FORZ(j,n) {
      if (tm[j]==0) {
        buf[c++]=j;
        tm[j]=ar[j];
      }
    }
    FORZ(j,n) tm[j]--;
  }
  cout << buf[(k-1)%c]+1 << "\n";
}

int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }
  
  return 0;
}
