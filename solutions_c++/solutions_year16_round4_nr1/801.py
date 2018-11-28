#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

int Tests;
int n, P, R, S, p[10], r[10], s[10];
string t[10], tt[10];

  string f(int n, int k) {
    if (n == 0) {
      if (k == 1) return "P";
      else
      if (k == 2) return "R";
      else
      if (k == 3) return "S";
    }
    string t1 = f(n - 1, k);
    string t2 = f(n - 1, k % 3 + 1);
    if (t1 + t2 < t2 + t1) return t1 + t2;
    return t2 + t1;
  }

int main() {
  scanf("%d", &Tests); 
  for (int tts = 0; Tests--; ) {
    scanf("%d%d%d%d", &n, &R, &P, &S);
    
    string ans = "";
    for (int k = 1; k <= 3; ++k) {
      p[k] = 0; r[k] = 0; s[k] = 0;
      string res = f(n, k);
      for (int i = 0; i < res.size(); ++i) {
        if (res[i] == 'P') ++p[k];
        else
        if (res[i] == 'R') ++r[k];
        else
        if (res[i] == 'S') ++s[k];
      }
      if (p[k] == P && r[k] == R && s[k] == S) {
        if (ans == "") ans = res;
        else
        if (res < ans) ans = res;
      }
    }

    printf("Case #%d: ", ++tts);
    if (ans == "") puts("IMPOSSIBLE"); else printf("%s\n", ans.c_str());
  }
  return 0;
}