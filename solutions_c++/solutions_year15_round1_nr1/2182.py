#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	int N;

	ifstream A_in;
	A_in.open("A-large.in");


	A_in >> N;

	ofstream A_out;
	A_out.open("A-large.out");
	
	

	for (int i = 0; i < N; i++) {
		
		int numberInputs = 0; 
		//cin >> numberInputs;
		A_in >> numberInputs;
		vector<int> inputs;
		for (int j = 0; j < numberInputs; j++) {
			int temp;
			//cin >> temp;
			A_in >> temp;
			inputs.push_back(temp);
		}

		int currentNumber = inputs.at(0);
		int minEaten = 0;

		for (int k = 1; k < inputs.size(); k++) {
			int temp = inputs.at(k);
			if (currentNumber > temp) {
				minEaten += (currentNumber - temp);
			}
			currentNumber = temp;
		}

		int maxEaten = 0;

		int maxDifference = 0;
		currentNumber = inputs.at(0);
		for (int k = 1; k < inputs.size(); k++) {
			if (currentNumber > inputs.at(k)) {
				if (currentNumber - inputs.at(k) > maxDifference)
					maxDifference = currentNumber - inputs.at(k);
			}
			currentNumber = inputs.at(k);
		}

		for (int k = 0; k < inputs.size() - 1; k++) {
			int temp = inputs.at(k);
			if (maxDifference > temp) {
				maxEaten += temp;
			}
			else {
				maxEaten += maxDifference;
			}
		}

		/*
		
		
		for (int k = 0; k < inputs.size() - 1; k++) {
			int temp = inputs.at(k);
			maxEaten += temp;
		}
		
		maxEaten -= inputs.at(inputs.size() - 1);
		*/
		//cout << "Case #" << (i + 1) << ": " << minEaten << " " << maxEaten << endl;
		A_out << "Case #" << (i + 1) << ": " << minEaten << " " << maxEaten << endl;
	}

	A_out.close();

	return 0;
}