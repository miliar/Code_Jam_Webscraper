#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream myfile ("A-large.in");
	ofstream outfile("A-large-answer.txt");
	int cases;
	long long num;
	myfile >> cases;
	long long* input = new long long[cases];
	for (int i = 0; i < cases; ++i) {
		myfile >> num;
		input[i] = num;
	}
	for (int j = 0; j < cases; ++j) {
		if (input[j] == 0) {
			outfile << "Case #" << j + 1 << ": INSOMNIA" << endl;
		}
		else {
			int n = 0;
			int complete = 0;
			int* arr = new int[10];
			for (int k = 0; k < 10; ++k) {
				arr[k] = 0;
			}
			while (complete == 0) {
				int index;
				long long copy;
				n++;
				copy = n*input[j];
				while (copy >= 10) {
					index = copy % 10;
					arr[index] = 1;
					copy = copy / 10;
				}
				arr[copy] = 1;
				for (int m = 0; m < 10; ++m) {
					complete = 1;
					if (arr[m] == 0) {
						complete = 0;
						break;
					}
				}
			}
			outfile << "Case #" << j + 1 << ": " << n*input[j] << endl;
		}
	}
	return 0;
}