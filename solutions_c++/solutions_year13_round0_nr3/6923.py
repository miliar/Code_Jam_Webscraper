#include<algorithm>
#include<iostream>
#include<cstdio>
#include<string>
#include<math.h>
using namespace std;

int main() {
  freopen("C-small-attempt1.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T;
  scanf("%d", &T);
  int A, B;

  for (int i = 1; i <= T; i++) {

    scanf("%d", &A);
    scanf("%d", &B);
    int AA = (int) (sqrt ( (double) A ));
    int BB = (int) (sqrt ( (double) B ));
    int counter = 0;

    while ( AA <= BB ) {
      int base = AA;
      int reverse = 0;
      while ( base > 0 ) {
	reverse = reverse * 10 + base % 10;
	base = base / 10;
      }
      if (AA == reverse) {
	int square = AA * AA;
	int reverses = 0;
	while ( square > 0 ) {
	  reverses = reverses * 10 + square % 10;
	  square = square / 10;
	}
	if ( AA * AA == reverses && reverses >= A && reverses <= B)
	  counter++;
      }
      AA++;
    }
    
    printf("Case #%d: %d\n", i, counter);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
