// code jam 2016 problem 3
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

#define MAX 1001

int main(int argc, char ** argv)
{
	int t;

	scanf_s("%d", &t);
	int heights[2501];

	for (int n = 0; n < t; n++) {
		for (int i = 0; i < 2501; i++){
			heights[i] = 0;
		}

		int size;
		int height;
		scanf_s("%d", &size);

		for (int i = 1; i < size * 2; i++){
			for (int j = 0; j < size; j++){
				scanf_s("%d", &height);
				heights[height] += 1;
			}
		}

		printf("Case #%d:", n+1);
		for (int i = 0; i < 2501; i++){
			if (heights[i] % 2 == 1){
				printf(" %d", i);
			}
		}
		printf("\n");
	}

	return 0;
}

