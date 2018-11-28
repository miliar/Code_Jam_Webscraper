#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <sstream>

using namespace std;

int numStanding;
int extraCount;
int smax;

long int toInt(char s) {
	return (s - '0');
}

bool willStand(int SL){
	if (numStanding >= SL){
		return true;
	}
	else
	{
		return false;
	}
}

int solve(string x){
	for (int k = 0; k <= smax; k++){
		while (!willStand(k)){
			extraCount++;
			numStanding++;
		}
		numStanding += toInt(x[k]);
	}
	return extraCount;
}


int main(){

	int cases = 0;
	string s;

	cin >> cases;
	for (int c = 1; c <= cases; c++){
		numStanding = 0;
		extraCount = 0;
		cin >> smax >> s;
		cout << "Case #" << c << ": " << solve(s) << endl;
	}

//	int end;
//	cin >> end;
	return 0;
}