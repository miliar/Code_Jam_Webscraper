#include <string>
#include <fstream>
#include <iostream>	


using namespace std;
ifstream infile("input.in");
ofstream outfile("output.in");

int testCases;
string ordering;
int maxShyness;
int main(){
	int caseN = 1;
	infile >> testCases;
	int Cases = testCases;
	// cout << Cases << " CASES" << endl;
	while(Cases--){
		infile >> maxShyness;
		infile >> ordering;
		int X[ordering.length()];
		for(int i =0; i<ordering.length(); i++){
			//cout << ordering[i] << " " << endl;
			X[i] = ordering[i]-48;
			//cout << X[i] << " " << endl;
		}
		

		int NumStanding = X[0];
		int peopleToInvite = 0;
		
		for(int i = 1; i< ordering.length(); i++){
			if(i > NumStanding){
				int diff = i - NumStanding;
				peopleToInvite += diff;
				NumStanding += diff;
				NumStanding += X[i];
			}
			else{
				NumStanding += X[i];
			}
		
		}
		// cout << endl;		
		outfile << "Case #" << caseN << ": " << peopleToInvite << endl;
		caseN++;
	}
	return 0;
}