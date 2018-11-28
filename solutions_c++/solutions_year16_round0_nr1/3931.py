#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main() {
	int testcase;
	int N;
	bool visited[10];
	char numbers[23];
	bool isfinished;
	FILE *f = fopen("A-large.in", "r");
	FILE *fo = fopen("out_A2.txt", "w");
	fscanf(f, "%d", &testcase);
	for (int i = 1; i <= testcase; i++) {
		int j;
		fscanf(f,"%d", &N);
		for (j = 0; j < 10; j++)
			visited[j] = false;

		isfinished = false;
		for (j = 1; j < 200; j++) {
			itoa((N*j), numbers, 10);
			//printf("%s\n", numbers);
			for (int k = 0; k < strlen(numbers); k++) {
				visited[numbers[k] - 48] = true;
			}
			
			int finishvalue;
			for (finishvalue = 0; finishvalue < 10; finishvalue++) {
				if (!visited[finishvalue])
					break;
			}
			if (finishvalue == 10) {
				fprintf(fo,"Case #%d: %d\n", i, N*j);
				break;
			}
		}
		if (j == 200) {
			fprintf(fo,"Case #%d: INSOMNIA\n", i);
		}
	}
}