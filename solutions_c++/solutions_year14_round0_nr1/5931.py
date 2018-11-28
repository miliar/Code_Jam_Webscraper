#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define rep(x,n) for(int x = 0; x < n; ++x)
#define print(x) cout << x << endl
#define dbg(x) cerr << #x << " == " << x << endl
#define _ << " , " <<
#define mp make_pair
#define x first
#define y second

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;
typedef pair<int,int> pii;

int ans[2];
int grid[2][4][4];

void read() {
  rep(i,2) {
    cin >> ans[i];
    rep(j,4) rep(k,4) cin >> grid[i][j][k];
  }
}

void process(int testcase) {
  int freq[17]={0};
  rep(i,2) {
    rep(j,4) rep(k,4) if(j == ans[i]-1) freq[grid[i][j][k]]++;
  }
  int magic = -1;
  rep(i,17) if(freq[i] == 2) {
    if(magic == -1) magic = i;
    else magic = -2;
  }
  printf("Case #%d: ",testcase);
  if(magic == -1) puts("Volunteer cheated!");
  if(magic == -2) puts("Bad magician!");
  if(magic > 0) printf("%d\n",magic);
}

int main() {
  int T;
  cin >> T;
  for(int testcase=1;testcase<=T;testcase++) {
    read();
    process(testcase);
  }
  return 0;
}

