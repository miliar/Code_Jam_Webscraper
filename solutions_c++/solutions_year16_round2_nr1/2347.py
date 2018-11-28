#include <iostream>
#include <fstream>
#include <string>

int count(std::string str, std::ofstream& output) {
	int* occ = new int['Z' + 1];
	for (int i = 0; i<'Z' + 1;i++) {
		occ[i] = 0;
	}
	for (unsigned int j = 0; j<str.size();j++) {
		occ[((int)str[j])] += 1;
	}
	int * result = new int [10];
	for (int i = 0; i<10;i++) {
		result[i] = 0;
	}
	result[0] = occ['Z'];
	result[2] = occ['W'];
	result[4] = occ['U'];
	result[6] = occ['X'];
	result[8] = occ['G'];
	result[5] = occ['F'] - result[4];
	result[7] = occ['S'] - result[6];
	result[9] = occ['I'] - result[5] - result[6] - result[8];
	result[1] = occ['O'] - result[0] - result[2] - result[4];
	result[3] = occ['R'] - result[0] - result[4];
	for (int i = 0; i<10;i++) {
		for (int j = 0; j < result[i];j++) {
			output << i;
		}
	}
	delete[] result;
	delete[] occ;
	return 0;
}

int main(int argc, char **argv) {
	int t;
	std::ifstream input;
	std::ofstream output;
	
	input.open("A-large.in");
	output.open("out.txt");
	input >> t;
	for (int i = 1;i<=t;i++) {
		std::string n;
		input >> n;
		output << "Case #" << i << ": ";
		count(n,output);
		output << std::endl;
	
	}
    input.close();
	output.close();
	return 0;
}
