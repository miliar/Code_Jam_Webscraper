#include <iostream>
using namespace std;

// utiliser comme ./speaktong < fin > fout

int main(int argc, char **argv)
{

(void)argc,(void)argv;

	char result[2][4] = {"YES","NO"};
	int T; // number of test cases (lines of file)
	scanf("%d/n",&T);

	for(int i = 0; i < T; i++) // (tests)
	{
		int N, M;
		scanf("%d %d/n",&N,&M);
		
		int **lawn = (int**) malloc(N*sizeof(int*));
		for(int j = 0; j < N; j++)
			lawn[j] = (int*) malloc(M*sizeof(int));
			
		int *maxlin = (int*) malloc(N*sizeof(int));
		int *maxcol = (int*) malloc(M*sizeof(int));
		
		for(int l = 0; l < N; l++) //percorre linhas do test
		{
			maxlin[l] = 0;
			for(int c = 0; c < M; c++) //percorre colunas do test
			{
				if(l==0) maxcol[c] = 0;
				scanf("%d ",&(lawn[l][c]));
				maxcol[c] = ((maxcol[c] > lawn[l][c]) ? maxcol[c] : lawn[l][c]);
				maxlin[l] = ((maxlin[l] > lawn[l][c]) ? maxlin[l] : lawn[l][c]);
			}
		}
		
		int r = 0;
		for(int l = 0; l < N; l++) //percorre linhas do test
		{
			for(int c = 0; c < M; c++) //percorre colunas do test
			{
				if( (lawn[l][c] < maxlin[l]) && (lawn[l][c] < maxcol[c]) )
				{
					r = 1;
					break;
				}
			}
			if(r == 1)
				break;
		}
		
		cout << "Case #" << i+1 << ": " << result[r] << endl;
		
		for(int j = 0; j < N; j++)
			free(lawn[j]);
		free(lawn);
		free(maxlin); free(maxcol);
	}
	return 0;
}


