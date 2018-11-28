#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<list>
#include<cctype>
#include<algorithm>
#include<functional>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>

using namespace std;

#define INF 0x7FFFFFFF
#define INFLL 0x7FFFFFFFFFFFFFFF
#define BIG 0x4F4F4F4F
#define RESET(a,x) memset(a,x,sizeof(a))
#define EXIST(a,s) ((s).find(a) != (s).end())
#define eps 1e-9
typedef long long ll;
typedef unsigned long long ull;
const double PI = acos(-1.0);

#define sqr(x) ((x)*(x))
#define eps 1e-9
#define REP(I,N) for(size_t I=0;I<(N);I++)
#define REPR(I,A,B) for(size_t I=(A);I<(B);I++)
#define REPE(I,A,B) for(size_t I=(A);I<=(B);I++)
#define RS(X) scanf("%s", (X))
#define RI(X) scanf("%d", &(X))
#define RD(X) scanf("%lf", &(X))
#define RII(X,Y) scanf("%d%d", &(X), &(Y))
#define FOR_EACH(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

int n;
int t;
const int maxn = 20;
int a[maxn][maxn];
set<int> b;
bool bo[maxn];

int main() {
#ifdef PRETEST
  freopen("in.txt", "r", stdin);
#endif
  RI(t);
  REPE(tt, 1, t) {
    b.clear();
    REP(k, 2) {
      int p;
      RI(p);
      p--;
      REP(i, 4) {
        REP(j, 4) {
          RI(a[i][j]);
        }
      }
      if (k == 0) {
        REP(j, 4) {
          b.insert(a[p][j]);
        }
      } else {
        memset(bo, false, sizeof(bo));
        REP(j, 4) {
          bo[a[p][j]] = true; 
        }
        REPE(i, 1, 16) {
          if (!bo[i]) {
            if (b.find(i) != b.end()) {
              b.erase(i);
            }
          }
        }
      }
    }
    cout << "Case #" << tt << ": ";
    if (b.empty()) {
      cout << "Volunteer cheated!";
    } else if (b.size() > 1) {
      cout << "Bad magician!";
    } else  {
      cout << *(b.begin());
    }
    cout << endl;
  }
  return 0;
}


