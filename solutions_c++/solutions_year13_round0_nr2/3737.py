#include <stdio.h>

FILE *fout;

void prn(int f)
{
	static int cnt =1 ;

	switch(f)
	{
	case 0:
		fprintf(fout,"Case #%d: YES\n",cnt);
		break;
	case 1:
		fprintf(fout,"Case #%d: NO\n",cnt);
		break;
	}
	cnt++;
}

void main()
{
	FILE *fin = fopen("B-large.in","r");
	fout = fopen("B-large.out","w");

	int lawn[100][100];
	int check[100][100];
	int N, M, n;
	int i, j, max;

	fscanf(fin,"%d",&n);
	printf("%d\n",n);

	while(n--)
	{
		fscanf(fin, "%d %d", &N, &M);
		
		for(i=0; i<N; i++)
			for(j=0; j<M; j++)
			{
				fscanf(fin,"%d",&lawn[i][j]);
				check[i][j] = 1;
			}
		
		for(i=0; i<N; i++)
		{
			max = 0;
			for(j=0; j<M; j++)
				if( max < lawn[i][j])
					max = lawn[i][j];
			
			for(j=0; j<M; j++)
				if( lawn[i][j] < max )
					check[i][j] = 0;
		}
						
		for(j=0; j<M; j++)
		{
			max = 0;
			for(i=0; i<N; i++)
				if( max < lawn[i][j])
					max = lawn[i][j];

			for(i=0; i<N; i++)
				if( !check[i][j] && lawn[i][j] == max )
					check[i][j] = 1;
		}

		for(i=0; i<N; i++)
		{
			for(j=0; j<M; j++)
			{
				if(!check[i][j])
				{
					prn(1);
					break;
				}
			}
			if(j!=M)
				break;
		}

		if( i==N )
			prn(0);

	}
}