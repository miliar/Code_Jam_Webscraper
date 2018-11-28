#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include <algorithm>

#define LL long long
#define LD long double
#define FM(i,a,b) for(int i=a;i<b;i++) //(b-a) times a ~ b-1
#define PROBLEM_T "A"
#define INPUT_T "large"
#define FP_1 fp1
#define FP_2 fp2
#define FILE_OPEN() FILE *FP_1,*FP_2;char name1[50],name2[50],P_T[]= PROBLEM_T ,I_T[]=INPUT_T ;\
sprintf(name1, "%s-%s.in",P_T,I_T);\
sprintf(name2,"%s-%s.out" ,P_T,I_T);\
FP_1=fopen(name1,"r" );FP_2=fopen(name2, "w")// open file
#define FILE_CLOSE() fclose(FP_1);fclose( FP_2) //close file
#define D_INPUT_A(x) int x;fscanf( FP_1, "%d " ,&x)
#define D_INPUT_B(x,y) int x; int y;fscanf(FP_1 ,"%d %d " ,&x,&y)
#define D_INPUT_C(x,y,z) int x;int y;int z;fscanf( FP_1, "%d %d %d " ,&x,&y,&z)
#define INPUT_A(x) fscanf(FP_1,"%d ",&x)
#define INPUT_B(x,y) fscanf(FP_1,"%d %d ",&x,&y)
#define INPUT_C(x,y,z) fscanf(FP_1,"%d %d %d ",&x,&y,&z)
#define INPUT_STR(x) fscanf(FP_1,"%s ",x)
#define OUTPUT(x) fprintf(FP_2,"Case #%d: %d\n",n+1,x)
#define OUTPUT_B(x,y) fprintf(FP_2,"Case #%d: %d %d\n",n+1,x,y)
#define OUTPUT_STR(x) fprintf(FP_2,"Case #%d: %s\n",n+1,x)
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

const LD EPS = 1e-10;
const LD PI = acos(-1.0);

char input[1005];
char answer[1005];

void get_answer() {
	int i = 1;
	answer[0] = input[0];
	while (input[i] != '\0') {
		if (input[i] >= answer[0]) {
			memmove(answer + 1, answer, i);
			answer[0] = input[i];
		}
		else {
			answer[i] = input[i];
		}
		i++;
	}
	answer[i] = '\0';
}

int main() {
	FILE_OPEN();

	D_INPUT_A(T);
	FM(n, 0, T) {
		INPUT_STR(input);
		get_answer();
		OUTPUT_STR(answer);
	}
	FILE_CLOSE();
	return 0;
}
