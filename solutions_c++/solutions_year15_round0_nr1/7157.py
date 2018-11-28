#include <iostream>
#include <cstdio>
#include <stdlib.h>

using namespace std;

int getCaseResult(){
	int result = 0,
			shynessListSize,
			standingGuys = 0;
	string str;

	cin >> shynessListSize >> str;
	standingGuys = (int)(str[0] - '0');
	for(int i=1; i<= shynessListSize; i++){
		int shynessNumber = i;
		int pplWithsShyness = (int)(str[i] - '0');
		if(standingGuys < shynessNumber && pplWithsShyness > 0){
			result += shynessNumber - standingGuys;
			standingGuys = shynessNumber;
		}
		standingGuys = standingGuys + pplWithsShyness;
	} 
	return result;
}

int main(){
	int testCase;
	cin >> testCase;
	for(int i=0; i<testCase; i++){
		int answer = getCaseResult();
		cout << "Case #" << i+1 << ": " << answer << endl;
	}
	return 0;
}