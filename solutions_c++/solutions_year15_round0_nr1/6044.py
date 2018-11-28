#include<stdio.h>

FILE *ou = fopen("output.txt", "w");
int s[1010];
int total = 0;
int friends = 0;
int T;
int Smax;

void init(){
	int i;
	for (i = 0; i < 1010; i++)
		s[i] = -1;
	total = 0;
	friends = 0;
	Smax = 0;
}

int main(){
	int i;
	scanf("%d", &T);
	for (i = 0; i < T; i++){
		int j;
		init();
		char trash;
		scanf("%d%c", &Smax,&trash);
		for (j = 0; j <= Smax; j++){
			char temp;
			scanf("%c", &temp);
			s[j] = temp - '0';
			if (j == 0)
				total += s[0];
			else{
				if (j>total && s[j]>0){
					friends += j - total;
					total += j - total;
				}
				total += s[j];
			}
		}
		fprintf(ou,"Case #%d: %d\n", i+1, friends);
	}

	return 0;
}