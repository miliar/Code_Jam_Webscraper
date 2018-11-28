#include <iostream>
#include <fstream>
using namespace std;

void compute(int a[], int b[]);

ofstream outFile;
ifstream inFile;

int main(int argc, const char* argv[]) {
	int a[4];
	int b[4];
	int N;
 	
  	outFile.open("out.txt");
	inFile.open(argv[1]);
	inFile >> N;
	int row;
	int dummy;
	for (int i = 1; i <= N; i++){
		outFile << "Case #" << i << ": ";
		inFile >> row;
		for (int j = 1; j <= 4; j++){
			for (int k = 0; k < 4; k++)
			if (j == row)
				inFile >> a[k];
			else
				inFile >> dummy;
		}
		inFile >> row;
		for (int j = 1; j <= 4; j++){
			for (int k = 0; k < 4; k++)
				if (j == row)
					inFile >> b[k];
				else
					inFile >> dummy;
		}	
		compute(a,b);
	}
	inFile.close();
	outFile.close();
	return 0;
}

void compute(int a[], int b[]) {
	int result;
	int count = 0;
	for (int i = 0; i < 4; i++)
	for (int j = 0; j < 4; j++)
	if (a[i] == b[j]) {
		result = a[i];
		count++;
	}
	if (count == 0) {
		outFile << "Volunteer cheated!" << std::endl;
	}
	else if (count == 1) {
		outFile << result << std::endl;
	}
	else {
		outFile << "Bad magician!" << std::endl;
	}
}
