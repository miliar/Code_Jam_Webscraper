#include "stdio.h"


int main()
{
	char str[10][10];
	int N;
	scanf("%d",&N);
	gets(str[0]);
	for(int I=1; I<=N; ++I)
	{
		gets(str[0]);
		gets(str[1]);
		gets(str[2]);
		gets(str[3]);
		gets(str[4]);

		int i, j, k;
		int rowS[4], rowT[4], colS[4], colT[4], diaS[4], diaT[4];
		for(i=0; i<4; ++i)
		{
			rowS[i]=rowT[i]=colS[i]=colT[i]=diaS[i]=diaT[i]=0;
		}
		bool anyEmpty = false;
		for(i=0; i<4; ++i)
		{
			for(j=0; j<4; ++j)
			{
				switch( str[i][j] )
				{
				case 'X': rowS[i]++; colS[j]++; break;
				case 'O': rowS[i]--; colS[j]--; break;
				case 'T': rowT[i]++; colT[j]++; break;
				case '.': anyEmpty = true; break;
				}
			}

			switch( str[i][i] )
			{
			case 'X': diaS[0]++; break;
			case 'O': diaS[0]--; break;
			case 'T': diaT[0]++; break;
			}

			switch( str[i][3-i] )
			{
			case 'X': diaS[1]++; break;
			case 'O': diaS[1]--; break;
			case 'T': diaT[1]++; break;
			}
		}

		printf("Case #%d:", I);
		bool xWon =  (rowS[0]==3 && rowT[0]==1) ||  (rowS[1]==3 && rowT[1]==1) ||  (rowS[2]==3 && rowT[2]==1) ||  (rowS[3]==3 && rowT[3]==1)
			      || (colS[0]==3 && colT[0]==1) ||  (colS[1]==3 && colT[1]==1) ||  (colS[2]==3 && colT[2]==1) ||  (colS[3]==3 && colT[3]==1)
				  || (diaS[0]==3 && diaT[0]==1) ||  (diaS[1]==3 && diaT[1]==1)
				  || (rowS[0]==4) ||  (rowS[1]==4) ||  (rowS[2]==4) ||  (rowS[3]==4)
			      || (colS[0]==4) ||  (colS[1]==4) ||  (colS[2]==4) ||  (colS[3]==4)
				  || (diaS[0]==4) ||  (diaS[1]==4);
		bool oWon =  (rowS[0]==-3 && rowT[0]==1) ||  (rowS[1]==-3 && rowT[1]==1) ||  (rowS[2]==-3 && rowT[2]==1) ||  (rowS[3]==-3 && rowT[3]==1)
			      || (colS[0]==-3 && colT[0]==1) ||  (colS[1]==-3 && colT[1]==1) ||  (colS[2]==-3 && colT[2]==1) ||  (colS[3]==-3 && colT[3]==1)
				  || (diaS[0]==-3 && diaT[0]==1) ||  (diaS[1]==-3 && diaT[1]==1)
				  || (rowS[0]==-4) ||  (rowS[1]==-4) ||  (rowS[2]==-4) ||  (rowS[3]==-4)
			      || (colS[0]==-4) ||  (colS[1]==-4) ||  (colS[2]==-4) ||  (colS[3]==-4)
				  || (diaS[0]==-4) ||  (diaS[1]==-4);
		if( xWon )
			printf(" X won");
		else if( oWon )
			printf(" O won");
		else if( anyEmpty )
			printf(" Game has not completed");
		else
			printf(" Draw");

		printf("\n");
	}
	return 0;
}

