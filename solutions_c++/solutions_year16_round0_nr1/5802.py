#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;
typedef long long llint;

void solve (){
  int n;
  scanf("%d", &n);
  int i;
  llint num = n;
  bool occ[10] = {0};
  int t = 0;
  for (i = 0; i < 1000000; ++i) {
    llint tmp = num;
    while (tmp) {
      if (!(occ[tmp%10]++)) ++t;
      tmp /= 10;
    }

    if (t == 10) break;
    num += n;
  }

  if (i < 100000) printf("%lld\n", num);
  else printf("INSOMNIA\n");
}

int main (void){
  int tc; scanf ("%d", &tc);
  for (int i = 1; i <= tc; ++i){
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}


