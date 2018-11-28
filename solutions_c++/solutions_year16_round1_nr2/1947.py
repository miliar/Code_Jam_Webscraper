#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>
#include <cmath>
#include <sstream>

void printVector(std::vector<int> &v) {
	for (int i = 0; i < v.size(); i++) {
		std::cout << v[i] << std::endl;
	}
}

int main() {

	std::ifstream fin("input.in");
	std::ofstream fout("output.out");

	if (!fin.is_open()) std::cout << "input.in was not open successfully" << std::endl;
	if (!fout.is_open()) std::cout << "output.out was not open successfully" << std::endl;
	int numCase;
	fin >> numCase;
	for (int i = 0; i < numCase; i++) {
		int n;
		int maxNum = 0;
		fin >> n;
		std::vector<int> intCount(2501, 0);
		for (int j = 0; j < (2 * n - 1); j++) {
			for (int x = 0; x < n; x++) {
				int number;
				fin >> number;
				// update maxNumber
				if (number > maxNum) {
					maxNum = number;
				}
				intCount[number]++;
				std::cout << number << ", " << intCount[number] << std::endl;
			}
		}

		std::cout << "Max Number" << maxNum << std::endl;

		std::vector<int> solution;

		for (int y = 1; y <= maxNum; y++) {
			if (intCount[y] % 2 == 1) {
				solution.push_back(y);
			}
		}

		printVector(solution);



		//std::cout << "Case #" << i + 1 << ": " << lastWord << std::endl;



		fout << "Case #" << i + 1 << ":";
		for (int v = 0; v < solution.size(); v++) {
			fout << " " << solution[v];
		}
		fout << std::endl;

	}
}
