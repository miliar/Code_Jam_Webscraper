//Google code jam 2015 round 1A
//Problem No.1: Mushroom Monster

#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");
	int caseNum;
	infile >> caseNum;
	for (int i = 1; i <= caseNum; i++){
		int N;
		infile >> N;
		int* mArray = new int[N];
		for (int j = 0; j < N; j++){
			infile >> mArray[j];
		}

		// Method 1
		int total1 = 0;
		for (int j = 1; j < N; j++){
			if (mArray[j] < mArray[j - 1]){
				total1 += mArray[j - 1] - mArray[j];
			}
		}

		// Method 2
		int total2 = 0;
		int maxInterval = 0;
		for (int j = 0; j < N - 1; j++){
			if (maxInterval < mArray[j] - mArray[j + 1]){
				maxInterval = mArray[j] - mArray[j + 1];
			}
		}
		for (int j = 0; j < N - 1; j++){
			if (mArray[j] <= maxInterval){
				total2 += mArray[j];
			}
			else{
				total2 += maxInterval;
			}
		}
		outfile << "Case #" << i << ": " << total1 << " " << total2 << endl;
		delete[] mArray;
	}
	infile.close();
	outfile.close();
	return 0;
}