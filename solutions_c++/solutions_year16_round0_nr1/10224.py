#include<iostream>
#include<cstdio>
using namespace std;

int main(){
  int N;
  cin>>N;
  for(int i=1;i<=N;i++){
    long int num;
    scanf("%ld", &num);
    if (num == 0) {
      printf("Case #%d: INSOMNIA\n", i);
      continue;
    }
    int bucket = 0;
    int j;
    for (j = 1; bucket < 1023; j++){
      int temp = j * num;
      while(temp>0){
	int s = temp % 10;
        bucket |=  (1 << s) ;
	temp /= 10;
      }
    }
     printf("Case #%d: %ld\n", i, (j-1)*num);
   }
  return 0;
}
