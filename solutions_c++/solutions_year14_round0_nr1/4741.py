#include <stdio.h>

int t, cases = 1, fa, sa, temp, res, i, j;
int first[20], second[20];
bool bad, cheat;

int main() {
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &fa);
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				scanf("%d ", &temp);
				first[temp] = i+1;
			}
		}
		scanf("%d", &sa);
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				scanf("%d ", &temp);
				second[temp] = i+1;
			}
		}
		res = 0;
		bad = false;
		cheat = true;
		for(i = 1; i < 17; i++) {
			if(first[i] == fa && second[i] == sa) {
				if(res == 0) {
					cheat = false;
					res = i;
				} else {
					bad = true;
				}
			}
		}
		if(!bad && !cheat) {
			printf("Case #%d: %d\n", cases++, res);
		} else if(bad && !cheat) {
			printf("Case #%d: Bad magician!\n", cases++);
		} else {
			printf("Case #%d: Volunteer cheated!\n", cases++);
		}
	}
	return 0;
}