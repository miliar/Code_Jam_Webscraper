#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include<math.h>
#define sqr(i) ( i * i )

bool isPan(long long c) {
	char str[256];
	sprintf(str, "%d", c);
//	printf("Test: %s\n", str);
  int len = strlen(str);
  for (int i = 0; i < strlen(str) / 2; ++i) {
    if (str[i] != str[len - 1 - i]) {
      return false;
    }
  }
//  printf("\tA pan:%ld && sqrt: %f \n", c, sqrt(c));
  return true;
}
bool isPerfectSquare(long long c){
  double sc = sqrt(c);
  if (sc - floor(sc) < 1e-5 || ceil(sc) - sc < 1e-5) {
//    printf("Perfect sqrt: %lld, %f\n", c, sc);
    return true;
  }else {
    return false;
  }
}
//484
int calpansq(long long a, long long b) {
  int count = 0;
	for (long long i = a; i <= b ; ++i) {
		if(isPerfectSquare(i) && isPan(i) && isPan(sqrt(i))) {
      count ++;
//      printf("%d: %lld and %f\n", count, i, sqrt(i));
      
    }
	}
  return count;
}

int main(){
  int cases;
  scanf("%d", &cases);
  for (int i = 0; i < cases; ++i) {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    printf("Case #%d: %d\n", i + 1, calpansq(a, b));
  }
	
}