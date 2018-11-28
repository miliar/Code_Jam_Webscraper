#include <iostream>
#include <cstdio>
#include <cassert>

using namespace std;

static int shyness[1001];

int countNeeds(int max)
{
	int total = 0;
	int needs = 0;
	
	for(int i = 0; i <= max; i++) {
		if(total < i) {
			needs += i - total;
			total = i;
		}
		total += shyness[i];
	}

	return needs;
}

int main(void)
{
	int T;				// test case number
	int maxShyness=0;	// maximum shyness
	int result; 		// number of Si, result num
	char num;
	assert(scanf("%d", &T));
	for(int i = 0; i < T; i++) {
		assert(scanf("%d ", &maxShyness));
		for(int j = 0; j <= maxShyness; j++) {
			assert(scanf("%c", &num));
			num -= '0';
			shyness[j] = num;
		}
		result = countNeeds(maxShyness);
		printf("Case #%d: %d\n", i + 1, result);
	}
	return 0;           
}
