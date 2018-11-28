#include <cstdio>

const int maxN = 32;

int casei, cases;
int N, J;
long long primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997};

long long bases[11][40];


int main() {
	for (int base = 2; base <= 10; ++base) {
		bases[base][0] = 1LL;
		for (int i = 1; i <= maxN; ++i) 
			bases[base][i] = bases[base][i - 1] * (long long)base;
	}
	int primesLen = sizeof(primes)/sizeof(primes[0]);
	int tmpList[40];
	long long factors[11];
	
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d%d", &N, &J);
		printf("Case #%d:\n", casei);
		
		int cnt = 0;
		for (int now = 0; cnt < J; ++now) {
			int tmpLen = 0;
			for (int i = 0; ; ++i) {
				int tmp = 1 << i;
				if (tmp > now) break;
				if (tmp & now) tmpList[tmpLen++] = i + 1;
			}
			
			bool flag = true;
			for (int base = 2; flag && base <= 10; ++base) {
				long long num = bases[base][N - 1] + 1LL;
				for (int i = 0; i < tmpLen; ++i)
					num += bases[base][tmpList[i]];
				flag = false;
				for (int i = 0; !flag && i < primesLen; ++i)
					if (num % primes[i] == 0) {
						factors[base] = primes[i];
						flag = true;
					}
			}
			if (flag) {
				++cnt;
				printf("1");
				for (int i = N - 2, j = tmpLen - 1; i >= 1; --i) {
					if (j >= 0) {
						if (i == tmpList[j]) {
							printf("1");
							--j;
						}
						else printf("0");
					}
					else printf("0");
				}
				printf("1");
				for (int base = 2; base <= 10; ++base) printf(" %lld", factors[base]);
				printf("\n");
			}
		}
	}
	return 0;
}
