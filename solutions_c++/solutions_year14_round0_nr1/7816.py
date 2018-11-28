#include<vector>
#include<cstdio>
using namespace std;

int firstArr[4][4];
int secondArr[4][4];

int main(){
	int tottcnt;
	scanf("%d", &tottcnt);
	for(int tt = 1; tt <= tottcnt; tt++){
		int row1;
		scanf("%d", &row1);
		for(int i = 0; i <4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &firstArr[i][j]);
		int row2;
		scanf("%d", &row2);
		for(int i = 0; i <4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &secondArr[i][j]);

		row1--; row2--;
		int cnt = 0;
		int answ = -1;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(firstArr[row1][i] == secondArr[row2][j]){
					cnt++;
					answ = firstArr[row1][i];
				}
			}
		}
		if(cnt == 1)
			printf("Case #%d: %d\n", tt, answ);
		else
			printf("Case #%d: %s\n", tt ,cnt > 1 ? "Bad magician!" : "Volunteer cheated!");
	}
}
