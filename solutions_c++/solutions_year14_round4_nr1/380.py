#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int n, x;
int a[10005];

void solve (){
  scanf("%d%d", &n, &x);
  for (int i = 0; i < n; ++i)
    scanf("%d", &a[i]);

  sort(a, a+n); reverse(a, a+n);

  int ans = 0;
  for (int i = 0; i < n; ++i){
    if (a[i] == 0) continue;
    ++ans; int c = x - a[i];
    a[i] = 0;
    for (int j = i+1; j < n; ++j)
      if (a[j] > 0 && a[j] <= c){
	a[j] = 0;
	break;
      }
  }

  printf("%d\n", ans);
}

int main (void){
  int tc; scanf ("%d", &tc);
  for (int i = 1; i <= tc; ++i){
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}


