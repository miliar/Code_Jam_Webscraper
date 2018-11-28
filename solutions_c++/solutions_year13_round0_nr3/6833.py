#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
using namespace std;

int readFile(char[], int[][2]);
bool isPallindrome(int number);

int main(int argc, char *argv[]) {
	int i, j, count = 0;
	double upper, lower;

	int array[100][2];
	int number_of_lines = readFile(argv[1], array);
	
	ofstream output;
	output.open("out.txt");
	for (i = 0; i < number_of_lines; i++) {
		lower = sqrt(array[i][0]);
		upper = sqrt(array[i][1]);

		for (j = ceil(lower); j <= floor(upper); j++) {
			if (isPallindrome(j)) {
				if (isPallindrome(j*j)) {
					count++;
					cout << j << endl;
				}
			}
		}
		output << "Case #" << i+1 << ": " << count << endl;
		count = 0;
	}
	output.close();
	return 0;
}

int readFile(char filename[], int array[][2]) {
	int number_of_lines, i = 0;
	ifstream file;
	file.open(filename);
	file >> number_of_lines;
	while (!file.eof()) {
		file >> array[i][0];
		file >> array[i][1];
		i++;
	}
	file.close();
	return number_of_lines;
}

bool isPallindrome(int number) {
	int string_length, half_string_length, i;
	string result;
	stringstream s;
	
	s << number;
	result = s.str();

	string_length = result.length();
	half_string_length = string_length/2;
	for (i = 0; i <= half_string_length; i++) {
		if (result[i] != result[string_length - 1 - i]) {
			return false;
		}
	}
	return true;
}
