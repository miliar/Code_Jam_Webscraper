#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <ctime>

#define pb push_back
#define mp make_pair
#define PI 3.1415926535897932384626433832795
#define ALL(x) x.begin(), x.end()
#define F first
#define S second
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,-1,sizeof(x))
#define pw(x) (1ull<<(x))

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

int main() {
  //freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int te=0;te<t;te++) {
    int was[20];
    m0(was);
    int ans1 = 0;
    cin >> ans1;
    for (int i=0;i<4;i++) {
      for (int j=0;j<4;j++) {
        int cur; cin >> cur;
        if (i+1==ans1) was[cur]++;
      }
    }
    cin >> ans1;
    for (int i=0;i<4;i++) {
      for (int j=0;j<4;j++) {
        int cur; cin >> cur;
        if (i+1==ans1) was[cur]++;
      }
    }
    vector<int> ans;
    for (int i=0;i<20;i++) {
      if (was[i]==2) {
        ans.pb(i);
      }
    }
    cout << "Case #" << te+1 << ": ";
    if (ans.size()>1) {
      cout << "Bad magician!";
    }
    else if (ans.size()<1) {
      cout << "Volunteer cheated!";
    }
    else {
      cout << ans[0];
    }
    cout << "\n";
  }
  return 0;
}
