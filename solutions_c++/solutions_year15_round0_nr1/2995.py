#include <stdio.h>

int T;
int S[1001];

int main(){

	FILE *fp = fopen("input.txt", "r");
	FILE *fp1 = fopen("output.txt", "w");
	fscanf(fp,"%d", &T);
	for (int testcase = 1; testcase <= T; testcase++){

		int S_max;
		int friend_num = 0;
		int human_num = 0;
		fscanf(fp, "%d", &S_max);
		for (int i = 0; i <= S_max; i++){
			fscanf(fp, "%1d", &S[i]);
		}
		for (int i = 0; i <= S_max; i++){
			if (human_num >= i){
				human_num += S[i];
			}
			else{
				friend_num += (i - human_num);
				human_num += (i - human_num);
				human_num += S[i];
			}
		}
		fprintf(fp1,"Case #%d: %d\n", testcase, friend_num);
	}
	return 0;
}