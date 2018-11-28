#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;
typedef long long llint;

int n;

llint prime (llint x) {
  for (llint i = 2; i*i <= x; ++i)
    if (x%i == 0) return i;

  return -1;
}
void print (int x) {
  while (x) {
    printf("%d", x%2);
    x /= 2;
  }
  printf(" ");
}

int check (int x) {
  vector<llint> ret;
  for (int i = 2; i <= 10; ++i) {
    llint num = 0;
    llint y = x;
    while (y) {
      num = num*i + y%2;
      y /= 2;
    }
    ret.push_back(prime(num));
    if (ret.back() == -1) return 0;
  }
  print(x);
  for (int i = 0; i < ret.size(); ++i)
    printf("%lld ", ret[i]);
  printf("\n");
  return 1;
}


void solve (){
  int j;
  scanf("%d%d", &n, &j);
  printf("\n");
  for (int i = 0; i < (1 << n) && j; ++i) {
    if (!(i&1)) continue;
    if (!(i & (1 << (n-1)))) continue;
    if (check(i)) {
      --j;
    }
  }
}

int main (void){
  int tc; scanf ("%d", &tc);
  for (int i = 1; i <= tc; ++i){
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}


