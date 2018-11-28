
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	ifstream is("A-large.in");
	ofstream os("out-large.txt");
	int T,k,i,j,sum_row,sum_col,sum_cross1, sum_cross2,sum,status;
	string str[4] = {"X won", "O won", "Draw", "Game has not completed"};

	char chs[4][4],c;
	is >> T;
	is.get(c);

	for(k = 1; k<=T; k++){
		//input 
		sum=0;
		status = 4;
		for(i = 0;i<4;i++){
			for(j=0;j<4;j++){
				chs[i][j] = is.get();
				switch(chs[i][j]){
				case 'X': 
					chs[i][j] = 2; 
					break;
				case 'O':
					chs[i][j] = 10;
					break;
				case '.':
					chs[i][j] = 0;
					break;
				case 'T':
					chs[i][j] = 1;
					break;
				}
				sum += chs[i][j];
			}
			is.get(c);
		}
		is.get(c);

		//check
		for(i=0;i<4;i++){
			sum_row=0, sum_col=0;
			for(j=0;j<4;j++){
				sum_row += chs[i][j];
				sum_col += chs[j][i];
				
			}
			if(sum_row == 8 || sum_row ==7 || sum_col == 7 || sum_col ==8) {
				status = 0;
				break;
			}
			if(sum_row == 40 || sum_row ==31 || sum_col == 31 || sum_col ==40) {
				status = 1;
				break;
			}
		}

		sum_cross1 =0;
		sum_cross2 =0;
		for(i=0;i<4;i++){
			sum_cross1 += chs[i][i];
			sum_cross2 += chs[i][3-i];
		}
		if(sum_cross1 == 8 || sum_cross1 == 7 || sum_cross2 == 8 || sum_cross2 == 7 ) status = 0;
		if(sum_cross1 == 40 || sum_cross1 == 31 || sum_cross2 == 40 || sum_cross2 == 31 ) status = 1;

		if(status ==4 && (sum == 96 || sum == 87 )) status = 2;
		if(status == 4) status = 3;

		os<<"Case #" << k << ": "<< str[status] << endl;
	}
	return 0;
}

