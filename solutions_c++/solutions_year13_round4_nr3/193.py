#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <cassert>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define pb push_back
#define MP make_pair
#define For(a,b,c) for(typeof(b)a=(b); a<(c); ++a)
#define ALL(a) (a).begin(),(a).end()
#define DBG(a) cout << #a << ": " << a << endl
#define FORE(i, v) for(typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

int N;
int a[2011], b[2011], x[2011];

bool rec(int val) {
  if (val == N+1) return true;

  int lis[2][2011];
  for (int dir = 0; dir < 2; dir++) {
    int cur_max = 0;
    int bit[2011] = {0};
    for (int i = (dir == 0 ? 0 : N-1); i != (dir == 0 ? N : -1); i += (dir == 0 ? 1 : -1)) {
      if (x[i] == 0) {
        lis[dir][i] = cur_max;
      } else {
        int cx = x[i]-1;
        int query = 0;
        while (cx) {
          query = max(query, bit[cx]);
          cx = cx - (cx&-cx);
        }
        cur_max = max(cur_max, query+1);
        cx = x[i];
        while (cx <= N) {
          bit[cx] = max(bit[cx], query+1);
          cx = cx + (cx&-cx);
        }
      }
    }
  }
  for (int i = 0; i < N; i++) {
    if (!x[i]) {
      if (lis[0][i]+1 == a[i] && lis[1][i]+1 == b[i]) {
        x[i] = val;
        if (rec(val+1)) {
          return true;
        }
        x[i] = 0;
      }
    }
  }
  
  return false;
}

int main()
{
  int T; cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cin >> N;
    for (int i = 0; i < N; i++) {
      cin >> a[i];
    }
    for (int i = 0; i < N; i++) {
      cin >> b[i];
    }
    
    memset(x, 0, sizeof x);
    rec(1);
    
    printf("Case #%d:", tt);
    for (int i = 0; i < N; i++) {
      printf(" %d", x[i]);
    }
    puts("");
  }
}