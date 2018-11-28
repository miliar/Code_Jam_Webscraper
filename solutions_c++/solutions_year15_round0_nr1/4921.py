#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main(){
	string info;
	ifstream problemFile;
	problemFile.open("A-large.in");
	ofstream problemSolution;
	problemSolution.open("problemA_Large.txt");
	int testCases;
	problemFile >> testCases;
	for (int i = 0; i < testCases; i++){
		
		int maxShyness;
		problemFile >> maxShyness;
		cout << "shyness : " << maxShyness << endl;
		int *shyness = (int*)malloc(sizeof(int) * (maxShyness + 1));
		for (int j = 0; j < maxShyness + 1; j++){
			int shyPeople;
			char c = ' ';
			while (c == ' '){
				c = problemFile.get();
			}
			shyness[j] = c - '0';
			cout << shyness[j] << endl;
		}
		
		int peopleStanding = 0;
		int peopleNeeded = 0;
		for (int j = 0; j < maxShyness + 1; j++){
			peopleStanding += shyness[j];
			if (peopleStanding == j){
				peopleNeeded++;
				peopleStanding++;
			}
		}
		problemSolution << "Case #" << (i + 1) << ": " << peopleNeeded << "\n";
	} 
	problemFile.close(); problemSolution.close();
}