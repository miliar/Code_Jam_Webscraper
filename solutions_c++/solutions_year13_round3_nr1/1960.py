#include <climits>
#include <vector>
#include <iostream>
#include <map>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

string name;
long long n;

void readCaseInput(){
	cin >> name;
	cin >> n;
}

bool isConsonant(char c){
	return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}

int solveCase(){
	long long res = 0;
	long long numStarts = 0;
	long long numCons = 0;
	for(int i = 0; i < name.size(); i++){
		if(isConsonant(name[i]))
			numCons++;
		else
			numCons = 0;
		
		if(numCons < n)
			res += numStarts;
		else {
			res += (i + 1 - n) + 1;
			numStarts = (i + 1 - n) + 1;
		}
	}
	return res;
}

int main(){
	int T; cin >> T;
	for(int i = 0; i < T; i++){
		readCaseInput();
		int res = solveCase();
		cout << "Case #" << (i+1) << ": " << res << endl;
	}
}




