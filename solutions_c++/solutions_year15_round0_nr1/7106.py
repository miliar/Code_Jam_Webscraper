#include<iostream>
#include<fstream>

using namespace std;

int solve(int input[], int S) {
	int i = 0;
	int total = 0;
	int need = 0;
	while(i < S) {
		total = total + input[i];
		if ((input[i] == 0) && (input[i+1] != 0)) {
			if (total <= i)
				{
				need = need + (i - total + 1);
				total = total + (i - total + 1);
			}
		}
		++i;
	}
	return need;
}

int main() {

	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("A-large.in");
	outputFile.open("output.txt");
	int values[10000];
	int i;
	int j = 0;
	int N;
	int S;
	if (inputFile.is_open()) {
		inputFile >> N;
		while( j < N) {
			inputFile >> S;
			inputFile.get();
			cout << S << "S" << '\n';
			i = 0;
			while( i <= S) {
				values[i] = inputFile.get() - 48;
				cout << values[i] << '\n';
				++i;
			}
			outputFile << "Case #" << j + 1 << ": " << solve(values, S) << "\n";
			j++;
		}
	}
	outputFile.close();
	inputFile.close();
	return 0;
}