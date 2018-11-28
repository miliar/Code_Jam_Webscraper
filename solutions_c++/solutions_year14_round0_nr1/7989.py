#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t, i, j, k;
	int row;
	
	int a[5], b[5];
	
	scanf("%d", &t);
	
	for(int kase=1; kase<=t; kase++) {
		
		scanf("%d", &row);
		
		for(i=0; i<4; i++) {
			if(i+1 == row) {
				for(j=0; j<4; j++)
					scanf("%d", &a[j]);
			} else {
				for(j=0; j<4; j++)
					scanf("%d", &k);
			}
		}
		
		scanf("%d", &row);
		
		for(i=0; i<4; i++) {
			if(i+1 == row) {
				for(j=0; j<4; j++)
					scanf("%d", &b[j]);
			} else {
				for(j=0; j<4; j++)
					scanf("%d", &k);
			}
		}
		
		int match = 0, index;
		
		for(i=0; i<4; i++) {
			for(j=0; j<4; j++) {
				if(a[i] == b[j]) {
					index = i;
					match++;
				}
			}
		}
		
		if(match == 0) {
			printf("Case #%d: Volunteer cheated!\n", kase);
		} else if(match == 1) {
			printf("Case #%d: %d\n", kase, a[index]);
		} else {
			printf("Case #%d: Bad magician!\n", kase);
		}
	}
	
	return 0;
}