#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
int convert(int& binary, int target) {
	int temp = binary;
	int ans=0;
	int current = 1;
	while (temp > 0) {
		ans += (temp%10)*current;
		temp=temp / 10;
		current = current*target;
	}
	return ans;

}
int main() {
	ifstream input;
	input.open("input.in");
	ofstream output;
	output.open("output.in");
	int t;
	input >> t;
	int length;
	input >> length;
	int number;
	input >> number;
	int dec = 3;
	output << "Case #1:" << endl;
	for (int i = 0; i < number; ++i) {

		vector<int> vector(9, 0);
		int temp = dec;
		int size = 0;
		int current = 1;
		int bin = 0;
		while (temp > 0) {
			bin += (temp % 2)*current;
			temp = temp / 2;
			current = current * 10;
			++size;
		}
		dec = dec + 2;

		output << bin;
		for (int i = 0; i < length - 2 * size; ++i) {
			output << "0";
		}
		output << bin << " ";
		for (int i = 2; i < 11; ++i) {
			vector[i-2] = convert(bin, i);
			output << vector[i-2] << "  ";

		}
		output << endl;

	}
	input.close();
	output.close();
	return 0;
}