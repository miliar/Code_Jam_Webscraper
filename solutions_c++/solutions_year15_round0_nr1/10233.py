#include<iostream>
#include<cstring>
#define MAXS 1000
using namespace std;

int main(){
	int testCaseCount;
	cin >> testCaseCount;
	
	int i;
	int solutionArray[testCaseCount];
	for(i = 0; i<testCaseCount;i++){
		int Smax;
		char shynessArray[MAXS] = {-1};
		cin >> Smax >> shynessArray;
		int friendsReqd = 0;
		int j;
		int currentSum = shynessArray[0] - (int)('0');
		for(j = 1; j<= Smax; j++){
			if((currentSum >= j) || ((shynessArray[j] - '0') == 0)){
				currentSum += (shynessArray[j] - (int)('0'));				
			}else{
				friendsReqd += (j - currentSum);				
				currentSum += friendsReqd;
				currentSum += (shynessArray[j] - (int)('0'));
			}
		}
		solutionArray[i] = friendsReqd;
	}	
	for(i = 0; i<testCaseCount;i++){
		cout << "Case #" << (i+1) << ": " << solutionArray[i] << endl;
	}
	return 0;
}
