#include<cstdio>
#include<cstdlib>
#include<cstring>

int compare(int *chp1, int *chp2){
	int cnt = 0;
	int match;
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(chp1[i] == chp2[j]){
				cnt++;
				match = chp1[i];
			}
			if(cnt > 1)
				return 17;
		}
	}

	if(cnt == 0)
		return 18;
	else
		return match;
}

int main(void){
	int T;
	int cards[4][4], cards2[4][4];
	int ch1, ch2, *chp1, *chp2;
	
	scanf("%d", &T);

	for(int i = 0; i < T; i++){
		scanf("%d", &ch1);
		for(int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++)
				scanf("%d", &cards[j][k]);
		chp1 = cards[ch1-1];

		scanf("%d", &ch2);
		for(int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++)				                                scanf("%d", &cards2[j][k]);
		chp2 = cards2[ch2-1];
		int result = compare(chp1, chp2);
		switch(result){
			case 17:
				printf("Case #%d: Bad magician!\n", i+1);
				break;
			case 18:
				printf("Case #%d: Volunteer cheated!\n", i+1);
				break;
			default:
				printf("Case #%d: %d\n", i+1, result);
		}

	}

	return 0;
}
