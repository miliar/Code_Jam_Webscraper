#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int inf = 2e9;
const int mod = 1e9 + 7;
const int MAXN = 3e5;
const int N = 5e5 + 11;

int main(){
  #if __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #else
    // freopen("typing.in", "r", stdin);
    // freopen("typing.out", "w", stdout);
  #endif
  int t;
  scanf("%d", &t);
  char a[123];
  int q = 0;
  while (t--){
    ++q;
    scanf("%s", a);
    int n = strlen(a);
    int res = 0;
    while (1){
      bool f = true;
      int r;
      for (int i = 0; i < n; i++) {
        if (a[i] == '-') {
          f = false;
          r = i;
        }
      }
      if (f) break;
      ++res;
      for (int i = 0; i <= r; i++){
        if (a[i] == '+') a[i] = '-';
        else a[i] = '+';
      }
    }
    printf("Case #");
    printf("%d", q);
    printf(": %d\n", res);
  }
  return 0;
}







