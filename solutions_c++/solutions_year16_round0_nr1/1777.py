#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

bool check(bool* digits) {
	for(int i = 0; i < 10; i++) {
		if(!digits[i])
			return false;
	}
	return true;
}

int main() {

	int cases;
	scanf("%d", &cases);

	for(int i = 0; i < cases; i++) {

		long long val;
		scanf("%lld", &val);
		long long start = val;
		printf("Case #%d: ", i + 1);
		if(val == 0) {
			printf("INSOMNIA\n");
		} else {
			bool digits[10];
			for(int i = 0; i < 10; i++)
				digits[i] = false;
			while(!check(digits)) {
				long long copy = val;
				while(copy != 0) {
					int num = copy % 10;
					copy /= 10;
					digits[num] = true;
				}
				val += start;
			}
			val -= start;
			printf("%lld\n", val);
		}

		
	}

}