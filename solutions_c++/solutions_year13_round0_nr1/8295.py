#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;
char matrix[4][4];
char check(void){
  int i,j;
  char ret;
  for(i=0; i<4; i++){  /* check rows */
    if((matrix[i][0]==matrix[i][1] &&
       matrix[i][0]==matrix[i][2] &&
       matrix[i][0]==matrix[i][3] && matrix[i][0]!='.') || 
       (matrix[i][1]=='T' &&
       matrix[i][0]==matrix[i][2] &&
       matrix[i][0]==matrix[i][3] && matrix[i][0]!='.') ||
       (matrix[i][0]==matrix[i][1] &&
       matrix[i][2]=='T' &&
       matrix[i][0]==matrix[i][3] && matrix[i][0]!='.') ||
       (matrix[i][0]==matrix[i][1] &&
       matrix[i][0]==matrix[i][2] &&
       matrix[i][3]=='T' && matrix[i][0]!='.'))
       return matrix[i][0];
    }
  for(i=0; i<4; i++){
    ret = matrix[0][i];
    if((matrix[0][i]==matrix[1][i] &&
       matrix[0][i]==matrix[2][i] &&
       matrix[0][i]==matrix[3][i] && matrix[0][i] != '.') ||
       (matrix[1][i]=='T' &&
       matrix[0][i]==matrix[2][i] &&
       matrix[0][i]==matrix[3][i] && matrix[0][i] != '.') ||
       (matrix[0][i]==matrix[1][i] &&
       matrix[2][i]=='T' &&
       matrix[0][i]==matrix[3][i] && matrix[0][i] != '.') ||
       (matrix[0][i]==matrix[1][i] &&
       matrix[0][i]==matrix[2][i] &&
       matrix[3][i]=='T' && matrix[0][i] != '.')
       )
        return matrix[0][i];
    }
  if((matrix[0][0]==matrix[1][1] &&
     matrix[0][0]==matrix[2][2] &&
     matrix[0][0]==matrix[3][3] && matrix[0][0] != '.') ||
     (matrix[1][1]=='T' &&
     matrix[0][0]==matrix[2][2] &&
     matrix[0][0]==matrix[3][3] && matrix[0][0] != '.') ||
     (matrix[0][0]==matrix[1][1] &&
     matrix[2][2]=='T' &&
     matrix[0][0]==matrix[3][3] && matrix[0][0] != '.') ||
     (matrix[0][0]==matrix[1][1] &&
     matrix[0][0]==matrix[2][2] &&
     matrix[3][3]=='T' && matrix[0][0] != '.'))
       return matrix[0][0];
  if((matrix[0][3]==matrix[1][2] &&
     matrix[1][2]==matrix[2][1] &&
     matrix[2][1]==matrix[3][0] && matrix[0][3] != '.') ||
     (matrix[0][3]==matrix[1][2] &&
     matrix[1][2]=='T' &&
     matrix[2][1]==matrix[3][0] && matrix[0][3] != '.') ||
     (matrix[0][3]==matrix[1][2] &&
     matrix[1][2]==matrix[2][1] &&
     matrix[2][1]=='T' && matrix[0][3] != '.') ||
     (matrix[0][3]==matrix[1][2] &&
     matrix[1][2]==matrix[2][1] &&
     matrix[3][0]=='T' && matrix[0][3] != '.')
     )
       return matrix[0][3];
  for(i=0;i<4;i++)
  	for(j=0;j<4;j++)
  		if(matrix[i][j] == '.')
  			return 'i';
  return ' ';
}

int main(){
	ofstream fout;
	ifstream fin;
	fin.open("A-small-attempt3.in");
	fout.open("out_1");
	int i,j,k;
	char win;
	int t;
	fin>>t;
	for(k=1;k<=t;k++){
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		fin>>matrix[i][j];
		win = check();
		if(win == ' ')
			fout<<"Case #"<<k<<": "<<"Draw"<<endl;
		else if(win == 'i')
			fout<<"Case #"<<k<<": "<<"Game has not completed"<<endl;
		else
		fout<<"Case #"<<k<<": "<<win<<" won"<<endl;
	}
}
