#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <cstdlib>

using namespace std;

#define ri(X) scanf("%d", &(X))
#define pi(X) printf("%d", (X))
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define lint long long
#define pii pair<int,int>
#define inf 1e9
#define linf 1e18
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define uni(X) X.erase(unique(X.begin(), X.end()), X.end());

int t, n;
string s;

int main(){
  ri(t);
  for (int test = 1; test <= t; test++) {
    ri(n);
    cin >> s;
    int res = 0;
    int stand = 0;
    for (int i = 0; i < s.size(); i++) {
      int cur = (s[i]-'0');
      if (cur > 0) {
        if (stand < i) {
          res += (i - stand);
          stand = i;
        }
        stand += cur;
      }
    }
    printf("Case #%d: %d\n", test, res);
  }
  
  return 0;
}
