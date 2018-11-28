#include <iostream>

void main(){
	FILE *ulaz = fopen("B-large.in","r");
	FILE *izlaz = fopen("output.txt","w");
	int p,n,m;
	fscanf(ulaz,"%d",&p);
	
	
	int polje[100][100];
	for( int k = 1; k < p+1; k++ ){
		fscanf(ulaz,"%d%d",&n,&m);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
				fscanf(ulaz,"%d",&polje[i][j]);
		}

		int max1 = 0;
		int max2 = 0;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				max1 = 0;
				max2 = 0;
				for (int a = 0; a < m; a++)
					if(polje[i][a]>max1)
						max1 = polje[i][a];
				for (int a = 0; a < n; a++)
					if(polje[a][j]>max2)
						max2 = polje[a][j];
				if((polje[i][j]==max1) || (polje[i][j]==max2))
					continue;
				else
				{
					fprintf(izlaz,"Case #%d: NO\n",k);
					goto out;
				}
		
			}

		fprintf(izlaz,"Case #%d: YES\n",k);
		out:continue;
	}

	fclose(izlaz);
	fclose(ulaz);
}