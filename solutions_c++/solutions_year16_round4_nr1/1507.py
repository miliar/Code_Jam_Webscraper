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

int n,r,p,s;
set<string> res;

int comp(char a, char b) {
  if (a==b) return 0;
  else if ((a=='P'&&b=='R') || (a=='R'&&b=='S') || (a=='S'&&b=='P')) return 1;
  else return -1;
}

bool check(string sq) {
  string  newsq;
  if (sq.size()==2 && sq[0]!=sq[1]) return true;
  for (int i=0; i<sq.size(); i+=2) {
    if (sq[i]==sq[i+1]) return false;
    if (comp(sq[i],sq[i+1])==1) newsq.pb(sq[i]);
    else newsq.pb(sq[i+1]);
  }
  return check(newsq);
}

void solve() {
  char str[10];
  cin>>n>>r>>p>>s;
  res=set<string>();
  int idx=0;
  FORZ(i,p) str[idx++]='P';
  FORZ(i,r) str[idx++]='R';
  FORZ(i,s) str[idx++]='S';
  do {
    string tmps(str);
    if (check(tmps)) {
      res.insert(tmps);
    }
  } while (next_permutation(str, str+(1<<n)));
  if (res.empty()) {
    cout<<"IMPOSSIBLE\n";
  } else {
    cout<<*(res.begin())<<"\n";
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
