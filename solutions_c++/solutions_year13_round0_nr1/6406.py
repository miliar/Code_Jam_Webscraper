#include<string>
#include<iostream>
#include<fstream>
using namespace std;

int main(void)
{
	ifstream file;
	file.open("A-large.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;

	for(int t=1; t<= caseNo; t++)
	{
		char model[4][4];
		char temp;
		int m,n;
		int result[4][4];
		for(n=0;n<4;n++){
			file >> model[n][0] >> model[n][1] >> model[n][2] >>model[n][3];
			for(m=0;m<4;m++){
				if(model[n][m]=='X') result[n][m]=1;
				if(model[n][m]=='O') result[n][m]=2;
				if(model[n][m]=='T') result[n][m]=3;
				if(model[n][m]=='.') result[n][m]=0;
			}
		}

		int score=0;
		int space=0;

		for(n=0;n<4;n++){
			if(result[n][0]==0 || result[n][1]==0 || result[n][2]==0 || result[n][3]==0) space = 1;
			if((result[n][0]==1 || result[n][0]==3) && (result[n][1]==1 || result[n][1]==3) && (result[n][2]==1 || result[n][2]==3) && (result[n][3]==1 || result[n][3]==3)){
				score = 1;
				break;
			}
			if((result[0][n]==1 || result[0][n]==3) && (result[1][n]==1 || result[1][n]==3) && (result[2][n]==1 || result[2][n]==3) && (result[3][n]==1 || result[3][n]==3)){
				score = 1;
				break;
			}
			if((result[n][0]==2 || result[n][0]==3) && (result[n][1]==2 || result[n][1]==3) && (result[n][2]==2 || result[n][2]==3) && (result[n][3]==2 || result[n][3]==3)){
				score = 2;
				break;
			}
			if((result[0][n]==2 || result[0][n]==3) && (result[1][n]==2 || result[1][n]==3) && (result[2][n]==2 || result[2][n]==3) && (result[3][n]==2 || result[3][n]==3)){
				score = 2;
				break;
			}
		}
		if((result[0][0]==1 || result[0][0]==3) && (result[1][1]==1 || result[1][1]==3) && (result[2][2]==1 || result[2][2]==3) && (result[3][3]==1 || result[3][3]==3)){
			score = 1;
		}
		if((result[0][3]==1 || result[0][3]==3) && (result[1][2]==1 || result[1][2]==3) && (result[2][1]==1 || result[2][1]==3) && (result[3][0]==1 || result[3][0]==3)){
			score = 1;
		}
		if((result[0][0]==2 || result[0][0]==3) && (result[1][1]==2 || result[1][1]==3) && (result[2][2]==2 || result[2][2]==3) && (result[3][3]==2 || result[3][3]==3)){
			score = 2;
		}
		if((result[0][3]==2 || result[0][3]==3) && (result[1][2]==2 || result[1][2]==3) && (result[2][1]==2 || result[2][1]==3) && (result[3][0]==2 || result[3][0]==3)){
			score = 2;
		}

		if(space == 0 && score == 0) score = 3;
		else if(score == 0)score = 4;
		

		output << "Case #" << t << ": ";
		if(score == 1)output <<  "X won" << endl;
		if(score == 2)output <<  "O won" << endl;
		if(score == 3)output <<  "Draw" << endl;
		if(score == 4)output <<  "Game has not completed" << endl;

	}
}