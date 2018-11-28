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

bool solve2() {
  int x,r,c;
  cin>>x>>r>>c;
  if (r>c) swap(r,c);
  if (x==1) return false;
  else if (x==2) {
    if ((r*c)%2!=0) return true;
    else return false;
  } else if (x==3) {
    if ((r*c)%3!=0||r==1) return true;
    return false;
  } else {
    if (r==1||r==2) return true;
    if (r==3) {
      if (c<4) return true;
      else return false;
    }
    else return false;
  }
  return false;
}

void solve() {
  if (solve2()) cout << "RICHARD\n";
  else cout << "GABRIEL\n";
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}

