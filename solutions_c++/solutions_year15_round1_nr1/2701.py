#include <iostream>
#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cstring>
#include <functional>
#include <list>
#include <map>
#include <numeric>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <fstream>

using namespace std;

const string fileName = "MushroomMonster";

int firstMethod(const vector<int>& sequence){
	int result = 0;

	for (int i = 0; i < sequence.size() - 1; i++){
		int nowValue = sequence[i] - sequence[i + 1];
		if (nowValue >= 0){
			result += nowValue;
		}
	}

	return result;
}

int secondMethod(const vector<int>& sequence){
	double rate = 0.0;

	for (int i = 0; i < sequence.size() - 1; i++){
		int next = sequence[i]>=sequence[i + 1] ? sequence[i + 1] : sequence[i];
		rate = max(rate, double(sequence[i]-next)/10.0);
	}

	int result = 0;
	for (int i = 0; i < sequence.size() - 1; i++){
		int possibleEating = rate*10;
		result += min(sequence[i], possibleEating);
	}

	return result;
}

int main(){
	ofstream file(fileName + ".txt", ofstream::out);

	int testCase;
	cin >> testCase;
	for (int t = 0; t < testCase; t++){
		int size;
		cin >> size;
		
		vector<int> sequence(size);
		for (int i = 0; i < size; i++){
			cin >> sequence[i];
		}

		file << "Case #" << (t + 1) << ": " << firstMethod(sequence)<< " " << secondMethod(sequence) << endl;
	}
	
	file.close();
	return 0;
}