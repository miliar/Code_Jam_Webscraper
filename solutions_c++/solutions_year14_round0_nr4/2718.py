#include<stdio.h>
#include<algorithm>

using namespace std;

void print_blocks(double* arr, int size){
	for(int i=0; i<size; i++){
		printf("%lf ", arr[i]);
	}
	printf("\n");
	return;
}

int main(void){
	int test_case;
	scanf("%d", &test_case);

	int case_count=1;

	while(test_case--){
		int block_num;
		int naomi_win_count=0;
		int ken_win_count=0;

		double naomi_block[10000]={};
		double ken_block[10000]={};
		double cp_naomi_block[10000]={};
		double cp_ken_block[10000]={};

		scanf("%d", &block_num);

		for(int i=0; i<block_num; i++){
			scanf("%lf", &naomi_block[i]);
			cp_naomi_block[i]=naomi_block[i];
		}
		for(int i=0; i<block_num; i++){
			scanf("%lf", &ken_block[i]);
			cp_ken_block[i]=ken_block[i];
		}

		sort(naomi_block, naomi_block+block_num);
		sort(ken_block, ken_block+block_num);
		sort(cp_naomi_block, cp_naomi_block+block_num);
		sort(cp_ken_block, cp_ken_block+block_num);

		for(int i=block_num-1; i>=0; i--){
			for(int j=block_num-1; j>=0; j--){
				if(naomi_block[i] > ken_block[j]){
					ken_block[j]=1.0;
					naomi_win_count++;
					break;
				}
			}
		}
		
		for(int i=block_num-1; i>=0; i--){
			for(int j=block_num-1; j>=0; j--){
				if(cp_ken_block[i] > cp_naomi_block[j]){
					cp_naomi_block[j]=1.0;
					ken_win_count++;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n", case_count++, naomi_win_count, block_num-ken_win_count);
	}
	return 0;
}