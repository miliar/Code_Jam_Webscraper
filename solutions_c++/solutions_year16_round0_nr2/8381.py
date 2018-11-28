#include <iostream>
#include <fstream>
#include <string>

int main() {

	std::ifstream fin("input.in");
	std::ofstream fout("output.out");

	if (!fin.is_open()) std::cout << "input.in was not open successfully" << std::endl;
	if (!fout.is_open()) std::cout << "output.out was not open successfully" << std::endl;
	std::string numCaseStr;
	int numCase;
	//fin >> numCase;
	std::getline(fin, numCaseStr);
	numCase = std::stoi(numCaseStr);
	for (int i = 0; i < numCase; i++) {
		//std::cout << "NEW CASE" << std::endl;
		std::string n;
		int numFlips = 0;
		int lastChar;
		std::getline(fin, n);

		int index = 0;
		lastChar = n[index];

		while (index < n.size()) {
			if (n[index] == lastChar) {
				index++;
				continue;
			}
			lastChar = n[index];
			numFlips++;
			index++;
		}

		if (n[n.size() - 1] == '-') numFlips++;
		std::cout << numFlips << std::endl;
		fout << "Case #" << i+1 << ": " << numFlips << std::endl;


	}
}
