//Ben
#include <iostream>
#include <fstream>
#include <cassert>
#include <string>



using namespace std;


int main(){

	ifstream inFile("A-large.in");
	assert(inFile);
	ofstream outFile("output.txt");

	int testCases;
	inFile >> testCases;

	

	for (int i = 0; i < testCases; i++){
		int N;
		inFile >> N;
		long long currNum;

		bool seen[10]{0};

		bool found = false;
		for (int j = 1; j < 10000 && !found; j++){
			
			currNum = N*j;
			string strNum = to_string(currNum);

			for (int k = 0; k < strNum.length(); k++){
				int index = strNum[k] - 48;
				seen[index] = true;
			}

			//See if she's asleep
			found = true;
			for (int k = 0; k < 10; k++){
				if (seen[k] == 0){
					found = false;
				}
			}
		}
		if (found == false){
			outFile << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		}
		else {
			outFile << "Case #" << i+1 << ": " << currNum << endl;
		}
	}




	return 0;
}