#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <fstream>

using namespace std;

void
createDigitMap(long N, map<int, int>& dMap) {	
	while (N) {
		dMap[N % 10]++;
		N = N / 10;
	}	
}

bool
foundAllDigits(map<int, int> dMap) {
	int counter = 0;
	for (int key = 0; key < 10; key++) {
		if (dMap.find(key) == dMap.end())
			return false;		
	}
	return true;
}

long
splitAndMapDigits(long N) {
	map<int,int> digitMap;	
	int i = 1;

	while(1) {
		if (N == 0)
			return(0);		
		
		createDigitMap(N*i, digitMap);
		
		if (foundAllDigits(digitMap))
			return(N*i);
		i++;
	}
}

int main() {
	long N;
	long sleepingN;
	ofstream outFileStream;
	outFileStream.open("output.txt");

	int testNum;
	cin >> testNum;

	for (int test = 0; test < testNum; test++) {
		cout << "Case #" << test+1 << ":" << " ";
		outFileStream << "Case #" << test+1 << ":" << " ";
		cin >> N;
		

		sleepingN = splitAndMapDigits(N);
		if (sleepingN == 0) {
			cout << "INSOMNIA" << endl;
			outFileStream << "INSOMNIA" << endl;
		}
		else {
			cout << sleepingN << endl;
			outFileStream << sleepingN << endl;
		}
	}

	return(0);
}

