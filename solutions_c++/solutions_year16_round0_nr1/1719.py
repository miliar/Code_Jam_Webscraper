#include <stdio.h>
#include <set>

using namespace std;

int main(){
  int T;
  scanf("%d", &T);
  long n, curr;
  long k;
  set <long> seen;
  for (int t = 0; t < T; t++){
    scanf("%ld", &n);
    if (n == 0){
      printf("Case #%d: INSOMNIA\n", t+1);
    }
    else{
      seen.clear();
      //printf("seen.size(): %d\n", seen.size());
      k = 1;
      while (true){
	curr = n * k;
	while (curr / 10 >= 1){
	  seen.insert(curr % 10);
	  curr = curr / 10;
	}
	seen.insert(curr);
	if (seen.size() == 10){
	  printf("Case #%d: %ld\n", t+1, k * n);
	  break;
	} 
	k++;
      }
    }
  }
  return 0;
}
