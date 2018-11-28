#include <iostream>
#include <string>

using namespace std;

int main(){
	int numberOfTestCases;
	cin >> numberOfTestCases;
	
	for (int i =0; i <  numberOfTestCases;i++){
		int blockSize, X, Y;
		cin >> blockSize >> X >> Y;
		int volume = (X * Y);
		string yes;
		yes = "GABRIEL";
		string no;
		no = "RICHARD";
		string Answer;
		if (blockSize == 1){
			Answer = yes;
		}else if(blockSize == 2 && (volume%2 == 0)){
			Answer = yes;
		}else if(blockSize == 3 && (volume%3 == 0) && (X != 1 && Y != 1)){
			Answer = yes;
		}else if(blockSize == 4 && (volume%4 == 0) && (X != 1 && Y != 1) && (X != 2 && Y != 2)){
			Answer = yes;
		}else{
			Answer = no;
		}
		
		int testCase = i+1;
		cout << "Case #" << testCase << ": " << Answer << endl;
	}
	return 0;
}