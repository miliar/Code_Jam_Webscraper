#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int TC, v1, v2;
	int a1[5][5], a2[5][5];
	int t, i, j, match[5], count;
	
	scanf("%d", &TC);
	for(t=1; t<=TC; t++) {

		scanf("%d", &v1);
		for(i=1; i<=4; i++) {
			for(j=1; j<=4; j++) {
				scanf("%d", &a1[i][j]);
			}
		}

		scanf("%d", &v2);
		for(i=1; i<=4; i++) {
			for(j=1; j<=4; j++) {
				scanf("%d", &a2[i][j]);
			}
		}

		count = 0;
		for(i=1; i<=4; i++) {
			match[i] = 0;
			for(j=1; j<=4; j++) {
				if(a1[v1][i] == a2[v2][j]) {
					count++;
					match[i] = a1[v1][i];
				}
			}
		}
		
		if(count == 0) {
			printf("Case #%d: Volunteer cheated!\n", t);
		}
		else if(count == 1) {
			for(i=1; i<=4; i++) {
				if(match[i] != 0) {
					break;
				}
			}
			printf("Case #%d: %d\n", t, match[i]);
		}
		else {
			printf("Case #%d: Bad magician!\n", t);
		}
	}
	return 0;
}