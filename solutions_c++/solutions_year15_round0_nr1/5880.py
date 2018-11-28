#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* fin=fopen("a.in", "r");
	FILE* fou=fopen("b.out", "w");
	int t;

	fscanf(fin, "%d", &t);

	for(int i=1; i<=t; i++)
	{
		int n;
		int people=0;
		int fri=0;
		char p=0;
		fscanf(fin, "%d ", &n);

		for(int j=0; j<=n; j++)
		{
			if(people<j)
			{
				fri+=j-people;
				people=j;
			}
			fscanf(fin, "%c", &p);
			people+=p-'0';
		}

		printf("Case #%d: %d\n", i, fri);
		fprintf(fou, "Case #%d: %d\n", i, fri);

	}

	return 0;
}



