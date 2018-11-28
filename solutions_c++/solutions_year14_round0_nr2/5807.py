#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;

int c, sign;
inline void get_int(int& n) {
  n = 0;
  c = getchar_unlocked();
  sign = 1;
  while (c < '0' || c > '9') {
    if (c == '-') sign = -1;
    c = getchar_unlocked();
  }
  while (c >= '0' && c <= '9') {
    n = (n<<3) + (n<<1) + c - '0';
    c = getchar_unlocked();
  }
  n = sign*n;
}

int main() {
  int T;
  get_int(T);
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    
    double C, F, X;
    cin >> C >> F >> X;
    
    double ans = 100000;
    double running = 0;
    int farms = 0;
    double temp_ans = 0;
    
    while (true) {
      temp_ans = running + X/(2.0 + farms*F);
      
      if (temp_ans > ans) break;
      else ans = min(ans, temp_ans);
      
      running += C/(2.0 + farms*F);
      farms++;
    }
    printf("%0.7lf\n", ans);
  }
  return 0;
}