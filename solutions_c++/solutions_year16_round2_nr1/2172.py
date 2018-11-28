#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>

#define si() (scanf("%d", &TEMP), TEMP)
int TEMP;

#define max_S 2002
using namespace std;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	int ENG[30];
	int IN[10];
	char c;
	c = getchar();

	for(int i=0; i<T; i++){
		printf("Case #%d: ", i+1);

		for(int j=0; j<30; j++)
			ENG[j]=0;
		for(int j=0; j<10; j++)
			IN[j] = 0;

		while((c = getchar()) != '\n'){
			ENG[c-'A']++;
		}

		IN[0] = ENG[25];
		IN[2] = ENG[22];
		IN[6] = ENG[23];
		IN[8] = ENG[6];
		IN[3] = ENG[19] - IN[2] - IN[8];
		IN[4] = ENG[17] - IN[0] - IN[3];
		IN[1] = ENG[14] - IN[0] - IN[2] - IN[4];
		IN[5] = ENG[5] - IN[4];
		IN[7] = ENG[18] - IN[6];
        IN[9] = ENG[8] - IN[5] - IN[6] - IN[8];

        for(int j=0; j<10; j++){
			for(int k=0; k<IN[j]; k++)
				printf("%d", j);
        }

		printf("\n");
	}

	return 0;
}
