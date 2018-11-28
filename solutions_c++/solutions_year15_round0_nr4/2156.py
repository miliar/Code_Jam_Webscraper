#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <algorithm>

using namespace std;

#define rep(i,j) REP((i), 0, (j))
#define REP(i,j,k) for(int i=(j);(i)<(k);++i)
#define BW(a,x,b) ((a)<=(x)&&(x)<=(b))
#define ALL(v) (v).begin(), (v).end()
#define LENGTHOF(x) (sizeof(x) / sizeof(*(x)))
#define AFILL(a, b) fill((int*)a, (int*)(a + LENGTHOF(a)), b)
#define SQ(x) ((x)*(x))
#define Mod(x, mod) (((x)+(mod)%(mod))
#define MP make_pair
#define PB push_back
#define Fi first
#define Se second
#define INF (1<<29)
#define EPS 1e-10
#define MOD 1000000007

typedef pair<int, int> pi;
typedef pair<int, pi> pii;
typedef vector<int> vi;
typedef queue<int> qi;
typedef long long ll;

int T;

int solve(int x, int r, int c)
{
  if(x==1) return 1;
  if(x==2){
    if(r==1&&c==1) return 0;
    if((r*c)%2) return 0;
    return 1;
  }
  if(x==3){
    if(r<=2&&c<=2) return 0;
    if(r==1||c==1) return 0;
    if((r*c)%3) return 0;
    return 1;
  }
  if(x==4){
    if(r<=3&&c<=3) return 0;
    if(r<=2||c<=2) return 0;
    return 1;
  }
  return 0;
}

int main()
{
  scanf("%d", &T);
  for(int tcase=1;tcase<=T;tcase++){
    int X, R,C;
    scanf("%d%d%d", &X, &R, &C);
    printf("Case #%d: %s\n", tcase, solve(X,R,C)?"GABRIEL":"RICHARD");
  }
  return 0;
}

