#include<iostream>
#include<fstream>
#include<string>
/*

jwkim0000@gmail.com
CodeJam nickname : JackRabbit

*/
using namespace std;

inline int getResult(int lawn[100][100], int raw, int col);
inline int isValid(int lawn[100][100], int raw, int col, int n, int m);
int main(){
	int howMany=0;
	string str;
	int raw, col;
	int lawn[100][100];

	ifstream fin("B-large.in");
	ofstream out("B-large.out");

	fin>>howMany;
	for(int k=0; k<howMany;k++){
		fin>>raw>>col;
		//	input
		for(int i=0;i<raw;i++){
			for(int j=0;j<col;j++){
				fin>>lawn[i][j];
			}
		}

		//	output
		out<<"Case #"<<(k+1)<<": ";
		//cout<<"Case #"<<(k+1)<<": ";

		if(getResult(lawn, raw, col)){
			out<<"YES"<<endl;
			//cout<<"YES"<<endl;
		}
		else{
			out<<"NO"<<endl;
			//cout<<"NO"<<endl;
		}
	}
	out.close();
	return 0;
}

inline int getResult(int lawn[100][100], int raw, int col){
	
	for(int i=0;i<raw;i++){
		for(int j=0; j<col; j++){
			if(!isValid(lawn,raw,col,i,j))
				return 0;
		}
	}
	return 1;
}

inline int isValid(int lawn[100][100], int raw, int col, int n, int m){
	int flag = 1;
	for(int i=0;i<raw;i++){
		if(lawn[i][m]>lawn[n][m] && i!=n)
			flag = 0;
	}
	if(flag==0){
		flag=1;
		for(int j=0;j<col;j++){
			if(lawn[n][j]>lawn[n][m] && j!= m)
				flag = 0;
		}
	}
	return flag;
}