#include <stdio.h>

int dp[500];
int arr[500];
int N, L;

void prework(){
  dp[0] = 0;
  for(int i=1; i<=L; i++){
    dp[i] = dp[i-1] + L-i + 1;
  }
}

int main(){
  int jcase;
  int a, b, p;
  int mode1, mode2;
  int end, mini;
  bool good;
  
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-small-attempt0.out", "w", stdout);
  //freopen("A-large.in", "r", stdin);
  //freopen("A-large.out", "w", stdout);
  
  scanf("%d", &jcase);
  for(int icase=0; icase<jcase; icase++){
    scanf("%d %d", &L, &N);
    prework();
    
    for(int i=0; i<L; i++) arr[i] = 0;
    
    mode1 = 0;
    for(int i=0; i<N; i++){
      scanf("%d %d %d", &a, &b, &p);
      for(int j=a; j<b; j++){
        arr[j]+=p;
      }
      mode1 += dp[b-a] * p;
    }
    
    mode2 = 0;
    while(true){
      good = false;
      for(int i=0; i<L; i++){
        if(arr[i] == 0) continue;
        good = true;
        mini = arr[i];
        //printf("mini = arr[%d] = %d\n", i, arr[i]);
        end = L;
        for(int j=i+1; j<L; j++){
          if(arr[j] == 0){
            end = j;
            break;
          }
          if(arr[j] < mini) mini = arr[j];
        }
        
        for(int j=i; j<end; j++){
          arr[j] -= mini;
        }
        
        //printf("end=%d, mini=%d\n", end, mini);
        mode2 += dp[end-i] * mini;
        break;
      }
      if(!good) break;
    }
    
    printf("Case #%d: %d\n", icase+1, mode1-mode2);
  }
  return 0;
}
