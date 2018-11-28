#include <cstdio>

//#define DEBUG
#ifdef DEBUG
	#define D(X) X
#else
	#define D(X)
#endif

int main() {

	int testCases;
	
	scanf("%d", &testCases);
	
	for (int testCase = 1; testCase <= testCases; ++testCase) {
		
		int maxShyness;
		char people[20000];
		int minimumAdditions = 0;

		scanf("%d %s\n", &maxShyness, people);

		D(printf("%d %s\n", maxShyness, people);)

		int totalPeople = 0;
		for (int i = 0; i <= maxShyness; ++i) {
			if (totalPeople < i) {
				minimumAdditions += i - totalPeople;
				totalPeople += i - totalPeople;
			}
			totalPeople += people[i] - '0';
			D(printf("total people = %d\n", totalPeople);)
		}

		printf("Case #%d: %d\n", testCase, minimumAdditions);

	}

	return 0;

}
