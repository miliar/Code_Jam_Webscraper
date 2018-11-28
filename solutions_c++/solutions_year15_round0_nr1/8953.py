#include <stdio.h>


int minFriendInvited(char aud[], int Smax) {

	int friendsInvited = 0;

	int numberOfPeopleThatWillStand = aud[0] - '0'; 
	for (int i = 1; i <= Smax; i++) {
		int nWithi = aud[i] - '0';
		if (nWithi && i > numberOfPeopleThatWillStand) {
			friendsInvited += i - numberOfPeopleThatWillStand; 
			numberOfPeopleThatWillStand = i;
		}
		numberOfPeopleThatWillStand += nWithi;
	}

	return friendsInvited;
}

int main () {
	int N;
	char aud[1010];

	scanf("%d", &N);

	int counter = 1;
	while (counter <= N) {
		int Smax;

		scanf("%d %s", &Smax, aud);
		printf("Case #%d: %d\n",counter++, minFriendInvited(aud, Smax));

	}

	return 0;
}