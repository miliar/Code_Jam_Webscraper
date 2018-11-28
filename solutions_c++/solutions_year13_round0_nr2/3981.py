#include<stdio.h>
#include<stdlib.h>

int	main()
{
	FILE *f1,*f2;
	int error;
	error = fopen_s(&f1,"B-large.in","r");
	if(error == -1)
		printf("eroare la deschidere");
	error = fopen_s(&f2,"B-large.out","w");
	if(error == -1)
		printf("eroare la deschidere2");

	int i,j,k,N,M,T;
	int a[101][101],lineheight[101],columnheight[101];
	bool possible;
	fscanf_s(f1,"%d",&T);
	for(i = 0; i < T; i++)
	{
		for(j = 0; j < 101; j++)
		{
			lineheight[j] = 0;
			columnheight[j] = 0;
		}
		possible = true;
		fscanf_s(f1,"%d %d",&N,&M);
		for(j = 0; j < N; j++)
		{
			for(k = 0; k < M; k++)
			{
				fscanf_s(f1,"%d",&a[j][k]);
				lineheight[j] = lineheight[j]<a[j][k]?a[j][k]:lineheight[j];
				columnheight[k] = columnheight[k]<a[j][k]?a[j][k]:columnheight[k]; 
			}
		}
		for(j = 0; j < N; j++)
		{
			for(k = 0; k < M; k++)
			{
				if( a[j][k]<lineheight[j] && a[j][k]<columnheight[k] && possible)
				{
					possible = false;
				}
			}
		}
		fprintf_s(f2,"Case #%d: ",i+1);
		if( possible )
		{
			fprintf_s(f2,"YES\n");
		}
		else
		{
			fprintf_s(f2,"NO\n");
		}
	}
return 0;
}