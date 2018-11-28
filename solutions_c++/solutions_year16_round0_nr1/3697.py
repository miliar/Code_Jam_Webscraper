#include <cstdio>
#include <cstring>

using namespace std;

int T;
int N;


bool has[10];

int process(int num){
  int count = 0;

  while(num > 0){
    int digit = num % 10;
    if(! has[digit]){
      has[digit] = true;
      count++;
    }

    num /= 10;
  }

  return count;
}

int find(int n){
  for(int i=0;i<10;i++) has[i] = false;
  int count = 0;

  if(n == 0) return 0;

  int num = 0;
  while(count < 10){
    num += n;
    count += process(num);
  }

  return num;
}

int main(){
  scanf("%d", &T);

  for(int i=0;i<T;i++){
    scanf("%d", &N);
    int ans = find(N);
    if (ans == 0)
      printf("Case #%d: INSOMNIA\n", i+1);
    else
      printf("Case #%d: %d\n", i+1, ans);
  }

  return 0;
}

