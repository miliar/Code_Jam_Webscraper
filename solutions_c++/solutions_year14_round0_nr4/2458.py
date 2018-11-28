#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

FILE* fin;
FILE* fout;

#define LEN 1000

typedef struct {
	double weigh[LEN];
	bool com[LEN];
}block;

//파일 오픈 함수
void file_open(void);
//main 처리 함수
void process(void);
//deceitful war에서 naomi가 얻을 수 있는 최적 포인트
int deceitful_war(block naomi, block ken, int len);
//정상적인 war에서 naomi가 얻을 수 있는 최적 포인트
int war(block naomi, block ken, int len);

bool desc (double i, double j) { return (j < i); }

bool asc (double i, double j) { return (j > i); }

int main(void){
	file_open();
	
	process();
}

void file_open(void){

	if((fin = fopen("D-large.in", "r")) == NULL){
		printf("파일 오픈 에러\n");
		exit(-1);
	}

	if((fout = fopen("D-large.out", "w")) == NULL){
		printf("파일 오픈 에러\n");
		exit(-1);
	}

}

void process(void){
	int T;

	fscanf(fin, "%d", &T);

	for(int i = 0; i < T; i++){
		int N = 0;
		block naomi;
		block ken;
		int d_opt = 0;
		int w_opt = 0;

		fscanf(fin, "%d", &N);

		for(int j = 0; j < N; j++){
			fscanf(fin, "%lf", &naomi.weigh[j]);
		}

		for(int j = 0; j < N; j++){
			fscanf(fin, "%lf", &ken.weigh[j]);
		}
		
		std::sort(naomi.weigh, naomi.weigh + N, desc);
		std::sort(ken.weigh, ken.weigh + N, desc);

		d_opt = deceitful_war(naomi, ken, N);

		std::sort(naomi.weigh, naomi.weigh + N, asc);
		std::sort(ken.weigh, ken.weigh + N, asc);

		w_opt = war(naomi, ken, N);

		fprintf(fout, "Case #%d: %d %d\n", i+1, d_opt, N-w_opt);
	}

}

int deceitful_war(block naomi, block ken, int len){
	int ret = 0;	//naomi score
	int j = 0;

	for(int i = 0; i < len ; i++){
		for(; j < len; j++){
			if(ken.com[j]){ //비교 안 한것이 모두 true
				if(naomi.weigh[i] > ken.weigh[j]){
					ken.com[j] = false;
					ret ++;
					break;
				}
			}
		}
		if(j == len)
			return ret;
	}

	return ret;
}
//ken이 최선을 다한 경우? 아니야
int war(block naomi, block ken, int len){
	int ret = 0;	//naomi score
	int j = 0;

	for(int i = 0; i < len ; i++){
		for(; j < len; j++){
			if(ken.com[j]){
				if(naomi.weigh[i] < ken.weigh[j]){
					ken.com[j] = false;
					ret ++;
					break;
				}
			}
		}
		if(j == len)
			return ret;
	}

	return ret;
}