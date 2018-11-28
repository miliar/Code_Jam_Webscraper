#include<stdio.h>

int lawn[100][100], rows, cols;

bool isOkCell(int r, int c)
{
	bool ok=true;

	for(int h=0; h<rows; h++)
	{	
		if(lawn[h][c] > lawn[r][c])
		{
			ok=false;
			break;
		}
	}
	if(ok)
		return true;

	ok=true;
	for(int h=0; h<cols; h++)
	{	
		if(lawn[r][h] > lawn[r][c])
		{
			ok=false;
			break;
		}
	}
	if(ok)
		return true;

	return false;
}

int main()
{
	int N, ok;

	FILE* fin = fopen("input.txt","r");
	FILE* fout = fopen("output.txt","w");

	fscanf(fin, "%d\n", &N);
	for(int h=0; h<N; h++)
	{
		fscanf(fin, "%d %d\n", &rows, &cols);

		for(int r=0; r<rows; r++)
		{
			for(int c=0; c<cols; c++)
			{
				fscanf(fin, "%d ", &lawn[r][c]);
			}
			fscanf(fin, "\n");
		}

		ok=1;
		for(int r=0; r<rows && ok; r++)
		{
			for(int c=0; c<cols; c++)
			{
				if(!isOkCell(r, c))
				{
					ok=0;
					break;
				}
			}
		}
		
	
		fprintf(fout,"Case #%d: ", h+1);
		if(ok)		
			fprintf(fout,"YES\n");
		else
			fprintf(fout,"NO\n");
	}

	fclose(fin);
	fclose(fout);
}