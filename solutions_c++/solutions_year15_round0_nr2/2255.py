#include <cstdio>

int T;
int P[1024];
int D;
int temp;
int max, ans;
int countt;

int main(){
  int i, j;

  scanf("%d", &T);
  for(int tt = 0; tt < T; tt++){
    scanf("%d", &D);
    for(i = 0; i <= 1000; i++)
      P[i] = 0;

    max = 0;
    for(i = 0; i < D; i++){
      scanf("%d", &temp);
      P[temp]++;
      
      if(temp > max)max = temp;
    }
    
    ans = 1000;
    for(i = max; i > 0; i--){
      countt = 0;
      for(j = max; j > i; j--){
	countt += (j / i - (j % i == 0)) * P[j];
      }
      if(ans > countt + i)ans = countt + i;
    }

    printf("Case #%d: %d\n", tt + 1, ans);
  }
}
