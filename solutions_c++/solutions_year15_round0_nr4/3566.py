# include <cstdio>
# include <iostream>
# define i64 long long
# define INPUT_FILE "D-small-attempt0.in"
# define OUTPUT_FILE "op.txt"
using namespace std;

char name[4][4][5] = { 	"GRRR",	"GGRR",	"GRRR",	"GGRR",	"GGRR",	"GGRR",	"GGGR",	"GGRR",	"GRRR",	"GGGR",	"GRGR",	"GGGG",	"GGRR",	"GGRR",	"GGGG",	"GGRG"};

int main()
{
	i64 T, t, X, R, C;
	FILE *ip, *op;
	
	ip = fopen(INPUT_FILE, "r");
	op = fopen(OUTPUT_FILE, "w");
	fscanf(ip, "%lld", &T);
	for(t = 1; t <= T; ++t)
	{
		fscanf(ip, "%lld%lld%lld", &X, &R, &C);
		fprintf(op, "Case #%d: ", t);
		if(name[R - 1][C - 1][X - 1] == 'G')
			fprintf(op, "GABRIEL\n");
		else
			fprintf(op, "RICHARD\n");
	}
	fclose(ip);
	fclose(op);
	
	return 0;
}
