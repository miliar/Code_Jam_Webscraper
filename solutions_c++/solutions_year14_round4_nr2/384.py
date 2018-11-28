#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int n;
int a[1<<17];

void solve (){
  scanf("%d", &n);
  for (int i = 0; i < n; ++i)
    scanf("%d", &a[i]);

  int ans = 0;
  int l, r;

  l = 0; r = n-1;

  for (int i = 0; i < n; ++i){
    int m = min_element(a+l, a+r+1) - a;
    if (m-l < r-m){
      while (m > l){
	++ans;
	swap(a[m], a[m-1]);
	--m;
      }

      ++l;
    }
    else{
      while (m < r){
	++ans;
	swap(a[m], a[m+1]);
	++m;
      }

      --r;
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


