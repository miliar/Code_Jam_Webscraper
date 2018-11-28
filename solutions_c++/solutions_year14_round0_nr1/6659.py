#include <fstream>
#include <iostream>

using namespace std;

int main(){
	ifstream fin;
	fin.open("A-small-attempt0.in.txt");
	ofstream fout;
	fout.open("output.txt");
	int times;
	fin>>times;
	int ansFirst, ansSecond;
	int boardFirst[4][4];
	int boardSecond[4][4];
	for(int caseNo=1;caseNo<=times;caseNo++){
		fin>>ansFirst;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				fin>>boardFirst[i][j];
		fin>>ansSecond;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				fin>>boardSecond[i][j];
		int matched=0,matNum;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(boardFirst[ansFirst-1][i]==boardSecond[ansSecond-1][j]){
					matched++;
					matNum=boardFirst[ansFirst-1][i];
				}
			}
		}
		fout<<"Case #"<<caseNo<<": ";
		if(matched==1)
			fout<<matNum<<'\n';
		else if(matched==0)
			fout<<"Volunteer cheated!"<<'\n';
		else
			fout<<"Bad magician!"<<'\n';
	}
	return 0;
}