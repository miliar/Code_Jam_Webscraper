#include <bits/stdc++.h>

#define F first
#define S second
#define llong long long
#define ullong unsigned long long
#define mp make_pair
#define pb push_back

using namespace std;

int T;
int n;
int a[1111];
int ans1, ans2;
int rate;
int cur;

int main(){
  #ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif
  scanf("%d", &T);
  for(int test = 1; test <= T; ++test){
    ans1 = ans2 = rate = 0;
    scanf("%d", &n);
    for(int i = 0; i < n; ++i){
      scanf("%d", &a[i]);
    }
    for(int i = 1; i < n; ++i){
      if(a[i] < a[i - 1])
        ans1 += a[i - 1] - a[i];
    }
    for(int i = 1; i < n; ++i){
      if(a[i] < a[i - 1]){
        rate = max(rate, a[i - 1] - a[i]);
      }
    }
    for(int i = 0; i < n - 1; ++i){
      ans2 += min(rate, a[i]);
    }
    printf("Case #%d: %d %d\n", test, ans1, ans2);
  }
  return 0;
}
