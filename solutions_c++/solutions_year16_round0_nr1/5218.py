#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	
	bool saw[10];

	int int_cnt;
	
	long long n, x, t, j;

	scanf("%lld", &x);

	for (long long i = 0; i < x; ++i) {

		scanf("%lld", &n);
		
		if (n == 0) printf("Case #%lld: INSOMNIA\n", i+1);

		else { 
			int_cnt = 0;

			for (j = 0; j < 10; ++j) saw[j] = false;
		
			j = 0;

			while (int_cnt < 10) {

				t = n * (++j);
					
				while (t > 0) {
	
					if (!saw[t % 10]) {
	
						saw[t % 10] = true;
					
						++int_cnt;

					}

					t /= 10;

				}

			}

			printf("Case #%lld: %lld\n", i+1, n*j);

		}

	}

	return 0;


}
