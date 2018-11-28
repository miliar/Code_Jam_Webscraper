#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
// Developed in Visual Studio 2013

class CountingSheep {
public:
	CountingSheep(int n) {
		if (n == 0) return;
		else {
			for (int i = 0; i < 10; ++i)
				seen[i] = false;
			int original = n;
			while (!solvable) {
				//std::cout << "n = " << n << std::endl;
				if (n < 0) return;
				updateSeen(n);
				updateSolvable();
				if (solvable) {
					answer = n;
					//std::cout << " answer = " << answer << std::endl;
					return;
				}
				else n += original;
			}
		}

	}
	int getAnswer() {
		return answer;
	}
	void updateSeen(int n) {
		while (n != 0) {
			int unit = n % 10;
			seen[unit] = true;
			//std::cout << unit << std::endl;
			n /= 10;
		}
	}
	void updateSolvable() {
		for (int i = 0; i < 10; ++i) {
			if (seen[i] == false) return;
		}
		solvable = true;
	}
	bool isSolvable() {
		return solvable;
	}
private:
	int answer;
	bool solvable = false;
	bool seen[10];
};

int main() {
	FILE *fp = fopen("output.txt", "w");
	if (fp == NULL)
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
			std::istringstream parameters(line);
			std::string temp;

			parameters >> temp;
			int n = atoi(temp.c_str());

			//std::cout << "Case #" << k + 1 << ": ";
			CountingSheep solution(n);

			std::string answer;
			//std::cout << solution.getAnswer() << std::endl;
			if (solution.isSolvable()) answer = std::to_string(solution.getAnswer());
			else answer = "INSOMNIA";
			std::cout << answer.c_str() << std::endl;

			fprintf(fp, "Case #%d: %s\n", k + 1, (answer).c_str());
		}
		input.close();
		fclose(fp);

		return 0; // End Program
	}
	else {
		std::cout << "No input file found";
		return 0; // Abort
	}
}