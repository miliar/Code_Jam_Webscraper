#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LEN 100000	//가짓수

FILE* fin;
FILE* fout;

//파일 오픈 함수
void file_open(void);
//main 처리 함수
void process(void);
//가능한 가짓수 저장
double findway(double C, double F, double X);

int main(void){
	
	file_open();
	
	process();
}

void file_open(void){
	if((fin = fopen("B-large.in", "r")) == NULL){
		printf("파일 오픈 에러\n");
		exit(-1);
	}

	if((fout = fopen("B-large.out", "w")) == NULL){
		printf("파일 오픈 에러\n");
		exit(-1);
	}
}

void process(void){
	int T = 0;

	fscanf(fin, "%d", &T);

	for(int i = 0; i < T; i++){
		double C = 0;
		double F = 0;
		double X = 0;
		double res = 0;

		fscanf(fin, "%lf %lf %lf\n", &C, &F, &X);

		res = findway(C, F, X);

		fprintf(fout, "Case #%d: %.7lf\n", i+1, res);
	}
}

double findway(double C, double F, double X){
	int farm = 0; //농장 갯수 
	double cookie = 2; //초당 쿠기 갯수
	double* way = (double*)calloc(LEN, sizeof(double));//way 배열 인덱스를 농장 구입 횟수로 하자
	double total = 0;	//총 소요 시간
	double sub_time = 0;
	double min_time = 0;
	int farm_num = 0;
	//가장 단순한 첫번째 방법
	way[farm++] = X/cookie;

	//농장이 몇 개지?
	while(farm < LEN){
		//첫 번째 농장 도입까지 걸리는 시간
		sub_time += C/cookie;
		//농장 도입
		cookie += F;
		//농장 1 도입하고 걸리는 시간
		min_time = way[farm-1];
		way[farm++] = X/cookie + sub_time;
		if(way[farm - 1] - min_time> 0){
			free(way);
			return min_time;
		}
	}

	/*min_time = way[0];

	for(int i = 1; i < LEN; i++){
		if(way[i] == 0)
			break;
		if(min_time > way[i])
			min_time = way[i];
	}*/
}