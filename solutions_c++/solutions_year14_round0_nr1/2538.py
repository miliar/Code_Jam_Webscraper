#include<stdio.h>
FILE *in = fopen("A-small-attempt0.in", "r");
FILE *out= fopen("output.txt","w");
int main()
{
	int T;
	fscanf(in, "%d", &T);
	for(int testCase = 1; testCase <= T; testCase++){
		int card[2][4] = {0,}, r1, r2, tmp, c = 0;
		fscanf(in, "%d", &r1);
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(i+1 == r1)
					fscanf(in, "%d", &card[0][j]);
				else
					fscanf(in, "%d", &tmp);
			}
		}
		fscanf(in, "%d", &r2);
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(i+1 == r2)
					fscanf(in, "%d", &card[1][j]);
				else
					fscanf(in, "%d", &tmp);
			}
		}
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(card[0][i] == card[1][j]){
					c++;
					tmp = card[0][i];
				}
			}
		}
		if(c == 0){
			fprintf(out, "Case #%d: Volunteer cheated!\n", testCase);
		}
		else if(c == 1){
			fprintf(out, "Case #%d: %d\n", testCase, tmp);
		}
		else{
			fprintf(out, "Case #%d: Bad magician!\n", testCase);
		}
	}
	return 0;
}