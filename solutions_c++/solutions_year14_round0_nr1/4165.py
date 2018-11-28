#include <stdio.h>
#include <string.h>

int main() {
	int t;
	scanf("%d", &t);
	
	int answer;
	int row[4];
	bool ok[4];
	int matriz[4][4];
	
	for(int tt=1; tt<=t; tt++) {
		scanf("%d", &answer);
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				scanf("%d", &matriz[i][j]);
			}
		}
		for(int i=0; i<4; i++) {
			row[i] = matriz[answer-1][i];
		}
		
		scanf("%d", &answer);
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				scanf("%d", &matriz[i][j]);
			}
		}
		
		memset(ok, false, sizeof(ok));
		int cont = 0;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) if(matriz[answer-1][j] == row[i]) {
				ok[i] = true;
				cont++;
			}
		}
		
		printf("Case #%d: ", tt);
		if(cont == 0) {
			printf("Volunteer cheated!\n");
		} else if(cont > 1) {
			printf("Bad magician!\n");
		} else {
			for(int i=0; i<4; i++) if(ok[i]) {
				printf("%d\n", row[i]);
				break;
			}
		}
	}
}
