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

string s;

void rep(int i, string& tmp) {
  if (i>=s.length()) return;
  if (i==0) {
    tmp.pb(s[0]);
  } else {
    if (tmp[0]<=s[i]) {
      string tmp2;
      tmp2.pb(s[i]);
      tmp2.append(tmp);
      tmp=tmp2;
    } else {
      tmp.pb(s[i]);
    }
  }
  rep(i+1,tmp);
}

void solve() {
  cin>>s;
  string res;
  rep(0,res);
  cout<<res<<"\n";
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
