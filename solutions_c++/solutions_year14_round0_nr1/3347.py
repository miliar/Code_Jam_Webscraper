#include <cstdio>
#include <cstring>

int main() {
	int t, tc, i, j, r1, r2, a, cnt, sol;
	
	int card[20];
	
	scanf("%d",&tc);
	for(t=1;t<=tc;t++) {
		memset(card, 0, sizeof(card));
		scanf("%d",&r1);
		for(i=1;i<=4;i++) {
			for(j=1;j<=4;j++) {
				scanf("%d",&a);
				if(i != r1) card[a] = 1;
			}
		}
		scanf("%d",&r2);
		for(i=1;i<=4;i++) {
			for(j=1;j<=4;j++) {
				scanf("%d",&a);
				if(i != r2) card[a] = 1;
			}
		}
		cnt = 0;
		for(i=1;i<=16;i++) {
			if(!card[i]) {
				cnt++;
				sol = i;
			}
		}
		printf("Case #%d: ",t);
		if(cnt == 0) {
			printf("Volunteer cheated!\n");
		} else if(cnt == 1) {
			printf("%d\n", sol);
		} else {
			printf("Bad magician!\n");
		}
	}
	
	return 0;
}
