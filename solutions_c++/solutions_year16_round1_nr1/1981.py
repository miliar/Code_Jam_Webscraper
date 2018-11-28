#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>
#include <cmath>
#include <sstream>

void printVector(std::vector<std::string> &v) {
	for (int i = 0; i < v.size(); i++) {
		std::cout << v[i] << std::endl;
	}
}

std::vector<std::string> &generateArtworks(int k, int c) {

	std::vector<std::string> v;

	// store all the possible combinations
	for (int i = 0; i < std::pow(2.0, k); i++) {
		v.push_back(std::bitset< 64 >(i).to_string());
	}

	for (int i = 0; i < v.size(); i++) {
		v[i] = v[i].substr(v[i].length() - (k), v[i].length() - 1);
		for (int j = 0; j < v[i].length(); j++) {
			std::stringstream ss;
			if (v[i][j] == '0') {
				for (int x = 0; x < k; x++) {
					ss << '0';
				}
			}
			else {
				for (int x = 0; x < k; x++) {
					ss << v[i];
				}
			}
		}
	}

	printVector(v);

	return v;
}

int main() {

	std::ifstream fin("input.in");
	std::ofstream fout("output.out");

	if (!fin.is_open()) std::cout << "input.in was not open successfully" << std::endl;
	if (!fout.is_open()) std::cout << "output.out was not open successfully" << std::endl;
	int numCase;
	fin >> numCase;
	for (int i = 0; i < numCase; i++) {
		std::string n;
		std::cout << "NEW TESTCASE" << std::endl;
		fin >> n;

		std::string lastWord;
		lastWord = "";

		for (int i = 0; i < n.size(); i++) {
			if (lastWord.size() == 0) {
				lastWord = n[i];
				continue;
			}
			if (lastWord.size() > 0) {
				if (n[i] >= lastWord[0]) {
					std::string newN = "";
					newN += n[i];
					newN += lastWord;
					lastWord = newN;
				}
				else {
					lastWord += n[i];
				}
				continue;
			}
			
		}



		fout << "Case #" << i + 1 << ": " << lastWord << std::endl;
	}
}
