#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define GI(x) scanf("%d", &x);
#define FORN(i, n) for(int i = 0; i < n; i++)
#define FOR(i, start, end) for(int i = start; i < end; i++)
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 1000000000
using namespace std;

double cost(double c, double f, double x, int n) {
  double rate = 2.0;
  double ret = 0;
  FORN(i, n-1) {
    ret += (c/rate);
    rate += f;
  }
  ret += x/rate;
  return ret;
}

void solve(double c, double f, double x) {
  int left = 1, right = 1000000;
  while (right - left > 10) {
    //cout << left <<" "<<right<<endl;
    int first = (2*left+right)/3;
    int second = (left+2*right)/3;
    if (first == second) break;
    double c1 = cost(c, f, x, first);
    double c2 = cost(c, f, x, second);
    //cout<<"costleft: "<<cost(c, f, x, left)<<endl;
    //cout<<"costright: "<<cost(c, f, x, right)<<endl;
    if (c2 - c1 > 1e-9) {
      right = second;
    } else if (c1 - c2 > 1e-9) {
      left = first;
    } else {
      break;
    }
  }
  double ret = 1e18;
  for (int i = left; i <= right; i++) {
    double cst = cost(c, f, x, i);
    //cout << i << ", " << cst << endl;
    if (ret - cst > 1e-9)
      ret = cst;
  }

  printf("%.8f\n", ret);
}
int main() {
  int tes;
  cin >> tes;
  FORN(i, tes) {
    double c,f,x;
    cin>>c>>f>>x;
    printf("Case #%d: ", i+1);
    solve(c, f, x);
  }
}
