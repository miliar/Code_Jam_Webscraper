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

string key,tg;
int k,l,s;

void en(vector<string>& s, int len) {
  int m=(int)key.length();
  if (len==1) {
    FORZ(i,m) {
      string ts;
      ts.pb(key[i]);
      s.pb(ts);
    }
    return;
  }
  vector<string> tmp;
  en(tmp,len-1);
  FORZ(i,m) {
    FORZ(j,tmp.size()) {
      string ts;
      ts.pb(key[i]);
      ts.append(tmp[j]);
      s.pb(ts);
    }
  }
}

int check(string& tmps) {
  int m=(int)tmps.length();
  int res=0;
  FORZ(i,m-l+1) {
    bool valid=true;
    FOR(j,i,i+l) valid &= (tmps[j]==tg[j-i]);
    if (valid) res++;
  }
  return res;
}

void solve() {
  cin>>k>>l>>s;
  cin>>key;
  cin>>tg;
  vector<string> all;
  en(all,s);
  int mx=0,sum=0;
  FORZ(i,all.size()) {
    int r = check(all[i]);
    mx=max(r,mx);
    sum+=r;
  }
  double ep = (double)sum/(double)all.size();
  printf("%.6f\n",(double)mx-ep);
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
