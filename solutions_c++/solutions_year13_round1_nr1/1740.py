#include <iostream>
#include <stdio.h>
using namespace std;

#define RT freopen("a.in", "r", stdin)
#define WT freopen("b.out", "w", stdout)


int main() {
	RT, WT;
	int cases, R, T; cin >> cases;
	for(int c = 0; c < cases; ++c) {
		cin >> R >> T;
		int sum = 0, i = 1, res = 0;
		while(1) {
			sum += ((i + R) * (i + R)) - ((i - 1 + R) * (i - 1 + R));
			//cout << sum << " " << res << endl;
			if(sum > T) break;
			i += 2;
			++res;
		}
		printf("Case #%d: %d\n", c + 1, res);
	}
	return 0;
}