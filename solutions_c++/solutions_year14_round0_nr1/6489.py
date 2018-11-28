#include <stdio.h>

int main(void) {
	
	int num;
	fscanf(stdin, "%d", &num);
	//printf("num = %d\n", num);
	
	for (int i = 0; i < num; ++i) {
		int r1;
		fscanf(stdin, "%d", &r1);
		//printf("r1 = %d\n", r1);
		
		int dummy;
		int d1[4];
		int j;
		for (j = 0; j < r1; ++j) {
			fscanf(stdin, "%d %d %d %d", &d1[0], &d1[1], &d1[2], &d1[3]);
		}
		for ( ; j < 4; ++j) {
			fscanf(stdin, "%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
		}
		//printf("d1 = %d %d %d %d\n", d1[0], d1[1], d1[2], d1[3]);

		int r2;
		fscanf(stdin, "%d", &r2);
		//printf("r2 = %d\n", r2);

		int d2[4];
		for (j = 0; j < r2; ++j) {
			fscanf(stdin, "%d %d %d %d", &d2[0], &d2[1], &d2[2], &d2[3]);
		}
		for ( ; j < 4; ++j) {
			fscanf(stdin, "%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
		}
		//printf("d2 = %d %d %d %d\n", d2[0], d2[1], d2[2], d2[3]);
		
		int a = -1;
		int c = 0;
		for (j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				if (d1[j] == d2[k]) {
					a = d1[j];
					++c;
				}
			}
		}
		if (c == 1) {
			printf("Case #%d: %d\n", i + 1, a);
		}
		else if (c == 0) {
			printf("Case #%d: Volunteer cheated!\n", i + 1);
		}
		else {
			printf("Case #%d: Bad magician!\n", i + 1);
		}
	}
	
}

