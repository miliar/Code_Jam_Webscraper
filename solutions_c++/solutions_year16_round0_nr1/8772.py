#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

bool Check[10];

bool checking(){
	for(int i = 0; i < 10; i ++){
		//printf("%d ", Check[i]);
		if(Check[i] == 0)
			return 0;
	}
	return 1;
}

int main(){
	FILE *f;
	FILE *fp;
	int tmp[7] = {1000000, 100000, 10000, 1000, 100, 10, 1};
	int T, i;
	int N;

	f = fopen("A-large.in", "r");
	fp = fopen("output2.txt", "w");
	fscanf(f, "%d", &T);
	
	for(i = 1; i <= T; i ++){
		fscanf(f, "%d", &N);
		if(N == 0)
			fprintf(fp, "Case #%d: INSOMNIA\n", i);
		else{
			int count, ori_N, ori_count = 2, Result;
			
			memset(Check, 0, sizeof(bool)*(10));

			ori_N = N;
			while(1){
				for(int j = 0; j < 7; j++){
					if(N/tmp[j] > 0){
						count = j;
						break;
					}
				}	
			//	printf("count : %d\n", count);
				for(int k = count; k < 7; k ++){
					if(N/tmp[k] >= 0){
						//printf("check => %d\n",N/tmp[k]);
						Check[N/tmp[k]] = 1;
					}
					//printf("rest : %d\n", N%tmp[k]);
					N%=tmp[k];
				}
				if(checking() == 0){
					N = ori_N*(ori_count++);
					Result = N;
				}else{
					fprintf(fp, "Case #%d: %d\n", i, Result);
					break;
				}
			//	printf("N : %d\n", N);
			}
		}
	}
}