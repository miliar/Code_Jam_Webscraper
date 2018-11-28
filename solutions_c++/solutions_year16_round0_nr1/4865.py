#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX_DINERS = 1005;

int testCases, num;

int main() {
	scanf("%d", &testCases);
	for(int t = 1; t <= testCases; t++) {
		scanf("%d", &num);
		if(num == 0) {
			printf("Case #%d: INSOMNIA\n", t);	
		} else {
			int seen = 0;
			int last_num = num, temp, d;

			while(true) {
				temp = last_num;
				while(temp > 0) {
					d = temp%10;
					if(!(seen & (1 << d))) {
						seen |= (1 << d);
					}
					temp /= 10;
				}
				if(seen == 1023) break;
				last_num += num;				
			}

			printf("Case #%d: %d\n", t, last_num);
		}		
	}
	return 0;
}