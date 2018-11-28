#include <stdio.h>
#include <iostream>

using namespace std;

int partition(double *input, int left, int right){
    double pivot;
	pivot = input[right];
	int storeIndex = left;
    for(; left < right; left++){
        if (input[left] < pivot){
            double tmp = input[left];
            input[left] = input[storeIndex];
            input[storeIndex] = tmp;
			storeIndex++;
        }
	}
	double tmp = input[left];
	input[left] = input[storeIndex];
	input[storeIndex] = tmp;
    return storeIndex;                                                                        
}

//Quicksort recursively calls itself/partition
void quickSort(double *input, int left, int right){
    if ( left < right ){
        int storeIndex = partition(input, left, right);                 //separates left( < pivot) and right side( > pivot) and returns location of the pivot on the array
		quickSort(input, left, storeIndex-1);                                   //sorts left side
        quickSort(input, storeIndex+1, right);                                  //sorts right side
    }
}


const int countDeceit(const double *inputN, const double *inputK, const int numBlocks){
	int Nwins = 0;
	int Ksmallest = 0;
	int Klargest = numBlocks;
	for(int i = 0; i <= numBlocks; i++){
		if(inputN[i] < inputK[Ksmallest]){
			Klargest--;
//			cout << inputN[i] << " removes " << inputK[Klargest + 1] << endl;
		} else {
			Nwins++;
			Ksmallest++;
//			cout << inputN[i] << " beats " << inputK[Ksmallest - 1] << endl;
		}
	}
	return Nwins;
}

int countWar(double *inputN, double *inputK, int numBlocks){
	int Nwins;
	int Kwins = 0;
	double pivot;
	bool currentRound = 1;
	int j = 0;
	for(int i = 0; i < numBlocks; i++){
		pivot = inputN[i];
		while((j < numBlocks) &&(currentRound)){
			if(pivot < inputK[j]){
//				cout << "K beats " << pivot << " with " << inputK[j]<< endl;
				Kwins++;
				inputK[j] = -1;
				currentRound = 0;
			} else {
				j++;
			}
		}
		if(currentRound){
			int Ksmallest = 0;
			for(int x = 1; x < numBlocks; x++){
				if((inputK[Ksmallest] == -1) || (inputK[Ksmallest] > inputK[x] )){
					Ksmallest = x;
				}
			}
			inputK[Ksmallest] = -1;
		}
		j = 0;
		currentRound = 1;
	}
	Nwins = numBlocks - Kwins;
	return Nwins;
}

int main(int argc, char **argv)
{
	double inputN[10];
	double inputK[10];
	
	int numTestCases;
	cin >> numTestCases;
	
	int numBlocks;

	int caseDResults[100];
	int caseWResults[100];
	for(int caseNum = 0; caseNum < numTestCases; caseNum++){
		cin >> numBlocks;
		for(int i = 0; i < numBlocks; i++){
			cin >> inputN[i];
		}
		
		for(int i = 0; i < numBlocks; i++){
			cin >> inputK[i];
		}
		
		quickSort(inputN, 0, (numBlocks-1));

		quickSort(inputK, 0, (numBlocks-1));

		caseDResults[caseNum] = countDeceit(inputN, inputK, (numBlocks-1));
		caseWResults[caseNum] = countWar(inputN, inputK, numBlocks);
	}
	for(int i = 0; i < numTestCases; i++){
		cout << "Case #" << (i+1) << ": ";
		cout << caseDResults[i] << " " << caseWResults[i] << endl;
	}
	
	return 0;
}
