#include <iostream>
#include <cstdio>
#define lli long long int
using namespace std;

int main() {
	// your code goes here
	lli a,b,k,tcase,i,j,k1,count,count1;
	
	scanf("%lld", &tcase);
	
	count1 = 1;
	
	while (count1 <= tcase) {
		scanf("%lld%lld%lld", &a, &b, &k);
		count = 0;
		
		for (i = 0; i < a; ++i) {
			for (j = 0; j < b; ++j) {
				if ((i & j) < k)
					++count;
			}
		}
		
		printf("Case #%lld: %lld\n", count1, count);
		++count1;
	}
	return 0;
}