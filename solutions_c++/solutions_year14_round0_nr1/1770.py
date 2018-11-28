#include <stdio.h>

void solve(){
	int i, j, l1, l2;
	int dummy, count=0;
	short flag[17];

	for(i=1;i<17;i++)
		flag[i] = 0;

	scanf("%d", &l1);
	l1--;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			scanf("%d", &dummy);
			if(i==l1)
				flag[dummy] = 1;
		}
	}

	scanf("%d", &l2);
	l2--;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			scanf("%d", &dummy);
			if(i==l2){
				count += flag[dummy];
				flag[dummy]++;
			}
		}
	}

	if(count > 1)
		printf("Bad magician!");
	else if (count == 0)
		printf("Volunteer cheated!");
	else if (count == 1){
		for(i=1;i<17;i++){
			if(flag[i]==2){
				printf("%d", i);
				break;
			}
		}
	}
}

int main(int argc, char *argv[]){
	int i, t;
	scanf("%d", &t);
	for(i=0;i<t;i++){
		printf("Case #%d: ", i+1);
		solve();
		printf("\n");
	}
	return 0;
}
