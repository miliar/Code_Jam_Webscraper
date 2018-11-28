#include<stdio.h>

int main(int argc, char *argv[])
{
	int matrix[4][4];
	char symbol;
	int caseNum=1, totalCases=0, i, j, k;
	int sumH=0, sumV=0, state;

	scanf("%d\n", &totalCases);
	for(i=0; i<totalCases; ++i)
	{
		state=0;
		for(j=0; j<4; ++j)
		{
			for(k=0; k<4; ++k)
			{
				symbol=getchar();
				if(symbol=='\n')
					--k;
				switch(symbol)
				{
					case 'X':
					matrix[j][k]=1;
					break;

					case 'O':
					matrix[j][k]=-1;
					break;

					case 'T':
					matrix[j][k]=100;
					break;

					case '.':
					matrix[j][k]=0;
					state=4;
					break;

					default:
					break;
				}
			}
		}
		for(k=0; k<4; ++k)
		{
			sumH=matrix[k][0]+matrix[k][1]+matrix[k][2]+matrix[k][3];
			sumV=matrix[0][k]+matrix[1][k]+matrix[2][k]+matrix[3][k];
			if(sumH==4 || sumH==103 || sumV==4 || sumV==103) state=1;
			else if(sumH==-4 || sumH==97 || sumV==-4 || sumV==97) state=2;
			//printf("SumH: %d, SumV: %d\n", sumH, sumV);
		}
		sumH=matrix[0][0]+matrix[1][1]+matrix[2][2]+matrix[3][3];
		sumV=matrix[3][0]+matrix[2][1]+matrix[1][2]+matrix[0][3];
		//printf("SumH: %d, SumV: %d\n\n", sumH, sumV);
		if(sumH==4 || sumH==103 || sumV==4 || sumV==103) state=1;
		else if(sumH==-4 || sumH==97 || sumV==-4 || sumV==97) state=2;

		if(state==0) state=3;

		switch(state)
		{
			case 1:
			printf("Case #%d: X won\n", caseNum);
			break;

			case 2:
			printf("Case #%d: O won\n", caseNum);
			break;

			case 3:
			printf("Case #%d: Draw\n", caseNum);
			break;

			case 4:
			printf("Case #%d: Game has not completed\n", caseNum);
			break;
		}
		caseNum++;

	}
	return 0;
}
