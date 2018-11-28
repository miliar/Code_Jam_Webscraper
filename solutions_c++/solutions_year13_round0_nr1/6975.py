#include <stdio.h>

// 0 - O, 1 - X
int A[10][2];

int check(bool comp)
{
	for(int i=0; i<10; i++)
	{
		if(A[i][0] == 4)
			return 0;	// O wins
		if(A[i][1] == 4)
			return 1;	// X wins
	}

	if(comp)
		return 2;	// DRAW
	else
		return 3;	// incomplete
}

void zero()
{
	for(int i=0; i<10; i++)
		A[i][0]=A[i][1]=0;
}

int main()
{
	FILE* fin = fopen("A-large.in", "r");
	FILE* fout = fopen("out.txt", "w");

	int n;
	fscanf(fin, "%d", &n);

	for(int i=1; i<=n; i++)
	{
		fprintf(fout, "Case #%d: ", i);
		bool complete = true; zero();
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
			{
				char c='\n';
				while(c=='\n')
					fscanf(fin, "%c", &c);
				switch(c)
				{
				case 'O':
					A[j][0]++; A[k+4][0]++; 
					break;
				case 'X':
					A[j][1]++; A[k+4][1]++; 
					break;
				case 'T':
					A[j][0]++; A[k+4][0]++; 
					A[j][1]++; A[k+4][1]++; 
					break;
				case '.':
					complete=false;
					break;
				}
				if(j==k)
					switch(c)
					{
					case 'O':
						A[8][0]++; 
						break;
					case 'X':
						A[8][1]++; 
						break;
					case 'T':
						A[8][0]++; 
						A[8][1]++; 
						break;
					}
				if(j+k==3)
					switch(c)
					{
					case 'O':
						A[9][0]++; 
						break;
					case 'X':
						A[9][1]++; 
						break;
					case 'T':
						A[9][0]++; 
						A[9][1]++; 
						break;
					}
			}
		switch(check(complete))
		{
		case 0:
			fprintf(fout, "O won");
			break;
		case 1:
			fprintf(fout, "X won");
			break;
		case 2:
			fprintf(fout, "Draw");
			break;
		case 3:
			fprintf(fout, "Game has not completed");
			break;
		}

		fprintf(fout, "\n");
	}
}