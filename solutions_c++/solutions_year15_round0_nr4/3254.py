#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <numeric>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <cstring>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <functional>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>
#include <iomanip>

using namespace std;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define ford(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define rep(i, N) FOR(i, 0, N)
#define FILL(A,value) memset(A,value,sizeof(A))

#define all(V) V.begin(), V.end()
#define sz(V) (int)V.size()
#define pb  push_back
#define mkp make_pair

#define fi first
#define se second

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int INF = 1000000000;
const int MAX = 1010;
const int MOD = 1000000007 ;

int main() {
  int t, __case = 1;
  cin >> t;
  while(t--) {
    int x, r, c ; cin >> x >> r >> c;
    printf("Case #%d: ",__case++);
    if(x == 1) {
      puts("GABRIEL");
      continue;
    }
    else if(x == 2) {
      if((r % 2 == 0) || (c % 2 == 0)) puts("GABRIEL") ;
      else puts("RICHARD");
    }
    else if(x == 3) {
      if(((r * c) % 3 > 0) || (r == 1 && c == 3) || (r == 3 && c == 1)) puts("RICHARD") ;
      else puts("GABRIEL") ;
    }
    else if(x == 4) {
      if((r == 1) || (c == 1) || ((r * c) % 4 > 0) || (r == 2 && c == 2) || (r == 2 && c == 4) || (r == 4 && c == 2)) puts("RICHARD");
      else puts("GABRIEL");
    }
  }
  return 0;
}