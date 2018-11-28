#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LEN 100000	//������

FILE* fin;
FILE* fout;

//���� ���� �Լ�
void file_open(void);
//main ó�� �Լ�
void process(void);
//������ ������ ����
double findway(double C, double F, double X);

int main(void){
	
	file_open();
	
	process();
}

void file_open(void){
	if((fin = fopen("B-large.in", "r")) == NULL){
		printf("���� ���� ����\n");
		exit(-1);
	}

	if((fout = fopen("B-large.out", "w")) == NULL){
		printf("���� ���� ����\n");
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
	int farm = 0; //���� ���� 
	double cookie = 2; //�ʴ� ��� ����
	double* way = (double*)calloc(LEN, sizeof(double));//way �迭 �ε����� ���� ���� Ƚ���� ����
	double total = 0;	//�� �ҿ� �ð�
	double sub_time = 0;
	double min_time = 0;
	int farm_num = 0;
	//���� �ܼ��� ù��° ���
	way[farm++] = X/cookie;

	//������ �� ����?
	while(farm < LEN){
		//ù ��° ���� ���Ա��� �ɸ��� �ð�
		sub_time += C/cookie;
		//���� ����
		cookie += F;
		//���� 1 �����ϰ� �ɸ��� �ð�
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