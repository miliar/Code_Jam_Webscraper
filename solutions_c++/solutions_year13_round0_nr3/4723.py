#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> palindromes;

bool isPalindrome(long long x) {
	long long k = x;
	long long rev = 0;
	while (k) {
		rev *= 10;
		rev += k % 10;
		k /= 10;
	}
	return rev == x;
}

void generate() {
	for (int i = 1; i <= 31622776; i++) {
		if (!isPalindrome(((long long)i))) {
			continue;
		}
		long long val = i * (i + 0LL);
		if (isPalindrome(val)) {
			palindromes.push_back(val);
		}
	}
	fprintf(stderr, "(%d)\n", palindromes.size());
}

int main() {
	generate();
	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; i++) {
		long long a, b;
		scanf("%lld %lld", &a, &b);
		int posA = -1;
		int posB = -1;
		for (int j = 0; j < palindromes.size(); j++) {
			if (palindromes[j] >= a and posA == -1) {
				posA = j;
			}
			if (palindromes[j] > b and posB == -1) {
				posB = j;
				break;
			}
		}
		//int posA = lower_bound(palindromes.begin(), palindromes.end(), a) - palindromes.begin();
		//int posB = upper_bound(palindromes.begin(), palindromes.end(), b) - palindromes.begin();
		printf("Case #%d: %d\n", i, posB - posA);
	}
	return 0;
}