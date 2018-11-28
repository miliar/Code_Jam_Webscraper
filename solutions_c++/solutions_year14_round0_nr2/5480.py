#pragma comment(linker,"/STACK:100000000000,100000000000")

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <map>
#include <stack>
#include <set>
#include <iomanip>
#include <queue>
#include <map>
#include <functional>
#include <list>
#include <sstream>
#include <ctime>
#include <climits>
#include <bitset>
#include <list>
#include <cassert>
#include <complex>

using namespace std;

/* Constants begin */
const long long inf = 1e18+7;
const long long mod = 1e9+9;
const double eps = 1e-9;
const double PI = 2*acos(0.0);
const double E = 2.71828;
/* Constants end */

/* Defines begin */
#define pb push_back
#define mp make_pair
#define ll long long
//#define double long double
#define F first
#define S second
#define all(a) (a).begin(),(a).end()
#define forn(i,n) for (int (i)=0;(i)<(n);(i)++)
#define random (rand()<<16|rand())
#define sqr(x) (x)*(x)
#define base complex<double>
/* Defines end */

double c, f, x;

void Solve(){
  scanf("%lf %lf %lf", &c, &f, &x);
  double add = 2;
  double res = inf;
  double need = 0;
  for(int i = 0; i <= x + 1; ++i){
   // cout << res << " " << need << " " << x << endl;
    res = min(res, need + x / add);
    need += c / add;
    add += f;
  }
  printf("%.7lf\n", res);
}

int main(void){
  #ifdef nobik
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
  #endif
  int t; scanf("%d", &t);
  forn(i, t){
    printf("Case #%d: ", i + 1);
    Solve();
  }
  return 0;
}
