//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
using namespace std;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define CLEAR(x) (memset(x,0,sizeof(x)))
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define VAR(v, n) __typeof(n) v = (n)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOREACH(i, c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define DBG(v) cout<<#v<<" = "<<v<<endl;
#define IN(x,y) ((y).find(x)!=(y).end())
#define ST first
#define ND second
#define PB push_back
#define PF push_front
#define MP make_pair
typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

int t;
double c,f,x;
int main() {
  scanf("%d",&t);
  FOR(ttt,1,t) {
    scanf("%lf %lf %lf",&c,&f,&x);
    //printf("%lf %lf %lf",c,f,x);
    long double mint = 1e+8;
    long double tim = 0;
    long double rat = 2.0;
    for(int i = 0; i <= 100010; i++) {
        mint = MIN(mint,tim + x/rat);
        tim = tim + c/rat;
        rat += f;
    }
    double ans = (double)mint;
    //printf("%Lf %Lf\n",rat,tim);
    printf("Case #%d: %.9f\n",ttt,ans);
  }
  return 0;
}
