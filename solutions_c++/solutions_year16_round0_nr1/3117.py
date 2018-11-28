#include <iostream>
#include <cstdio>
#include <cstring>  
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;
 
int main() {
	int cases;
	scanf("%d", &cases);
	for (int o = 0; o < cases; ++o) {
		int n, m = 0;
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", o + 1);
			continue;
		}
		long long ans = 0;
		while (m != (1 << 10) - 1) {
			ans += n;
			long long tmp = ans;
			while (tmp) {
				m |= (1 << (tmp % 10));
				tmp /= 10;
			}
		}
		printf("Case #%d: %lld\n", o + 1, ans);
	}
	return 0;
}


