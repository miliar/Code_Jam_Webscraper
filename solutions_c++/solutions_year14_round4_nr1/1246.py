#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

int arr[10100];
bool use[10010];

int main(){
  int jcase;
  int N, X;
  int ans;
  
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  
  scanf("%d", &jcase);
  for(int icase=0; icase<jcase; icase++){
    scanf("%d %d", &N, &X);
    for(int i=0; i<N; i++) scanf("%d", &arr[i]);
    sort(arr, arr+N);
    
    ans = 0;
    memset(use, false, sizeof(use));
    int ct = 0;
    
    for(int i=N-1; i>=0; i--){
      if(use[i]) continue;
      use[i] = true;
      if(arr[i] + arr[ct] <= X){ 
        use[ct] = true;
        ct++;
      }
      ans++;
    }
    printf("Case #%d: %d\n", icase+1, ans);
  }
  
  return 0;
}
