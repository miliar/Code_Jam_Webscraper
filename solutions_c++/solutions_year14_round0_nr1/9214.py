#include <cstdio>

int N;
int card1[4][4];
int card2[4][4];
int guess1;
int guess2;

void f(int number){
	int candidate[4];
	for(int i = 0;i < 4;i++){
		candidate[i] = card1[guess1-1][i];
	}
	int cnt = 0;
	int answer = -1;
	for(int i = 0;i < 4;i++){
		for(int j = 0;j < 4;j++){
			if(candidate[i] == card2[guess2-1][j]){
				cnt += 1;
				answer = candidate[i];
			}
		}
	}
	if(cnt == 1){
		printf("Case #%d: %d\n",number,answer);
	}else if(cnt > 1){
		printf("Case #%d: Bad magician!\n",number);
	}else{
		printf("Case #%d: Volunteer cheated!\n",number);
	}
}

int main(){
	scanf("%d\n",&N);
	for(int i = 0;i < N;i++){
		scanf("%d\n",&guess1);
		for(int y = 0;y < 4;y++){
			for(int x = 0;x < 4;x++){
				scanf("%d",&card1[y][x]);
			}
		}

		scanf("%d\n",&guess2);
		for(int y = 0;y < 4;y++){
			for(int x = 0;x < 4;x++){
				scanf("%d",&card2[y][x]);
			}
		}

		f(i+1);
	}
}
