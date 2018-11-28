#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

#define MAX 105
int T;
char S[MAX];
int D[MAX][2];
int main() {
	// insert code here...

	FILE *in, *out;
	in = fopen("B-large.in", "r");
	out = fopen("result.out", "w");

	D[0][0] = 0;  // µÞÀÚ¸®°¡ +
	D[0][1] = 1;  // µÞÀÚ¸®°¡ -
	D[1][0] = 1;  // -+
	D[1][1] = 2;  // +-

	for (int i = 2; i<MAX; i++)
	{
		D[i][0] = D[i - 1][1];    //+-+
		D[i][1] = D[i][0] + 1;      //-+-


	}

	fscanf(in,"%d", &T);
	for (int a = 1; a <= T; a++)
	{
		int len, cnt = 0;
		fscanf(in,"%s", S);

		len = strlen(S);

		for (int i = 1; i<len; i++){
			if (S[i] != S[i - 1]) cnt++;
		}
		//  printf("cnt = %d\n ", cnt);

		fprintf(out,"Case #%d: ", a);
		if (S[len - 1] == '+') fprintf(out,"%d\n", D[cnt][0]);
		else fprintf(out,"%d\n", D[cnt][1]);
	}



	return 0;
}