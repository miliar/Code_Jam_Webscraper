#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE* fin;
FILE* fout;

//파일 오픈 함수
void file_open(void);
//main 처리 함수
void process(void);
//정답 확인 함수	
int compare_arr(int farr[][4], int sarr[][4], int fans, int sans);
//매지션 검증
int Bad_magician(int farr[][4], int sarr[][4]);
//자원봉사자 검증
int volunteer(int* arr1, int* arr2);

int main(void){
	
	file_open();
	
	process();
}

void file_open(void){

	if((fin = fopen("A-small-attempt3.in", "r")) == NULL){
		printf("파일 오픈 에러\n");
		exit(-1);
	}

	if((fout = fopen("A-small-attempt3.out", "w")) == NULL){
		printf("파일 오픈 에러\n");
		exit(-1);
	}

}

void process(void){
	int i;
	int T;
	int first_ans;
	int second_ans;
	int first[4][4];
	int second[4][4];
	int res;

	fscanf(fin, "%d", &T);

	for(i = 0; i < T; i++)
	{
		fscanf(fin, "%d", &first_ans);	
		//first arr
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				fscanf(fin, "%d", &first[j][k]);
			}
		}

		fscanf(fin, "%d", &second_ans);
		//second arr
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				fscanf(fin, "%d", &second[j][k]);
			}
		}

		res = compare_arr(first, second, first_ans, second_ans);

		switch(res){
		case -1:
			fprintf(fout, "Case #%d: Bad magician!\n", i+1);
			break;
		case 0:
			fprintf(fout, "Case #%d: Volunteer cheated!\n", i+1);
			break;
		default:
			fprintf(fout, "Case #%d: %d\n", i+1, res);
			break;
		}
	}
}

int compare_arr(int farr[][4], int sarr[][4], int fans, int sans){
	int ret = 1;
	int answer = -1;

	answer = volunteer(farr[fans-1], sarr[sans-1]);
	if(answer == 0)
		return 0;
	else if(answer == -1)
		return -1;

	ret = Bad_magician(farr, sarr);

	if(ret == -1)
		return -1;
	
	return answer;
}

int Bad_magician(int farr[][4], int sarr[][4]){
	int ret;

	//Bad magician
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(farr[i][j] != sarr[i][j]){
				return 1;
				break;
			}
		}	
	}

	return -1;
}

int volunteer(int* arr1, int* arr2){
	int corr = 0;
	int answer = 0;

	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(arr1[i] == arr2[j]){
				corr++;
				answer = arr1[i];
			}
		}
	}
	
	if(corr == 1)
		return answer;
	else if(corr > 1)
		return -1;
	else if(corr == 0)
		return 0;
}