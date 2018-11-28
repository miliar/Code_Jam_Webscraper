#include <iostream>

using namespace std;

int main()
{
	int i, j, k, l, T, sumTotal;
	char gameC;
	int game [4][4];
	int rowSum[4], colSum[4], diaSum[2];
	bool allfilled;
	cin>>T;
	for (i=0; i<T; i++)
	{
		sumTotal=0;
		for (j=0; j<4; j++) 
		{
			rowSum[j]=0;
			colSum[j]=0;
			if (j<2) diaSum[j]=0;
			for (k=0; k<4; k++) 
			{
				cin>>gameC;
				if (gameC=='X') game[j][k]=-2;
				if (gameC=='O') game[j][k]=1;
				if (gameC=='T') game[j][k]=0;
				if (gameC=='.') game[j][k]=100;
			}
		}

		for (j=0; j<4; j++)
		{
			for (k=0; k<4; k++) {rowSum[j]+=game[j][k]; colSum[j]+=game[k][j]; sumTotal+=sumTotal+game[j][k];}
			if (j==0) for(l=0; l<4; l++) diaSum[j]+=game[l][l];
			if (j==1) diaSum[j] = game[0][3]+game[1][2]+game[2][1]+game[3][0];
		}
			
		l=0;
		if (diaSum[l]==4 || diaSum[l]==3) {cout<<"Case #"<<i+1<<": O won\n"; continue;}
		else if (diaSum[l]==-8 || diaSum[l]==-6) {cout<<"Case #"<<i+1<<": X won\n"; continue;}
		else
		{
		l=1;
		if (diaSum[l]==4 || diaSum[l]==3) {cout<<"Case #"<<i+1<<": O won\n"; continue;}
		else if (diaSum[l]==-8 || diaSum[l]==-6) {cout<<"Case #"<<i+1<<": X won\n"; continue;}
		}

		for (j=0; j<4; j++) 
		{
			if (rowSum[j]==4 || colSum[j]==4 || rowSum[j]==3 || colSum[j]==3) {cout<<"Case #"<<i+1<<": O won\n"; break;}
			else if (rowSum[j]==-8 || colSum[j]==-8 || rowSum[j]==-6 || colSum[j]==-6) {cout<<"Case #"<<i+1<<": X won\n"; break;}			
			else if (j==3)
			{
				if (sumTotal<50) {cout<<"Case #"<<i+1<<": Draw\n"; break;}
				else {cout<<"Case #"<<i+1<<": Game has not completed\n"; break;}
			}
		}
	}
	return 0;
}
