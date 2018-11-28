#include <stdio.h>

int main(){
	int i, j, k, cases, count=1;
	char input[4][4];
	scanf("%d", &cases);
	for(k=1;k<=cases;k++){
		int xrow[4]={0}, xcol[4]={0}, yrow[4]={0}, ycol[4]={0}, xslo[3]={0}, yslo[3]={0}, draw=0;
		getchar();
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				input[i][j] = getchar();
				switch(input[i][j]){
					case 'X':
						xrow[i]++;
						xcol[j]++;
						if(i==j)
							xslo[1]++;
						else if(i+j==3)
							xslo[2]++;
						break;
					case 'O':
						yrow[i]++;
						ycol[j]++;
						if(i==j)
							yslo[1]++;
						else if(i+j==3)
							yslo[2]++;
						break;
					case 'T':
						xrow[i]++;
						xcol[j]++;
						yrow[i]++;
						ycol[j]++;
						if(i==j){
							xslo[1]++;	yslo[1]++;
						}
						else if(i+j==3){
							xslo[2]++;	yslo[2]++;
						}
				}
			}
			getchar();
		}
		for(i=0;i<4;i++){
			if(xrow[i]==4||xcol[i]==4||xslo[1]==4||xslo[2]==4){
				printf("Case #%d: X won\n", count++);
				break;
			}
			else if(yrow[i]==4||ycol[i]==4||yslo[1]==4||yslo[2]==4){
				printf("Case #%d: O won\n", count++);
				break;
			}
		}
		if(count>k)
			continue;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++){
				if(input[i][j]=='T'){
					ycol[j]--;xcol[j]--;
					yrow[i]--;xrow[i]--;
					if(i==j){
						yslo[1]--;xslo[1]--;
					}
					else if(i+j==3){
						yslo[2]--;xslo[2]--;
					}
				}
			}
		for(i=0;i<4;i++){
			if(xrow[i]>=1&&yrow[i]>=1)
				draw++;
			if(xcol[i]>=1&&ycol[i]>=1)
				draw++;
		}
		for(i=1;i<=2;i++)
			if(xslo[i]>=1&&yslo[i]>=1)
				draw++;
		if(draw==10){
			printf("Case #%d: Draw\n", count++);
			continue;
		}
		printf("Case #%d: Game has not completed\n", count++);
	}
	return 0;
}
