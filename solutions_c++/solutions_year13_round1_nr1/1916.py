#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

int N;

class algorithm
{

public:
void solution(char *input, char *output);

/* You can add your own class functions, 
but main function call "solution" function only. */

};

void algorithm::solution(char *input, char *output){

	FILE *ifp, *ofp;

	ifp = fopen(input, "r");
	ofp = fopen(output, "w");

	if (ifp == NULL || ofp == NULL)
		return;

	int C;
	unsigned long long int r, t;
	fscanf (ifp, "%d\n", &C);

	for (int i = 1; i <= C; i++)
	{
		unsigned long count = 0;
		unsigned long long curp = 0, totp = 0;

		fscanf (ifp, "%llu %llu\n", &r, &t);

		while(1)
		{
			curp = (r << 1) + 1;
			r += 2;
			if (curp > t)
				break;

			t = t - curp;
			totp += curp;
			count++;
		}

		fprintf (ofp, "Case #%d: %lu\n", i, count);
	}
	fclose(ifp);
	fclose(ofp);
}


/* You can add your own functions, 
but main function call "solution" function only. */

int main (int argc, char *argv[])
{
	algorithm alg;
	alg.solution(argv[1], argv[2]);
	return 0;
}