#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
typedef long long i64;
using namespace std;

inline int Calc(i64 x) {
	int y = 0;
	for (; x; x /= 10) 
		y |= 1 << (x % 10);
	return y;
}

int main() {

	int tcase; 
	scanf("%d", &tcase);
	int full = (1<<10)-1;
	for (int i = 1; i <= tcase; ++i) {
		i64 x;
		scanf("%lld", &x);
		int y = Calc(x);
		i64 t = x;
		for (; y != full && x; x += t, y |= Calc(x));
		printf("Case #%d: ", i);
		if (x) printf("%lld\n", x);
		else puts("INSOMNIA");
	}

	return 0;
}
