#include <stdio.h>

int main() {
	int t, i, j, smax, no,friends[1000],temp;
	char instring[1000];
	scanf("%d",&t);
	for(i = 0; i < t; i++) {
		no = 0;
		friends[i] = 0;
		scanf("%d",&smax);
		scanf("%s",&instring);
		for(j = 0; j <= smax; j++) {
			temp = instring[j] - 48;
			if(temp != 0) {
				if (no < j) {
					friends[i] = friends[i] + j - no;
					no = no + friends[i];
				}
				no = no + temp;
			}
		}
	}
	for(i = 0; i < t; i++) {
		printf("Case #%d: %d\n",i+1,friends[i]);
}
	return 0;
}
