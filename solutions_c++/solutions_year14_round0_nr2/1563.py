#include <cstdio>

int main()
{
	FILE * Input;
	FILE * Output;
	Output = fopen("output.txt","w");
	Input = fopen("B-large.in", "r");
	int TC;
	float C,F,X;

	long double memo;
	long double temp;
	long double tempcount;

	fscanf(Input,"%d", &TC);

	for ( int tc = 1; tc <= TC ; tc++ )
	{
		temp = 0;
		memo = 0;
		fscanf(Input,"%f", &C);
		fscanf(Input,"%f", &F);
		fscanf(Input,"%f", &X);
		tempcount = 2;
		memo = X / 2;
		while ( true ) 
		{
			temp = temp + ( C / tempcount );
			tempcount = tempcount + F;
			if ( memo > X/tempcount+temp)
				memo = X/tempcount+temp;
			else break;
		}
		
		fprintf(Output,"Case #%d: %.7f\n", tc,memo);
	}
	fclose(Input);
	fclose(Output);

	return 0;
}
