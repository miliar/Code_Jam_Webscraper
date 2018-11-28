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

	for (int n = 0; n < t; n++) {
		char instr[MAX];
		scanf_s("%s", instr, MAX);

		char outstr[2 * MAX];

		int start = MAX-1;
		int end = MAX;

		size_t len = strlen(instr);
		outstr[start] = instr[0];

		for (int i = 1; i < (int)len; i++){
			if (outstr[start] <= instr[i]){
				outstr[start - 1] = instr[i];
				start--;
			}
			else {
				outstr[end] = instr[i];
				end++;
			}
		}

		strncpy_s(instr, MAX, outstr + start, len);

		printf("Case #%d: %s\n", n+1, instr);
	}

	return 0;
}

