#include <iostream>
#include <fstream>
#include <vector>

void printVector(std::vector<int> &v) {
	for (int i = 0; i < v.size(); i++) {
		//std::cout << v[i] << std::endl;
	}
}

bool check(std::vector<int> &v) {
	bool isComplete = true;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] == -1) {
			isComplete = false;
		}
	}
	//std::cout << isComplete << std::endl;
	return isComplete;
}

void eval(int n, std::vector<int> &v) {
	//std::cout << "Current Number: " << n << std::endl;
	while (n > 0) {
		int currDigit;
		currDigit = (n % 10);
		//std::cout << "Current Digit: " << currDigit << std::endl;
		v[currDigit] = 1;
		n /= 10;
	}
	printVector(v);
	//std::cout << "=============" << std::endl;
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
		fin >> n;
		if (n) {
			int newN = n;
			int multiplier = 1;
			std::vector<int> checkArray(10, -1);

			do {
				//std::cout << newN << std::endl;
				eval(newN, checkArray);
				if (check(checkArray)) break;
				newN = n*++multiplier;
			} while (true);

			fout << "Case #" << i+1 << ": " << newN << std::endl;
		}
		else {
			fout << "Case #" << i + 1 << ": " << "INSOMNIA" << std::endl;
		}
	}
}
