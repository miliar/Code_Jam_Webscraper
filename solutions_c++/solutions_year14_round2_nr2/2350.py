#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<vector>
#include<set>
#include<deque>

using namespace std;

int number;
unsigned int first,second,bound;


void run(){  
  scanf("%u", &first);
  scanf("%u", &second);
  scanf("%u", &bound);
  int result = 0;
  for(int i=0; i<first; ++i){
    for(int j=0; j<second; ++j){
      unsigned int res = i&j;
      if(res < bound){
	result++;
      }
    }
  }
  printf("%d", result);
}

int main(){
  scanf("%d", &number);
  for(int i=1; i<=number; ++i){
    printf("Case #%d: ", i);
    run();
    printf("\n");
  }
  return 0;
}
