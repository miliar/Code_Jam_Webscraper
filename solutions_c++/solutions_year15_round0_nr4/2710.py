#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* fin=fopen("d.in", "r");
	FILE* fou=fopen("answer.out", "w");
	int t;

//	scanf("%d", &t);
	fscanf(fin, "%d", &t);

	for(int i=1; i<=t; i++)
	{
		int x, r, c;
//		scanf("%d %d %d", &x, &r, &c);
		fscanf(fin, "%d %d %d", &x, &r, &c);
		if(r*c%x!=0)
		{
			printf("Case #%d: RICHARD\n", i);
			fprintf(fou, "Case #%d: RICHARD\n", i);
			continue;
		}
		if(x>r && x>c)
		{
			printf("Case #%d: RICHARD\n", i);
			fprintf(fou, "Case #%d: RICHARD\n", i);
			continue;
		}
		if(x<=2)
		{
			printf("Case #%d: GABRIEL\n", i);
			fprintf(fou, "Case #%d: GABRIEL\n", i);
			continue;
		}
		if(x>=7)
		{
			printf("Case #%d: RICHARD\n", i);
			fprintf(fou, "Case #%d: RICHARD\n", i);
			continue;
		}
		if(x>2*r-1 || x>2*c-1)
		{
			printf("Case #%d: RICHARD\n", i);
			fprintf(fou, "Case #%d: RICHARD\n", i);
			continue;
		}

		printf("Case #%d: GABRIEL\n", i);
		fprintf(fou, "Case #%d: GABRIEL\n", i);
	}

	return 0;
}



