#include <stdio.h>

void flip(char * full, int place) {
	char taken[100];

	for (int i=0; i<=place; i++) {
		taken[i]=full[i];
	}

	for (int i=0; i<=place; i++) {
		if (taken[i]=='-') {
			full[place-i]='+';
		} else {
			full[place-i]='-';
		}
	}
}

int main() {
	
	int cccc;
	char in[100][100], in2[100], numvals;

	scanf_s("%d", &numvals);

	for (int i=0; i<numvals; i++) {
		scanf_s("%50s", in[i], sizeof(in[i]));
	}

	printf("\n");

	for (int i=0; i<numvals; i++) {
		char ins[100];
		int count=0;

		for (int b=10; b>=0; b--) {
			if (in[i][b]=='-') {
				if (in[i][0]=='+') {
					for (int c=0; c<99; c++) {
						if (in[i][c]=='-') {
							flip(in[i],c-1);
							c=99;
						}
					}
					flip(in[i],b);

					count+=2;
				} else {
					flip(in[i],b);

					count++;
				}
				b=99;
			}
		}

		printf("Case #%d: %d \n", i+1, count);
	}

	scanf_s("%d", &cccc);
}