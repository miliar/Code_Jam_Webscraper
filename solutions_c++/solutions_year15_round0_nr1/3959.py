#include <cstdio>

int main(void) {
	int numCases;

	scanf("%d\n", &numCases);
	for (int numCase = 1; numCase <= numCases; numCase++) {
		int maxShynessLevel;
		int standingPeople = 0;
		int friendsToInvite = 0;

		scanf("%d ", &maxShynessLevel);
		for (int shynessLevel = 0; shynessLevel <= maxShynessLevel; shynessLevel++) {
			char peopleWithShynessLevel;

			scanf("%c", &peopleWithShynessLevel);
			if (peopleWithShynessLevel != '0') {
				int friendsNeeded = standingPeople >= shynessLevel ? 0 : shynessLevel - standingPeople;

				friendsToInvite += friendsNeeded;
				standingPeople += friendsNeeded + peopleWithShynessLevel - '0';
			}
		}

		printf("Case #%d: %d\n", numCase, friendsToInvite);
	}
}