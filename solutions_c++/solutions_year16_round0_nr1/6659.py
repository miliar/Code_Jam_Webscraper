#include <iostream>
#define s(n) scanf("%d", &n)
#include <cstring>
#define fill(a, v) memset(a, v, sizeof a)
typedef long long ll;

int cs;
int mask = 0;

bool isOk(int val) {

	while(val > 0) {
		int dig = val % 10;
		mask |= 1<<dig;
		val /= 10;
	}
	return mask == (1<<10)-1;
}

int main() {
	int cases, N;
	s(cases);
	while(cases-- > 0) {
		mask = 0;
		s(N);
		int val = 0;
		int till = 100*N;
		bool found = false;
		for(int i=1;i<=till && !found;i++) {
			val += N;
			if (isOk(val)) {
				found = true;
				break;
			}
		}

		if(found) {
			printf("Case #%d: %d\n", ++cs, val);
			continue;
		}
		printf("Case #%d: INSOMNIA\n", ++cs);
	}
	return 0;
}
