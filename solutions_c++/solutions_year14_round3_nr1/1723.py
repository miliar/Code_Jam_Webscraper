#define EACH(i,c) for(__typeof(c.begin()) i=(c).begin();i!=(c).end();i++)
#include<algorithm>
#include<bitset>
#include<cassert>
#include<cfloat>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<limits>
#include<map>
#include<queue>
#include<set>
#include<vector>

const long double PI = 2*acos(.0L);
using namespace std;

long long gcd(int a, int b) { return b==0?a:gcd(b, a%b); }

struct Fraction {
  long long a, b;
  Fraction(long long _a, long long _b) {
    long long _ = gcd(_a, _b);
    a = _a/_;
    b = _b/_;
  }
};

bool operator>=(const Fraction &a, const Fraction &b) {
 return a.a*b.b >= b.a*a.b;
}

void operator-=(Fraction &a, const Fraction &b) {
  long long _ = a.b/gcd(a.b, b.b)*b.b;
  a.a = _/a.b*a.a-_/b.b*b.a;
  a.b = _;
}

bool powerOfTwo(long long x) {
  while(!(x&1))
    x>>=1;
  return x==1;
}

int main() {
  int nCase;
  scanf("%d", &nCase);
  for(int iCase = 1; iCase<=nCase; iCase++) {
    long long _0, _1;
    scanf("%lld/%lld", &_0, &_1);
    Fraction _2(_0, _1), _3(1, 1);
    if(powerOfTwo(_2.b)) {
      for(int i = 0; _2.a; i++, _3.b<<=1) {
        if(_2 >= _3) {
          //_2 -= _3;
          //printf("~%d ", i);
          printf("Case #%d: %d\n", iCase, i);
          break;
        }
      }
    } else {
      printf("Case #%d: impossible\n", iCase);
    }
  }
  return 0;
}
