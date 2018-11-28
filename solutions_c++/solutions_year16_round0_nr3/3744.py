#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;
int digit[16] = {1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1};
long long int divider[11] = {0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1};
long long int prime[6000000];
void digitMute(){
  int i=1;
  do{
    digit[i] += 1;
    if(digit[i] >= 2){
      digit[i] -= 2;
      i++;
    }
    else break;
  }while(1);
}

int main(){
  int T;
  int N, J;
  scanf("%d", &T);
  long long int val = 0;
  long long int times = 1;
  long long int base = 2;
  for(int i=1; i<=T; i++){
    scanf("%d %d", &N, &J);
    freopen("prime.txt", "r", stdin);
    for(int j=0; j<5761456; j++)
      scanf("%lld", &prime[j]);
    fclose(stdin);
    printf("Case #1:\n");
    int cnt = 0;
    while(cnt < J){
      bool isprime = true;
      bool iscoin = true;
      digitMute();
      for(base = 2; base<=10; base++){
        isprime = true;
        val = 0;
        times = 1;
        for(int j=0; j<=N; j++){
          val += (long long int)digit[j] * times;
          times *= base;
        }
        for(int j=1; (j<5761456 && (prime[j] * prime[j] <= val)); j++){
          if(val % prime[j] == 0){
            isprime = false;
            divider[base] = prime[j];
            break;
          }
        }
        if(isprime){
          iscoin = false;
          break;
        }
      }
      if(iscoin){
        for(int j=15; j>=0; j--)
          printf("%d", digit[j]);
        for(int j=2; j<=10; j++)
          printf(" %lld", divider[j]);
        printf("\n");
        cnt++;
      }
    }
  }
  return 0;
}
