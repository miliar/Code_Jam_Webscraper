#include <stdio.h>

int main(void)
{
	int T;
	int Smax[100];
	char Si[101][7];
	int i, j;
	int stand;
	int frd[100]={0};

	FILE *in, *out;
	out = fopen("OUT.out", "w");
	in = fopen("A-small-attempt10.in", "r");

	fscanf(in, "%d", &T);
	for(i=0 ; i<T ; i++)
	{
		fscanf(in, "%d %s", &Smax[i], Si[i]);
		stand=0;

		for(j=0 ; j<=Smax[i] ; j++)
		{
			if(stand < j)
			{
				if(frd[i] < j - stand)
					frd[i] = j - stand;
			}
			stand += (Si[i][j]-'0');
		}
		fprintf(out,"Case #%d: %d\n", i+1, frd[i]);
	}
	fclose(in);
	fclose(out);
	return 0;
}