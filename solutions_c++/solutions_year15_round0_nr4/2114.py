#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* inf= fopen("input.txt", "r");
	FILE* outf= fopen("output.txt", "w");

	int T, R, C, X;
	fscanf(inf, "%d", &T);

	for(int i=1; i<=T; i++)
	{
		fscanf(inf, "%d %d %d", &X, &R, &C);
		if(R>C)
		{
			int buf=R;
			R=C;
			C=buf;
		}

		int res; // 0 - GABRIEL, 1 - RICHARD
		if(X==1) res=0;
		else
		if(X==2)
		{
			if((R*C) % 2 !=0) res=1;
			else res=0;
		}
		if(X==3)
		{
			if((R*C) % 3 !=0) res=1;
			else
			{
				if(R==1) res=1;
				else res=0;
			}
		}
		if(X==4)
		{
			if((R*C) % 4 !=0) res=1;
			else
			{
				if(R<3) res=1;
				else res=0;
			}
		}
		if(res==0) fprintf(outf, "Case #%d: GABRIEL\n", i);
		else fprintf(outf, "Case #%d: RICHARD\n", i);
	}

	return 0;
}