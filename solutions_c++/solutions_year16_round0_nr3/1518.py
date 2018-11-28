#include<stdio.h>

using namespace std;

int num[16];

long long tobase(int n, int b){ //n length of n, b base
  long long inten = 0;
  long long pow = 1;
  for (int i = 0; i < n; i++){
    inten += num[n - 1 - i] * pow;
    pow *= b;
  }
  return inten;
}

long long is_prime(long long n){
  long long i;
  i = 2;
  for (i = 2; i < 10000; i++){
    if (n % i == 0) return i;
  }
  return 0;
}

void add_one(int n){
  int k = n-2;
  while (k > 1){
    if (num[k] == 0) {
      num[k] = 1;
      break;
    }
    else{
      num[k] = 0;
      k--;
    }
  }
}

int main(){
  int T;
  int N, J;
  long long n;
  long long proof[9];
  bool prime;
  scanf("%d", &T);

  for (int t = 0; t < T; t++){
    printf("Case #%d:\n", t+1);
    scanf("%d %d", &N, &J);
    for (int i = 0; i < N; i++){
      num[i] = 0;
    }
    num[0] = 1;
    num[N-1] = 1;
    int printed = 0;
    long long  count = 0;
    while (printed < J){
      count ++;
      prime = false;
      //printf("stop1\n");
      for (int i = 0; i < 9; i++) proof[i] = 0;
      //printf("stop2\n");
      for (int b = 2; b < 11; b++){
	//printf("b = %d ", b);
	n = tobase(N, b);
	//printf("%lld", n);
	proof[b-2] = is_prime(n);
	//printf("b = %d %lld %lld | ", b, n, proof[b-2]);
	if (proof[b-2] == 0) prime = true;
      }
      //printf("stop3\n");
      //printf("count %lld printed %d\n", count, printed);
      if (prime == false){
	printed ++;
	printf("%lld", n);
	for (int b = 2; b < 11; b++) printf(" %lld", proof[b-2]);
	printf("\n");
      }
      
      //printf("\n");
      add_one(N);
      //printf("added one\n");
    }
    
  }
  return 0;
}