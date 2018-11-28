#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <complex>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <iomanip>
#include <assert.h>
#include <array>
#include <cstdio>
#include <cstring>
#include <random>
#include <functional>
#include <numeric>
#include <bitset>

using namespace std;

struct before_main{before_main(){cin.tie(0); ios::sync_with_stdio(false);}} before_main;

#define REP(i,a,b) for(int i=a;i<(int)b;i++)
#define rep(i,n) REP(i,0,n)
#define all(c) (c).begin(), (c).end()
#define zero(a) memset(a, 0, sizeof a)
#define minus(a) memset(a, -1, sizeof a)
template<class T1, class T2> inline bool minimize(T1 &a, T2 b) { return b < a && (a = b, 1); }
template<class T1, class T2> inline bool maximize(T1 &a, T2 b) { return a < b && (a = b, 1); }

typedef long long ll;
int const inf = 1<<29;

int main() {

  int T; cin >> T;
  rep(_, T) {
    string s; cin >> s;
    int N = s.size();
    reverse(all(s));
    int cnt = 0;
    bool flag = 0;
    rep(i, N) {
      if(!flag) {
        if(s[i] == '-') {
          flag ^= 1;
          cnt ++;
        }
      } else {
        if(s[i] == '+') {
          flag ^= 1;
          cnt ++;
        }
      }
    }
    cout << "Case #" << _ + 1 << ": " << cnt << endl;
  }
  
  return 0;
}