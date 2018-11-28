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

// 1234, 123 => 1234321
LL merge_to_palin(LL a, LL b) {
  LL ret = a;
  while(b) {
    ret*=10;
    ret+=b%10;
    b/=10;
  }
  return ret;
}

bool ispalin(LL v) {
  LL k = 1;
  while(v/k != 0) {
    k*=10;
  }
  k/=10;
  LL i = 0;
  LL r = 10;
  LL v1 = v;
  while(k > r) {
    LL left = (v/k)%10;
    LL right = v1%10;
    v1/=10;
    if (left != right)
      return false;
    k/=10;
    r*=10;
  }
  return true;
}

LL get_to(LL value) {
  LL ret = 0;
  for(LL i = 1; i<10; i++) {
    if (i*i > value)
      return ret;
    if (i == 1 || i==2 || i==3)
      ret++;
  }
  for(LL i = 1;; i++) {
    if (i*i > value)
      return ret;
    LL base = merge_to_palin(i, i);
    LL v = base*base;
    if (base*base > value) {
      return ret;
    }
    if (ispalin(v)) {
      //cout<<i<<" "<<v<<endl;
      ret++;
    }
  }
  return ret;
}

int main() {
  int T;
  GI(T);
  LL a, b;
  FORN(i, T) {
    printf("Case #%d: ", i+1);
    cin >> a >> b;
    printf("%lld\n", get_to(b) - get_to(a-1));
  }
  return 0;
}
