#include <cstdio>
#include <vector>
#include <set>

using namespace std;

typedef long long llint;

vector< llint > v;
set< llint > S;

void test( llint x ) {
  if( S.count(x*x) ) return;

  llint y = 0, p = x*x;
  while(p > 0) y = y*10+(p%10), p /= 10;
  if(x*x == y) S.insert(x*x);
}

int main() {
  for(int i = 0; i < 10000; ++i) {
    int x = i, y = 0, pw = 1;
    while(x > 0) {
      y = y*10 + (x%10);
      x /= 10;
      pw *= 10;
    }

    test( i*pw+y );
    for(int j = 0; j < 10; ++j)
      test( (i*10 + j)*pw + y );
  }

  vector< llint > v;
  for(set< llint > :: iterator it = S.begin(); it != S.end(); ++it)
    v.push_back(*it);
  
  int t;
  scanf("%d", &t);
  for(int c = 1; c <= t; ++c) {
    llint a, b;
    scanf("%lld %lld", &a, &b);

    int ans = 0;
    for(int i = 0; i < (int)v.size(); ++i)
      if(v[i] >= a && v[i] <= b) ans++;
   
    printf("Case #%d: %d\n", c, ans);
  }
  return 0;
}
