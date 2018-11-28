#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
	ifstream input;
	ofstream output;
	
	input.open(argv[1]);
	output.open("output.out");
	
	int cases;
	input >> cases;
	
	for (int c = 1; c <= cases; c++) {
		int row;
		input >> row;
		int numbers[4];
		
		for (int i = 1; i <= 4; i++) {
			if (i == row) {
				input >> numbers[0];
				input >> numbers[1];
				input >> numbers[2];
				input >> numbers[3];
			} else {
				int tmp;
				input >> tmp >> tmp >> tmp >> tmp;
			}
		}
		
		input >> row;
		
		int count = 0, num;
		for (int i = 1; i <= 4; i++) {
			if (i == row) {
				int tmp;
				
				for (int i = 0; i < 4; i++) {
					input >> tmp;

					for (int j = 0; j < 4; j++) {
						if (tmp == numbers[j]) {
							num = tmp;
							count++;
						}
					}
				}
			} else {
				int tmp;
				input >> tmp >> tmp >> tmp >> tmp;
			}
		}
		
		output << "Case #" << c << ": ";
		if (count == 0) {
			output << "Volunteer cheated!";
		} else if (count == 1) {
			output << num;
		} else {
			output << "Bad magician!";
		}
		if (c != cases) {
			output << endl;
		}
	}
	
	input.close();
	output.close();
}
