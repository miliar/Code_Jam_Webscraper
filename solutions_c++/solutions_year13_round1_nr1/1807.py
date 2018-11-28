#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int size;
	long long int a ,b;
	FILE* input, *output;

	if((input = fopen("A-small-attempt0.in","rt")) == NULL)
	{
		printf("err\n\n");
	}

	if((output = fopen("A-small-attempt0.out","wt")) == NULL)
	{
		printf("err\n\n");
	}

	fscanf(input, "%d", &size);

	for(int i=0 ; i< size; i++)
	{
		long long int l=0;
		long long int j = 0;
		fscanf(input, "%lld %lld", &a, &b);

		for(j = a ; b > 0 ; j+=2 , a++ )
		{
			long long int n;
			n = (j+1)*(j+1) - j*j;
			b -= n;
			l++;
		}
		if( b == 0 ) l++;
		fprintf(output, "Case #%d: %lld\n", i+1, l-1);
	}
	return 0;
}