#include <stdio.h>
#include <stdlib.h>
int caseNum, totalCaseNum;
FILE *fin, *fout;

#define id(i,j) (i)*50+(j)

int N;
int aa[100][50];
bool findSol;

int compare(const void *a, const void *b)
{
	return ((int*)a)[0] - ((int*)b)[0];
}

void dfs(int k, int *map, int beginR, int beginC)
{
	int mm[2500];
	int p, i, j, l;
	p = aa[k][0];
	bool ch;
	
	if(findSol) return;

	for(i=0; i<2500; i++) mm[i] = map[i];
	
	if(k == 2*N-1 && beginR == N && beginC == N)
	{
		findSol = 1;
		for(i=0; i<N; i++)
		{
			for(j=0; j<N; j++) printf("%d ", mm[id(i,j)]);
			printf("\n");
		}
		printf("-------------\n\n");

		bool rr[50], cc[50];
		for(i=0; i<N; i++) rr[i] = cc[i] = 0;
		for(i=0; i<2*N-1; i++)
		{
			//R
			for(j=0; j<N; j++)
			{
				if(aa[i][0] == mm[id(j,0)]) break;
			}
			if(!rr[j]){
				rr[j] = 1;
				for(l=0; l<N; l++)
				{
					if(mm[id(j,l)] != aa[i][l])
					{
						rr[j] = 0;
						break;
					}
				}
				if(rr[j]) continue;
			}

			//C
			for(j=0; j<N; j++)
			{
				if(aa[i][0] == mm[id(0,j)]) break;
			}
			if(!cc[j]){
				cc[j] = 1;
				for(l=0; l<N; l++)
				{
					if(mm[id(l,j)] != aa[i][l])
					{
						cc[j] = 0;
						break;
					}
				}
			}
		}

		for(i=0; i<N; i++)
		{
			if(!rr[i])
			{
				fprintf(fout, "Case #%d: ", caseNum+1);
				for(j=0; j<N; j++) fprintf(fout, "%d ", mm[id(i,j)]);
				fprintf(fout, "\n");
				return;
			}
		}

		for(i=0; i<N; i++)
		{
			if(!cc[i])
			{
				fprintf(fout, "Case #%d: ", caseNum+1);
				for(j=0; j<N; j++) fprintf(fout, "%d ", mm[id(j,i)]);
				fprintf(fout, "\n");
			}
		}
	}

	// R
	if(beginR < N)
	{
		ch = 1;
		for(i=0; i<N; i++)
		{
			if(mm[id(beginR,i)] != 0 && mm[id(beginR,i)] != aa[k][i])
			{
				ch = 0;
				break;
			}
			mm[id(beginR,i)] = aa[k][i];
		}
		if(ch) dfs(k+1, mm, beginR+1, beginC);
		for(j=0; j<=i; j++) mm[id(beginR,j)] = map[id(beginR,j)];
		if(!ch) dfs(k, mm, beginR+1, beginC);
	}

	// C
	if(beginC < N)
	{
		ch = 1;
		for(i=0; i<N; i++)
		{
			if(mm[id(i,beginC)] != 0 && mm[id(i,beginC)] != aa[k][i])
			{
				ch = 0;
				break;
			}
			mm[id(i,beginC)] = aa[k][i];
		}
		if(ch) dfs(k+1, mm, beginR, beginC+1);
		for(j=0; j<=i; j++) mm[id(j,beginC)] = map[id(j,beginC)];
		if(!ch) dfs(k, mm, beginR, beginC+1);
	}
}

int main()
{
	fin = fopen("sample_input.in", "r");
	fout = fopen("sample_output.out", "w");

	fscanf(fin, "%d", &totalCaseNum);
	int mm[2500];
	for(caseNum=0; caseNum<totalCaseNum; caseNum++)
	{
		fscanf(fin, "%d", &N);
		for(int i=0; i<2*N-1; i++)
		{
			for(int j=0; j<N; j++) fscanf(fin, "%d", &aa[i][j]);
		}
		qsort(aa, 2*N-1, sizeof(int)*50, compare);
		for(int i=0; i<2500; i++) mm[i] = 0;
		findSol = 0;
		dfs(0, mm, 0, 0);
	}

	fcloseall();

	return 0;
}