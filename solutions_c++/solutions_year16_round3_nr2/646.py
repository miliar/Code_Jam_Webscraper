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

const int MAXN=55;
int n;
llong m;
int mat[MAXN][MAXN];

void solve() {
  cin>>n>>m;
  if (m>(1LL<<(llong)(n-2))) {
    cout<<"IMPOSSIBLE\n";
    return;
  }
  cout<<"POSSIBLE\n";
  FORZ(i,MAXN) memset(mat[i],0,sizeof mat[i]);
  m+=(1LL<<(llong)(n-2))-1;
  llong sum=0;
  for (int i=n-2; i>=0; i--) {
    if (sum>=m) break;
    llong p=1LL<<((llong)((n-2)-i));
    if (sum+p<=m) {
      FOR(j,i+1,n) mat[i][j]=1;
      sum+=p;
    } else {
      llong rem=m-sum;
      int j=n-2;
      while (rem>0) {
        mat[i][j]=rem%2LL;
        rem>>=1LL;
        j--;
      }
      break;
    }
  }
  FORZ(i,n) {
    FORZ(j,n) {
      cout<<mat[i][j];
    }
    cout<<"\n";
  }
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
