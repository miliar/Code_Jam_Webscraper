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

int ar[30];
int n;

void solve() {
  cin>>n;
  int sz=0;
  FORZ(i,n) {
    cin>>ar[i];
    sz+=ar[i];
  }
  while (sz>0) {
    int mx1=0,mx2=0,idx1=-1,idx2=-1;
    FORZ(i,n) {
      if (ar[i]>mx1) {
        idx2=idx1;
        mx2=mx1;
        idx1=i;
        mx1=ar[i];
      } else if (ar[i]>mx2) {
        idx2=i;
        mx2=ar[i];
      }
    }
    if (idx1==-1) break;
    char c1='A'+idx1;
    char c2='A'+idx2;
    if ((mx1-1)*2>sz-1||mx2*2>sz-1) {
      cout<<c1<<c2<<" ";
      sz-=2;
      ar[idx1]--;
      ar[idx2]--;
    } else {
      cout<<c1<< " ";
      sz--;
      ar[idx1]--;
    }
  }
  cout<<"\n";
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
