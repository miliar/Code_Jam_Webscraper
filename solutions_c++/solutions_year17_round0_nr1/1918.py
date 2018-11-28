#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <string>
using namespace std;

char FaceReverse(char Pancake){
	if (Pancake == '+')
		return('-');
	else
		return('+');
}

int main(){

	int NumberOfTestCases;
	scanf("%d", &NumberOfTestCases);

	vector<string> PancakeSequence(NumberOfTestCases);
	vector<int> PanSize(NumberOfTestCases);

	for (int i = 0; i < NumberOfTestCases; i++){
		getline(cin, PancakeSequence[i], ' ');
		scanf("%d", &PanSize[i]);
		int SeqLength = PancakeSequence[i].length();
		int FlipCount = 0;

		for (int j = 0; j < SeqLength; j++){
			if ((PancakeSequence[i][j] == '-') && (j + PanSize[i] <= SeqLength)){
				FlipCount++;
				for (int k = j; (k < SeqLength) && (k < j + PanSize[i]); k++)
					PancakeSequence[i][k] = FaceReverse(PancakeSequence[i][k]);
			}
		}
		bool isPossible = true;
		for (int j = 0; j < SeqLength; j++)
			if (PancakeSequence[i][j] == '-'){
				isPossible = false;
				break;
			}
		if (isPossible)
			printf("Case #%d: %d\n", i+1, FlipCount);
		else
			printf("Case #%d: IMPOSSIBLE\n", i+1);
	}

	return 0;
}