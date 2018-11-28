#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
#define x 0
#define o 1
#define t 2
#define n -1
#define xwon 1
#define owon 2
#define draw 3
#define nf 0
int checkRow(int *input){
	int i=0;
	int xnum = 0;
	int onum = 0;
	for( i = 0 ;i <4; i++){
		if(input[i] ==x) xnum++;
		else if(input[i] ==o) onum++;
		else if(input[i] ==t) {xnum++;onum++;}
	}
	if(xnum == 4) 
		return xwon;
	if(onum == 4) 
		return owon;
	return draw;
}
int whowon(int input[4][4] ){
	int i,j;
	int tempInput[4];
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			tempInput[j] = input[i][j];

		}
		if(checkRow(tempInput)!=3) return checkRow(tempInput);

	}
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			tempInput[j] = input[j][i];

		}
		if(checkRow(tempInput)!=3) 
				return checkRow(tempInput);

	}
		for(j=0;j<4;j++){
			tempInput[j] = input[j][j];

		}
					if(checkRow(tempInput)!=3) return checkRow(tempInput);

		for(j=0;j<4;j++){
			tempInput[j] = input[j][3-j];

		}
		if(checkRow(tempInput)!=3) return checkRow(tempInput);

	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(input[i][j]<0) 
				return nf;

		}
	}

	return draw;
}
int main(int argc, char *argv[]){

	ifstream in("B-large-practice.in");
	ofstream out("out.txt");
	int  testcases;
	in >> testcases;
	char temp;
	int input[4][4];
	for(int i=0;i<testcases;i++){
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				in>>temp;
				if(temp=='X')input[j][k] = x;
				else if(temp == 'O') input[j][k]=o;
				else if(temp =='T') input[j][k] = t;
				else if(temp =='.') 
					input[j][k]=n;
			}
		}
		int result = whowon(input);
		if(result == xwon) out<<"Case #"<<i+1<<": X won"<<endl;
		else if(result == owon) out<<"Case #"<<i+1<<": O won"<<endl;
		else if(result == draw) out<<"Case #"<<i+1<<": Draw"<<endl;	
		else if(result == nf) out<<"Case #"<<i+1<<": Game has not completed"<<endl;

	}
	return 1;
}