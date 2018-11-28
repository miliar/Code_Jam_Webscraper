#include <stdio.h>

int main(void) {
	char people[2000];
	int T, Smax;
	int i, j;
	int stands;
	int friends;
	
	scanf("%d", &T);
	for(i = 0; i < T; i++) {
		scanf("%d %s", &Smax, &people);
		friends = 0;
		stands = 0;
		//Operation
		for(j = 0; j <= Smax; j++) {
			if(people[j] - 48 != 0) {	
				if(stands >= j) {
					stands += people[j] - 48;
				}
				else {
					friends += j - stands;
					stands += people[j] - 48 + j - stands;
				}
			}
		}
		printf("Case #%d: %d\n", i + 1, friends);
	}
}