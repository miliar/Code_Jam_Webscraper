#include<iostream>
#include<fstream>

using namespace std;


int main(){
	int T;
	int k;
	int SInt;
	int * aSInt;
	int result;
	int p;
	
	// 파일 입력 (쓰기)
	ofstream outFile("output.txt");
	ifstream inFile("A-small-attempt4.in");

	inFile >> T;
	for (int i = 0; i < T; i++){
		p = 0;
		result = 0;
		inFile >> k;
		aSInt = new int[k + 1];
		inFile >> SInt;
		for (int j = 0; j < k+1; j++){
			aSInt[k - j]=SInt%10;
			SInt /= 10;
		}
		for (int j = 0; j < k + 1; j++){
			if (aSInt[j] != 0){
				if (p < j){
					result+=(j-p);
					p = j;
				}
			}
			p += aSInt[j];
		}
		outFile <<"Case #"<<i+1<<": "<< result;
		if (i+1 != T){
			outFile << endl;
		}
	}

	return 0;
}