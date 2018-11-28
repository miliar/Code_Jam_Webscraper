#include <cstdio>
#include <algorithm>
using namespace std;

int dinersWithPancakes[1001];

int solve(int maxPancakesInPlate) {
	int solution = maxPancakesInPlate;

	if (maxPancakesInPlate >= 4) {
		int dinersWithMaxPancakes = dinersWithPancakes[maxPancakesInPlate];

		dinersWithPancakes[maxPancakesInPlate] = 0;
		for (int p = 1; p <= maxPancakesInPlate / 2; p++) {
			dinersWithPancakes[p] += dinersWithMaxPancakes;
			dinersWithPancakes[maxPancakesInPlate - p] += dinersWithMaxPancakes;

			for (int i = maxPancakesInPlate - 1; i >= 0; i--) {
				if (dinersWithPancakes[i]) {
					solution = min(solution, dinersWithMaxPancakes + solve(i));
					break;
				}
			}

			dinersWithPancakes[p] -= dinersWithMaxPancakes;
			dinersWithPancakes[maxPancakesInPlate - p] -= dinersWithMaxPancakes;
		}
		dinersWithPancakes[maxPancakesInPlate] = dinersWithMaxPancakes;
	}

	return solution;
}

int main(void) {
	int numCases;

	scanf("%d\n", &numCases);
	for (int numCase = 1; numCase <= numCases; numCase++) {
		int nonEmptyDiners;
		int maxPancakesInPlate = 0;

		for (int i = 0; i <= 1000; i++) {
			dinersWithPancakes[i] = 0;
		}

		scanf("%d\n", &nonEmptyDiners);
		for (int i = 0; i < nonEmptyDiners; i++) {
			int pancakes;

			scanf("%d", &pancakes);
			dinersWithPancakes[pancakes]++;
			maxPancakesInPlate = max(pancakes, maxPancakesInPlate);
		}

		printf("Case #%d: %d\n", numCase, solve(maxPancakesInPlate));
	}
}