#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool isPrime(long long &a, long long &ret) {
	if (a <= 1) {
		return false;
	}
	else if (a <= 3) {
		return true;
	}
	else if ((a % 2) == 0) {
		ret = 2;
		return false;
	}else if((a % 3) == 0) {
		ret = 3;
		return false;
	}
	for (long long i = 5; i*i <= a; i+=6) {
		if ((a%i) == 0) {
			ret = i;
			return false;
		}
		else if ((a % (i + 2)) == 0) {
			ret = i+2;
			return false;
		}
	}
	return true;
}
int main() {
	int tc;
	int N = 6, J = 50;
	scanf("%d", &tc);
	scanf("%d%d", &N, &J);
	int anssize = 0;
	puts("Case #1:");
	for (int i = 0; i < (1 << (N-2)); i++) {
		bool sw = true;
		long long div[11];
		for (int base = 2; base <= 10; base++) {
			long long x = (1LL << (N-1)) + ((long long)i << 1) + 1;
			long long now = 1;
			long long val = 0;
			long long ret;
			while (x > 0LL) {
				if (x & 1LL) val += now;
				now *= base;
				x >>= 1;
			}
			if (isPrime(val, ret)) {
				sw = false;
				break;
			}
			else {
				div[base] = ret;
			}
		}
		
		if (sw) {
			anssize++;
			string s;
			long long v = (1LL << (N - 1)) + ((long long)i << 1) + 1;
			while (v > 0) {
				s.append(to_string(v & 1));
				v >>= 1;
			}
			reverse(s.begin(), s.end());
			printf("%s", s.c_str());
			for (int i = 2; i <= 10; i++) {
				printf(" %lld", div[i]);
			}
			puts("");
		}
		if (anssize >= J) break;
	}
	
	return 0;
}