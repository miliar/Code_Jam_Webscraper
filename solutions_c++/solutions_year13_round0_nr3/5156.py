#include <stdio.h>

int integerLogBase2(long int v) {
	int r = 0; // r will be lg(v)

	while (v >>= 1) // unroll for more speed...
	{
		  r++;
	}
	return r;
}

int integerLogBase10(long int v) {
  int r;          // result goes here
  int t;          // temporary

  static long int const PowersOf10[] = 
	      {1, 10, 100, 1000, 10000, 100000,
			       1000000, 10000000, 100000000, 1000000000,
				   10000000000, 100000000000, 1000000000000,
		  10000000000000, 100000000000000, 1000000000000000, 10000000000000000};

  t = (integerLogBase2(v) + 1) * 1233 >> 12; // (use a lg2 method from above)
  r = t - (v < PowersOf10[t]);
  return r;
}

bool isPalindrome(long int v) {
	int digits[15];
	int d, i = 0;

	digits[0] = v % 10;
	while (v /= 10) {
		digits[++i] = v % 10;
	}

	for (d = 0; d <= i/2; d++) {
		if (digits[d] != digits[i-d]) return false;
	}
	return true;
}


int main(int argc, char *argv[]) {
	int T;
	long int A, B;
	int lA, lB;

	scanf("%d", &T);

	int t,i,count;
	long int p,a,b,c,d,pp;
	for (t = 1; t <= T; t++) {
		count = 0;

		scanf("%ld %ld", &A, &B);

		lA = integerLogBase10(A) / 2;
		lB = (integerLogBase10(B) / 2) + 1;

		for (i = lA; i <= lB; i++) {
			switch (i) {
				case 7:
					for (a = 1; a <= 9; a++) {
						for (b = 0; b <= 9; b++) {
							for (c = 0; c <= 9; c++) {
								for (d = 0; d <= 9; d++) {
									p = 1000001 * a + 100010 * b + 10100 * c + 1000 *d;
									pp = p*p;
									if (A <= pp && pp <=B && isPalindrome(pp)) count++;
								}
							}
						}
					}
				break;
				case 6:
					for (a = 1; a <= 9; a++) {
						for (b = 0; b <= 9; b++) {
							for (c = 0; c <= 9; c++) {
								p = 100001 * a + 10010 * b + 1100 * c;
								pp = p*p;
								if (A <= pp && pp <=B && isPalindrome(pp)) count++;
							}
						}
					}
				break;
				case 5:
					for (a = 1; a <= 9; a++) {
						for (b = 0; b <= 9; b++) {
							for (c = 0; c <= 9; c++) {
								p = 10001 * a + 1010 * b + 100 * c;
								pp = p*p;
								if (A <= pp && pp <=B && isPalindrome(pp)) count++;
							}
						}
					}
				break;
				case 4:
					for (a = 1; a <= 9; a++) {
						for (b = 0; b <= 9; b++) {
							p = 1001 * a + 110 * b;
							pp = p*p;
							if (A <= pp && pp <=B && isPalindrome(pp)) count++;
						}
					}
				break;
				case 3:
					for (a = 1; a <= 9; a++) {
						for (b = 0; b <= 9; b++) {
							p = 101 * a + 10 * b;
							pp = p*p;
							if (A <= pp && pp <=B && isPalindrome(pp)) count++;
						}
					}
				break;
				case 2:
					for (a = 1; a <= 9; a++) {
						p = 11 * a;
						pp = p*p;
						if (A <= pp && pp <=B && isPalindrome(pp)) count++;
					}
				break;
				case 1:
					for (a = 1; a <= 9; a++) {
						pp = a*a;
						if (A <= pp && pp <=B && isPalindrome(pp)) count++;
					}
				break;
			}

		}

		printf("Case #%d: %d\n", t, count);
	}
}
