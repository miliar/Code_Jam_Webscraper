#include <cstdio>
#include <vector>
#include <cmath>

typedef unsigned long long ull;

bool is_palindrome(ull &n) {
	ull clone = n;
	ull reversed = 0;
	while (clone != 0) {
		reversed = reversed * 10 + clone % 10;
		clone /= 10;	
	}
	return (n == reversed);
}

inline bool check_square_check(ull &n) {
	ull sq = n*n;
	return (is_palindrome(n) && is_palindrome(sq));
}

int main() {
	std::vector <ull> memoizer;
	memoizer.assign(10000000,-1);
	ull n, m, end;
	int t, out;
	scanf("%d",&t);
	for (int i = 1; i <=t; ++i) {
		n = m = end = out = 0;
		scanf("%d %d", &n, &m);
		end = (ull) floor(sqrt(m));
		for (ull j = (ull) ceil(sqrt(n)); j<=end; ++j) {
		/*	if (memoizer[j] == 1) {
				++out;
			} else {
				memoizer[j] += check_square_check(j) + 1;
				out += memoizer[j];
			}
		*/
			out += check_square_check(j);
		}
		printf("Case #%d: %d\n", i, out);
	}
}
