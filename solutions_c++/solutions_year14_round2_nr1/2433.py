
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w+", stdout);
	int t;
    cin >> t;
	string words[100];
	int moveCounter;
	int ULetters[100];
	char currentChar[100 * 100];
	int numLetters[100 * 100];
	int numLetterTotal[100];
	double numLettersAvgF[100];
	double numLettersAvgC[100];




	for(int ti = 0; ti < t; ti++){
		
		cout << "Case #" << (ti+1) << ": ";

		int numStr;
		cin>>numStr;

		moveCounter = 0;

		for(int i = 0; i < 100; i++){
			ULetters[i] = 0;
			numLettersAvgF[i] = 0;
			numLettersAvgC[i] = 0;
			numLetterTotal[i] = 0;
		}

		for(int i = 0; i < 10000; i++){
			numLetters[i] = 0;
		}

		for(int i = 0; i < numStr; i++){
			cin >> words[i];

			ULetters[i] = 1;

			if(words[i][0] != NULL){
				currentChar[i*100] = words[i][0];
				numLetters[i*100] = 1;
			}

			for(int j = 1; j < 100; j++){
				if(j < words[i].length()){
					if(words[i][j] == words[i][j-1]){
						numLetters[i*100 + ULetters[i]-1]++;
					}
					else{
						ULetters[i]++;
						currentChar[i*100 + ULetters[i]-1] = words[i][j];
						numLetters[i*100 + ULetters[i]-1]++;
					}
				}
				else{
					break;
				}
			}
			
		}

		
		for(int i = 0; i < numStr; i++){
			for(int j = 0; j < ULetters[0]; j++){
				numLetterTotal[j] = numLetterTotal[j] + numLetters[i*100 + j];
			}
		}
		
		
		for(int i = 0; i < ULetters[0]; i++){
			numLettersAvgF[i] = floor(double(numLetterTotal[i])/double(numStr));
			numLettersAvgC[i] = ceil(double(numLetterTotal[i])/double(numStr));
		}
		

		int possible = 1;

		for(int i = 1; i < numStr; i++){
			if(ULetters[i] != ULetters[0]){
				possible = 0;
				break;
			}
			for(int j = 0; j < ULetters[0]; j++){
				if(currentChar[j + 100*i] != currentChar[j]){
					possible = 0; 
					break;
				}
			}
			if(possible == 0){break;}
		}

		if(possible){
			int movesF = 0;
			int movesC = 0;

			for(int i = 0; i < ULetters[0]; i++){
				for(int j = 0; j < numStr; j++){
					movesF = movesF + abs(numLetters[j * 100 + i] - numLettersAvgF[i]);
					movesC = movesC + abs(numLetters[j * 100 + i] - numLettersAvgC[i]);
				}
			}
			if(movesF < movesC){
				cout<<movesF;
			}
			else{
				cout<<movesC;
			}

		}
		else{
			cout<< "Fegla Won";
		}
		
		cout << endl;

	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}

/*
for(int i = 0; i < N; i++){
			for(int j = 0; j < L; j++){
				outletAnd[j + i*40] = outletOut[j + i*40] && outletIn[j + i*40];
				if(i == 0){
					if(outletAnd[j + i*40] == 0){
						switchCount++;
					}
				}
				else{
					if(outletAnd[j + i*40] != outletAnd[j + (i-1)*40]){
						notPossible = 1;
					}
				}
				if(notPossible){break;}
			}
			if(notPossible){break;}
		}
*/