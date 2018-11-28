#include <bits/stdc++.h>
#include <math.h>

using namespace std;

int main(int argc, char* argv[]) {
  //freopen("customtests.txt", "r", stdin);
  
  int T;
  scanf("%d", &T);
  for (int qq = 1; qq <= T; qq++) {
    long N;
    // input data starts
    scanf("%ld", &N);
	// input data ends

    printf("Case #%d: ", qq);
	fflush(stdout);
	//printf("N = %ld\n", N);
    
    int numberCheck = 0;
	long current;
	for (int i = 1; true; i++) {
		if (N == 0 ||
			log(N) + log(i) > 32) {
			printf("INSOMNIA\n");
			fflush(stdout);
			break;
		}
		current = N * i;
		//printf("N: %ld, current: %ld ", N, current);
		fflush(stdout);
		long checkCopy = current;
		do {
			numberCheck |= 1 << (checkCopy % 10);
			fflush(stdout);
			checkCopy = checkCopy / 10;
			if (checkCopy == 0) {
				break;
			}
		} while (true);
		//printf(" numberCheck = %02x\n", numberCheck);
		fflush(stdout);
		if (numberCheck == 0b1111111111) {
			printf("%ld\n", current);
			fflush(stdout);
			break;
		}
	}
	
	
  }
  
  return 0;
}
