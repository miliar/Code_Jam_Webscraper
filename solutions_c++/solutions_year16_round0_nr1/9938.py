#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <bitset>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <iostream>

using namespace std;
#define VARIABLE(x) cerr << #x << "=" << x << endl
#define BINARY(x) static_cast<bitset<16> >(x);
#define if_range(x, w, h) if (w <= x && x <= h)
#define BitCheck(a,b)   (a >> b) & 1
#define BitSet(a,b)       a |= (1 << b)
#define BitunSet(a,b)    a &= ~(1 << b)
#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b))
#define numof(array)  (sizeof (array) / sizeof *(array))

int main() {
	char num[7];
	int t;
	scanf("%d", &t);

	for (int i = 0; t > i; i++){
		int n,chs = {};
		long long int n_temp, n_tempt;
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i + 1);
			continue;
		}

		itoa(n, num, 10);

		for (int j = 1; chs != 1023; j++) {
			n_temp = n*j;
			n_tempt = n_temp;
			while (n_temp > 0) {
				BitSet(chs, n_temp % 10);
				n_temp = n_temp/10;
			}
		}
		printf("Case #%d: %lld\n", i+1, n_tempt);
	}
}