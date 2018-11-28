#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
// Developed in Visual Studio 2014
class MagicTrick {
public:
	MagicTrick(int firstAnswer, std::vector<std::vector<int>> firstArrangement, int secondAnswer, std::vector<std::vector<int>> secondArrangement)
	{
		std::vector<int> firstRow = firstArrangement[firstAnswer];
		std::vector<int> secondRow = secondArrangement[secondAnswer];

		std::vector<int> answers;
		for (int i = 0; i < 4; i++) { // firstRow
			for (int j = 0; j < 4; j++) { // secondRow
				if (firstRow[i] == secondRow[j]) {
					answers.push_back(firstRow[i]);
				}
			}
		}

		if (answers.size() > 1) {
			result = "Bad magician!"; 
		}
		else if (answers.size() == 0) {
			result = "Volunteer cheated!";
		}
		else result = std::to_string(answers[0]);
	}
	std::string answer() {
		return result;
	}
private:
	std::string result;
};

int main() {
	FILE *f = fopen("output.txt", "w");
	if (f == NULL)
	{
		printf("Error opening file!\n");
		exit(1);
	}

	std::ifstream input("input.in");
	if (input.is_open()) { // Input file found
		std::string line;
		getline(input, line);
		int numTestCases = atoi(line.c_str());
		for (int k = 0; k < numTestCases; k++) { // For each test case
			getline(input, line);
			int firstAnswer = atoi(line.c_str()) - 1; 

			std::vector<std::vector<int>> firstArrangement;
			for (int i = 0; i < 4; i++) {
				std::vector<int> newVec;
				firstArrangement.push_back(newVec);
				getline(input, line);

				std::istringstream row(line);
				while (row) {
					std::string temp;
					row >> temp;
					firstArrangement[i].push_back(atoi(temp.c_str()));
				}
			}

			getline(input, line);
			int secondAnswer = atoi(line.c_str()) - 1;

			std::vector<std::vector<int>> secondArrangement;
			for (int i = 0; i < 4; i++) {
				std::vector<int> newVec;
				secondArrangement.push_back(newVec);
				getline(input, line);

				std::istringstream row(line);
				while (row) {
					std::string temp;
					row >> temp;
					secondArrangement[i].push_back(atoi(temp.c_str()));
				}
			}

			MagicTrick testCase(firstAnswer, firstArrangement, secondAnswer, secondArrangement);

			std::cout << testCase.answer() << std::endl;

			fprintf(f, "Case #%d: %s\n", k + 1, (testCase.answer()).c_str());
		}
		input.close();
		fclose(f);

		return 0; // End Program
	}
	else {
		std::cout << "No input file found";
		return 0; // Abort
	}
}