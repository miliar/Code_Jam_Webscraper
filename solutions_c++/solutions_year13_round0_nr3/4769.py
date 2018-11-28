#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include "math.h"
using namespace std;

bool isPalindrome(unsigned long input){
	unsigned long tmp=input;
	unsigned long mag=1;
	while((tmp=tmp/10) != 0) mag*=10;
	tmp = 0;
	for(int i=1; i<=mag; i*=10){
		tmp += (mag/i)*((input/i)%10);
	}
	return tmp==input;
}

int main(int argc, char const *argv[]){
	if(argc != 2){
		cout<<"Error in Input"<<endl;
		return 0;
	}
	ifstream inFile;
	ofstream outFile;
	inFile.open(argv[1]);
	outFile.open("output.txt", ios::trunc | ios::out);
	if(!(inFile.is_open() && outFile.is_open()) ){
		cout << "can't open files"<<endl;
		return 0;
	}

	int N;
	unsigned long min, max, minSquare, maxSquare, fairCount;
	inFile >> N;
	cout << "Running through " << N << " Iterations" << endl;
	for(int count=0; count<N; count++){
		fairCount = 0;
		inFile>>min;
		inFile>>max;
		minSquare = ceil(sqrt(min));
		maxSquare = floor(sqrt(max));

		for(unsigned long i=minSquare; i<=maxSquare; i++){
			if(isPalindrome(i)&&isPalindrome(i*i)){
				cout << "found fairSquare " << i*i << endl;
				fairCount++;
			}
		}

		outFile << "Case #" << count+1 << ": " << fairCount << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}
