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
#define FORZ(i,n) FOR((i),0,(n)

void solve() {
  string s;
  cin>>s;
  int n=(int)s.length();
  int res=1;
  char curr=s[0];
  FOR(i,1,n) {
    if (curr!=s[i]) {
      curr=s[i];
      res++;
    }
  }
  if (s[n-1]=='+') res--;
  printf("%d\n",res);
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
