#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include "conio.h"

using namespace std;

vector<int> getDigits(int n);
int getLastNumberCounted(int n);

int main(){
	cout<<"Enter input file:"<<endl;
	string inputFile;
	getline(cin, inputFile);
	ifstream fileIn(inputFile.c_str());
	ofstream fileOut("output.txt");
	
	int numTrials;
	fileIn >> numTrials;
	
	int n;
	int count = 1;
	while(fileIn >> n){
		int last = getLastNumberCounted(n);
		fileOut<<"Case #"<<count<<": ";
		count++;
		if(last==-1){
			fileOut<<"INSOMNIA"<<endl;
		}else{
			fileOut<<last<<endl;
		}
	}
	
	return 0;
}
vector<int> getDigits(int n){
	bool digits[10] = {false};
	vector<int> digitsSeen;
	
	bool running = true;
	while(running){
		digits[n%10] = true;
		if(n>=10){
			n = n/10;
		}
		else{
			running = false;
		}
	}
	
	for(int i=0;i<10;i++){
		if(digits[i]){
			digitsSeen.push_back(i);
		}
	}
	return digitsSeen;
}
int getLastNumberCounted(int n){
	bool digitsSeen[10] = {false};
	
	if(n==0){
		return -1;
	}
	int k = 1;
	bool running = true;
	while(running){
		vector<int> digits = getDigits(k*n);
		for(int i=0;i<digits.size();i++){
			digitsSeen[digits[i]] = true;
		}
		bool stop = true;
		for(int j=0;j<10;j++){
			if(!digitsSeen[j]){
				stop = false;
			}
		}
		if(stop){
			return k*n;
		}
		k++;
	}
}