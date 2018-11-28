#include <cstdio>
#include <algorithm>

int main()
{
	FILE * Input;
	FILE * Output;
	Output = fopen("output.txt","w");
	Input = fopen("D-large.in", "r");
	int TC;
	int length;
	int tempN,tempK;
	int memoN,memoK;
	float naomi[1001];
	float ken[1001];

	fscanf(Input,"%d", &TC);

	for ( int tc = 1; tc <= TC ; tc++ )
	{
		tempN = 0; memoN = 0;
		tempK = 0; memoK = 0;
		fscanf(Input,"%d", &length);
		for ( int i = 0 ; i < length; i++)
			fscanf(Input,"%f", &naomi[i]);
		for ( int i = 0 ; i < length; i++)
			fscanf(Input,"%f", &ken[i]);
		

		std::sort(naomi,naomi+length);
		std::sort(ken,ken+length);
		for ( int i = 0 ; i < length; i++ )
		{
			if ( naomi[i] > ken[tempN] )
			{
				memoN++;
				tempN++;
			}
			if ( ken[i] > naomi[tempK] )
			{
				memoK++;
				tempK++;
			}
		}
		
		
		fprintf(Output,"Case #%d: %d %d\n", tc,memoN, length-memoK);
	}
	fclose(Input);
	fclose(Output);

	return 0;
}
