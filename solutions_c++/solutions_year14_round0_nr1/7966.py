#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]){
	int tests;
	cin >> tests;
	int n = tests;
	int firstAns;
	int firstMat[4][4];
	int cases = 1;
	string *output = new string[tests];

	while (tests > 0){
		int secondAns;
		cin >> firstAns;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> firstMat[i][j];
		cin >> secondAns;
		int secondMat[4][4];
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> secondMat[i][j];

		firstAns--;
		secondAns--;
		int count = 0;
		int Ans = 0;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (firstMat[firstAns][i] == secondMat[secondAns][j]){
					count++;
					Ans = firstMat[firstAns][i];
				}
			}
		}
		string str = to_string(cases);
		if (count == 0)
			output[cases-1] = "Case #" + str + ": Volunteer cheated!";
		else if (count > 1)
			output[cases - 1] = "Case #" + str + ": Bad magician!";
		else
			output[cases - 1] = "Case #" + str + ": " +  to_string(Ans);
		tests--;
		cases++;
	}
	ofstream outputFile("program3data.txt");
	for (int i = 0; i < n; i++){
		outputFile << output[i] << "\n";
	}
	outputFile.close();
	cin.ignore();
	cin.ignore();
	cin.ignore();
	return 0;
}