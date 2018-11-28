#include <cstdio>

const int MAX = 1005;
int totalCases, sMax, totalFriendsBrought, friendsNeeded, peopleStanding;
char S[MAX];

int main() {
	scanf("%d", &totalCases);
	for(int t = 1; t <= totalCases; t++) {
		scanf("%d %s", &sMax, &S);
		
		for(int i = 0; i < sMax + 1; i++) {
			S[i] -= '0';
		}
		
		totalFriendsBrought = friendsNeeded = peopleStanding = 0;
		
		for(int minStanding = 0; minStanding < sMax + 1; minStanding++) {
			if(peopleStanding >= sMax) break;
			if(peopleStanding < minStanding) {
				friendsNeeded = (minStanding - peopleStanding);
				peopleStanding += friendsNeeded;
				totalFriendsBrought += friendsNeeded;
			}
			peopleStanding += S[minStanding];
		}

		printf("Case #%d: %d\n", t, totalFriendsBrought);
	}
	return 0;
}