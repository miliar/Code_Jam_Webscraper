#include <stdio.h>
#include <math.h>

int cal(char str[][10],int i,int j){
	int k = 0;
	for(k = 0; k < 4; k++){
		if(str[i][k] == str[i][j] ||str[i][k] == 'T')
			continue;
		else
			break;
	}
	if (k == 4)
		return 1;
	for(k = 0; k < 4; k++){
		if(str[k][j] == str[i][j] ||str[k][j] == 'T')
			continue;
		else
			break;
	}
	if (k == 4)
		return 1;

	if( i == j){
		for(k = 0; k < 4; k++){
			if(str[k][k] == str[i][j] ||str[k][k] == 'T')
				continue;
			else
				break;
		}
		if (k == 4)
			return 1;
	}

	if( i + j == 3){
		for(k = 0; k < 4; k++){
			if(str[k][3-k] == str[i][j] ||str[k][3-k] == 'T')
				continue;
			else
				break;
		}
		if (k == 4)
			return 1;
	}
	return 0;
}

char str[10][10];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,bo,s;
	scanf("%d",&t);
	for(int k = 1; k <= t; k++){
		bo = 0;
		s = 1;
		for(int i = 0; i < 4; i++)
			scanf("%s",str[i]);
		for(i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(str[i][j] != '.' && str[i][j] != 'T'
					&& cal(str,i,j) ){
					if(str[i][j] == 'X')
						bo = 1;
					else
						bo = -1;
					break;
				}
				if (str[i][j] == '.')
					s = 0;
			}
			if (bo)
				break;
		}
		if (bo == 0 && s == 0)
			printf("Case #%d: Game has not completed\n",k);
		else if(bo == 0 && s == 1)
			printf("Case #%d: Draw\n",k);
		else if (bo == 1)
			printf("Case #%d: X won\n",k);
		else
			printf("Case #%d: O won\n",k);
	}
}